from __future__ import annotations

import json
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

from remram_cortex import CortexPreparationRuntime, CortexSettings
from remram_cortex.models import BoundaryInput
from remram_cortex.policy import PolicyResolver, StartupBundleAssembler
from remram_cortex.service import CortexBridgeHttpService, create_http_server


SAMPLE_BOUNDARY = {
    "session_id": "session-001",
    "conversation_id": "conversation-layered-cortex",
    "user_id": "user-jason",
    "trigger": "session_end",
    "checkpoint_label": "prep-pass",
    "messages": [
        {
            "role": "system",
            "content": "You are operating inside the locked layered Cortex architecture.",
        },
        {
            "role": "user",
            "content": "My name is Jason and I am working on the layered Cortex MVP.",
        },
        {
            "role": "user",
            "content": "I prefer inspectable staging surfaces over hidden automation.",
        },
        {
            "role": "user",
            "content": "The implementation should target Moltbox later and we need a preparation-only pass first.",
        },
    ],
}


class PreparationRuntimeTests(unittest.TestCase):
    def test_startup_bundle_order_is_layered_and_bounded(self) -> None:
        settings = CortexSettings(data_root=Path(".runtime/test-startup"))
        policy = PolicyResolver().resolve(mode="standard", preference_overlays={"tone": "direct"})
        bundle = StartupBundleAssembler(settings).assemble(
            session_id="session-001",
            conversation_id="conversation-001",
            policy_bundle=policy,
            hot_continuity=["one", "two", "three", "four", "five", "six", "seven"],
            durable_orientation=["a", "b", "c", "d", "e"],
            knowledge_pointers=["k1", "k2", "k3", "k4", "k5", "k6", "k7"],
        )

        self.assertEqual(
            [block.kind for block in bundle.blocks],
            ["policy", "hot_continuity", "durable_orientation", "knowledge_pointers"],
        )
        self.assertEqual(len(bundle.blocks[1].payload), settings.max_hot_continuity_items)
        self.assertEqual(len(bundle.blocks[2].payload), settings.max_durable_orientation_items)
        self.assertEqual(len(bundle.blocks[3].payload), settings.max_knowledge_pointer_items)

    def test_run_boundary_writes_inspectable_phase1_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime = CortexPreparationRuntime(CortexSettings(data_root=Path(tmpdir)))
            result = runtime.run_boundary(BoundaryInput.from_dict(SAMPLE_BOUNDARY))

            output_paths = [
                result.evidence_path,
                result.semantic_checkpoint_path,
                result.qmd_mutation_path,
                result.layer4_outbox_path,
                result.layer3_outbox_path,
                result.reflection_hook_path,
                result.dream_hook_path,
                result.next_startup_bundle_path,
            ]
            for output_path in output_paths:
                self.assertIsNotNone(output_path)
                self.assertTrue(Path(output_path).exists(), output_path)

            support_payload = json.loads(Path(result.layer4_outbox_path).read_text(encoding="utf-8"))
            support_bodies = support_payload["support_bodies"]
            self.assertGreaterEqual(len(support_bodies), 4)
            self.assertEqual(
                support_bodies[0]["evidence_refs"][0]["uri"],
                result.evidence_path,
            )

    def test_layer3_package_stays_pointer_based(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime = CortexPreparationRuntime(CortexSettings(data_root=Path(tmpdir)))
            result = runtime.run_boundary(BoundaryInput.from_dict(SAMPLE_BOUNDARY))

            graphiti_payload = json.loads(Path(result.layer3_outbox_path).read_text(encoding="utf-8"))
            self.assertIn("claims", graphiti_payload)
            self.assertIn("relationships", graphiti_payload)
            self.assertNotIn("messages", graphiti_payload)
            self.assertFalse(graphiti_payload["metadata"]["raw_transcript_included"])
            self.assertGreaterEqual(len(graphiti_payload["claims"]), 1)


class BridgeServiceTests(unittest.TestCase):
    def _request_json(
        self,
        base_url: str,
        path: str,
        *,
        method: str = "GET",
        payload: dict | None = None,
    ) -> tuple[int, dict]:
        data = None
        headers = {}
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(
            f"{base_url}{path}",
            data=data,
            headers=headers,
            method=method,
        )
        try:
            with urllib.request.urlopen(request) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read().decode("utf-8"))

    def test_http_service_health_bundle_and_hook_capture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime = CortexPreparationRuntime(CortexSettings(data_root=Path(tmpdir)))
            runtime.run_boundary(BoundaryInput.from_dict(SAMPLE_BOUNDARY))

            service = CortexBridgeHttpService(runtime)
            server = create_http_server(service, host="127.0.0.1", port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                host, port = server.server_address
                base_url = f"http://{host}:{port}"

                status, payload = self._request_json(base_url, "/healthz")
                self.assertEqual(status, 200)
                self.assertEqual(payload["status"], "ok")

                status, bundle_payload = self._request_json(
                    base_url,
                    "/v1/sessions/session-001/startup-bundle/latest",
                )
                self.assertEqual(status, 200)
                self.assertIn("bundle_id", bundle_payload)

                status, hook_payload = self._request_json(
                    base_url,
                    "/v1/openclaw/hooks",
                    method="POST",
                    payload={
                        "event": "agent_end",
                        "session_id": "session-001",
                        "trigger": "reply",
                        "payload": {"duration_ms": 12},
                    },
                )
                self.assertEqual(status, 202)
                self.assertEqual(hook_payload["status"], "accepted")
                self.assertTrue(Path(hook_payload["stored_at"]).exists())
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)

    def test_http_service_processes_boundary_requests(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime = CortexPreparationRuntime(CortexSettings(data_root=Path(tmpdir)))
            service = CortexBridgeHttpService(runtime)
            server = create_http_server(service, host="127.0.0.1", port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                host, port = server.server_address
                base_url = f"http://{host}:{port}"

                status, payload = self._request_json(
                    base_url,
                    "/v1/openclaw/boundaries",
                    method="POST",
                    payload={
                        **SAMPLE_BOUNDARY,
                        "mode": "standard",
                        "preference_overlays": {"tone": "direct"},
                    },
                )
                self.assertEqual(status, 200)
                self.assertIn("result", payload)
                self.assertIn("startup_bundle", payload)
                self.assertTrue(Path(payload["result"]["semantic_checkpoint_path"]).exists())

                status, error_payload = self._request_json(
                    base_url,
                    "/v1/openclaw/boundaries",
                    method="POST",
                    payload={
                        **SAMPLE_BOUNDARY,
                        "preference_overlays": ["bad"],
                    },
                )
                self.assertEqual(status, 400)
                self.assertEqual(error_payload["error"], "invalid_preference_overlays")
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
