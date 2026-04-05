from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import CortexSettings
from .models import BoundaryInput, to_primitive
from .runtime import CortexPreparationRuntime
from .service import run_http_service


def _parse_preferences(values: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise SystemExit(f"invalid preference override: {item!r}")
        key, value = item.split("=", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="remram-cortex",
        description="Preparation scaffold for the layered Cortex Phase 0 and Phase 1 loop.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_boundary = subparsers.add_parser(
        "run-boundary",
        help="Capture runtime evidence and produce prep-only Phase 1 staging artifacts.",
    )
    run_boundary.add_argument("--input", required=True, help="Path to a boundary input JSON file.")
    run_boundary.add_argument(
        "--data-root",
        default=".runtime/cortex",
        help="Root directory for inspectable output artifacts.",
    )
    run_boundary.add_argument(
        "--mode",
        default="standard",
        help="Policy mode for the generated Cortex policy bundle.",
    )
    run_boundary.add_argument(
        "--preference",
        action="append",
        default=[],
        help="Preference overlay in key=value form. Can be repeated.",
    )

    serve = subparsers.add_parser(
        "serve",
        help="Run the local Cortex bridge HTTP service for prep and appliance contract testing.",
    )
    serve.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host interface for the local HTTP service.",
    )
    serve.add_argument(
        "--port",
        type=int,
        default=8091,
        help="TCP port for the local HTTP service.",
    )
    serve.add_argument(
        "--data-root",
        default=".runtime/cortex",
        help="Root directory for inspectable output artifacts.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "run-boundary":
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        boundary = BoundaryInput.from_dict(payload)
        runtime = CortexPreparationRuntime(CortexSettings(data_root=Path(args.data_root)))
        result = runtime.run_boundary(
            boundary,
            mode=args.mode,
            preference_overlays=_parse_preferences(args.preference),
        )
        print(json.dumps(to_primitive(result), indent=2, sort_keys=True))
        return 0
    if args.command == "serve":
        run_http_service(
            host=args.host,
            port=args.port,
            data_root=Path(args.data_root),
        )
        return 0
    parser.error(f"unknown command: {args.command}")
    return 2
