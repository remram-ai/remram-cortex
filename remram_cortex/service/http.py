from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from ..config import CortexSettings
from ..models import BoundaryInput, dataclass_dict, to_primitive
from ..runtime import CortexPreparationRuntime


def _sanitize_segment(value: str) -> str:
    return "".join(character if character.isalnum() or character in "._-" else "_" for character in value)


@dataclass(slots=True)
class CortexBridgeHttpService:
    runtime: CortexPreparationRuntime

    @property
    def settings(self) -> CortexSettings:
        return self.runtime.settings

    def health_payload(self) -> dict[str, Any]:
        self.settings.ensure_layout()
        return {
            "status": "ok",
            "service": "cortex-bridge-prep",
            "data_root": self.settings.data_root.as_posix(),
        }

    def latest_startup_bundle(self, session_id: str) -> dict[str, Any] | None:
        session_root = self.settings.startup_bundle_root / _sanitize_segment(session_id)
        if not session_root.exists():
            return None
        bundle_paths = sorted(session_root.glob("*.json"))
        if not bundle_paths:
            return None
        latest_path = bundle_paths[-1]
        return json.loads(latest_path.read_text(encoding="utf-8"))

    def record_hook_event(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.settings.ensure_layout()
        session_id = _sanitize_segment(str(payload.get("session_id") or "unknown"))
        event_name = _sanitize_segment(str(payload.get("event") or "unknown"))
        event_root = self.settings.openclaw_hook_event_root / session_id
        event_root.mkdir(parents=True, exist_ok=True)
        output_path = event_root / f"{event_name}__{threading.get_native_id()}__{len(list(event_root.glob('*.json'))):04d}.json"
        output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return {
            "status": "accepted",
            "stored_at": output_path.as_posix(),
        }

    def process_boundary(
        self,
        payload: dict[str, Any],
        *,
        mode: str = "standard",
        preference_overlays: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        boundary = BoundaryInput.from_dict(payload)
        result = self.runtime.run_boundary(
            boundary,
            mode=mode,
            preference_overlays=preference_overlays,
        )
        startup_bundle = self.latest_startup_bundle(boundary.session_id)
        return {
            "result": to_primitive(result),
            "startup_bundle": startup_bundle,
        }


def _build_handler(service: CortexBridgeHttpService):
    class Handler(BaseHTTPRequestHandler):
        server_version = "CortexBridgePrep/0.1"

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path == "/healthz":
                self._send_json(HTTPStatus.OK, service.health_payload())
                return
            parts = [part for part in parsed.path.split("/") if part]
            if (
                len(parts) == 5
                and parts[0] == "v1"
                and parts[1] == "sessions"
                and parts[3] == "startup-bundle"
                and parts[4] == "latest"
            ):
                bundle = service.latest_startup_bundle(parts[2])
                if bundle is None:
                    self._send_json(HTTPStatus.NOT_FOUND, {"error": "startup_bundle_not_found"})
                    return
                self._send_json(HTTPStatus.OK, bundle)
                return
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

        def do_POST(self) -> None:  # noqa: N802
            payload = self._read_json()
            parsed = urlparse(self.path)
            if parsed.path == "/v1/openclaw/hooks":
                self._send_json(HTTPStatus.ACCEPTED, service.record_hook_event(payload))
                return
            if parsed.path == "/v1/openclaw/boundaries":
                mode = str(payload.pop("mode", "standard"))
                preferences = payload.pop("preference_overlays", None)
                if preferences is not None and not isinstance(preferences, dict):
                    self._send_json(HTTPStatus.BAD_REQUEST, {"error": "invalid_preference_overlays"})
                    return
                response = service.process_boundary(
                    payload,
                    mode=mode,
                    preference_overlays=preferences,
                )
                self._send_json(HTTPStatus.OK, response)
                return
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A003
            return

        def _read_json(self) -> dict[str, Any]:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(content_length) if content_length > 0 else b"{}"
            if not raw:
                return {}
            return json.loads(raw.decode("utf-8"))

        def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
            self.send_response(status.value)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return Handler


def run_http_service(
    *,
    host: str = "127.0.0.1",
    port: int = 8091,
    data_root: Path | None = None,
) -> None:
    settings = CortexSettings(data_root=data_root or Path(".runtime/cortex"))
    service = CortexBridgeHttpService(CortexPreparationRuntime(settings))
    httpd = create_http_server(service, host=host, port=port)
    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()


def create_http_server(
    service: CortexBridgeHttpService,
    *,
    host: str = "127.0.0.1",
    port: int = 8091,
) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), _build_handler(service))
