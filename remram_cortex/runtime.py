from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from .config import CortexSettings
from .models import (
    BoundaryInput,
    EvidencePointer,
    Phase1RunResult,
    RuntimeEvidenceRecord,
    dataclass_dict,
    to_primitive,
    utc_now,
)
from .policy import PolicyResolver, StartupBundleAssembler
from .semantic import SemanticProcessor


class FilesystemRuntimeEvidenceStore:
    def __init__(self, settings: CortexSettings) -> None:
        self._settings = settings

    def capture(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint_id: str,
        policy_bundle_id: str,
    ) -> tuple[RuntimeEvidenceRecord, Path]:
        session_root = self._settings.runtime_evidence_root / boundary.session_id
        session_root.mkdir(parents=True, exist_ok=True)
        output_path = session_root / f"{checkpoint_id}.json"
        payload = {
            "session_id": boundary.session_id,
            "conversation_id": boundary.conversation_id,
            "user_id": boundary.user_id,
            "trigger": boundary.trigger.value,
            "checkpoint_id": checkpoint_id,
            "checkpoint_label": boundary.checkpoint_label,
            "captured_at": utc_now().isoformat(),
            "policy_bundle_id": policy_bundle_id,
            "messages": [to_primitive(message) for message in boundary.messages],
        }
        body = json.dumps(payload, indent=2, sort_keys=True)
        sha = sha256(body.encode("utf-8")).hexdigest()
        output_path.write_text(body + "\n", encoding="utf-8")
        pointer = EvidencePointer(
            evidence_id=f"runtime-evidence-{sha[:12]}",
            evidence_class="runtime_evidence",
            uri=output_path.as_posix(),
            sha256=sha,
            captured_at=utc_now(),
        )
        record = RuntimeEvidenceRecord(
            pointer=pointer,
            session_id=boundary.session_id,
            conversation_id=boundary.conversation_id,
            user_id=boundary.user_id,
            trigger=boundary.trigger,
            checkpoint_id=checkpoint_id,
            policy_bundle_id=policy_bundle_id,
            checkpoint_label=boundary.checkpoint_label,
            captured_at=utc_now(),
            message_count=len(boundary.messages),
            messages=boundary.messages,
        )
        return record, output_path


class CortexPreparationRuntime:
    def __init__(
        self,
        settings: CortexSettings | None = None,
        *,
        policy_resolver: PolicyResolver | None = None,
        semantic_processor: SemanticProcessor | None = None,
    ) -> None:
        self.settings = settings or CortexSettings()
        self._policy_resolver = policy_resolver or PolicyResolver()
        self._semantic_processor = semantic_processor or SemanticProcessor()
        self._evidence_store = FilesystemRuntimeEvidenceStore(self.settings)
        self._startup_assembler = StartupBundleAssembler(self.settings)

    def run_boundary(
        self,
        boundary: BoundaryInput,
        *,
        mode: str = "standard",
        preference_overlays: dict[str, str] | None = None,
    ) -> Phase1RunResult:
        self.settings.ensure_layout()
        checkpoint_id = self._build_checkpoint_id(boundary)
        policy_bundle = self._policy_resolver.resolve(
            mode=mode,
            preference_overlays=preference_overlays,
        )
        evidence_record, evidence_path = self._evidence_store.capture(
            boundary=boundary,
            checkpoint_id=checkpoint_id,
            policy_bundle_id=policy_bundle.bundle_id,
        )
        (
            semantic_checkpoint,
            qmd_batch,
            support_bodies,
            graphiti_package,
            reflection_hook,
            dream_hook,
        ) = self._semantic_processor.process(
            boundary=boundary,
            checkpoint_id=checkpoint_id,
            evidence_pointer=evidence_record.pointer,
        )
        next_startup_bundle = self._startup_assembler.assemble(
            session_id=boundary.session_id,
            conversation_id=boundary.conversation_id,
            policy_bundle=policy_bundle,
            hot_continuity=[
                semantic_checkpoint.conversation_summary,
                *[candidate.statement for candidate in semantic_checkpoint.notion_candidates[:4]],
            ],
            durable_orientation=[claim.statement for claim in graphiti_package.claims[:4]],
            knowledge_pointers=[
                f"{body.support_body_id}:{body.body_type.value}"
                for body in support_bodies[:6]
            ],
        )
        semantic_path = self._write_json(
            self.settings.semantic_checkpoint_root / boundary.session_id / f"{checkpoint_id}.json",
            dataclass_dict(semantic_checkpoint),
        )
        qmd_path = self._write_json(
            self.settings.qmd_mutation_root / boundary.session_id / f"{checkpoint_id}.json",
            dataclass_dict(qmd_batch),
        )
        layer4_path = self._write_json(
            self.settings.layer4_outbox_root / boundary.session_id / f"{checkpoint_id}.json",
            {"support_bodies": [dataclass_dict(body) for body in support_bodies]},
        )
        layer3_path = self._write_json(
            self.settings.layer3_outbox_root / boundary.session_id / f"{checkpoint_id}.json",
            dataclass_dict(graphiti_package),
        )
        reflection_path = self._write_json(
            self.settings.reflection_hook_root / boundary.session_id / f"{checkpoint_id}.json",
            dataclass_dict(reflection_hook),
        )
        dream_path: Path | None = None
        if dream_hook is not None:
            dream_path = self._write_json(
                self.settings.dream_hook_root / boundary.session_id / f"{checkpoint_id}.json",
                dataclass_dict(dream_hook),
            )
        startup_path = self._write_json(
            self.settings.startup_bundle_root / boundary.session_id / f"{checkpoint_id}.json",
            dataclass_dict(next_startup_bundle),
        )
        return Phase1RunResult(
            checkpoint_id=checkpoint_id,
            evidence_path=evidence_path.as_posix(),
            semantic_checkpoint_path=semantic_path.as_posix(),
            qmd_mutation_path=qmd_path.as_posix(),
            layer4_outbox_path=layer4_path.as_posix(),
            layer3_outbox_path=layer3_path.as_posix(),
            reflection_hook_path=reflection_path.as_posix(),
            dream_hook_path=dream_path.as_posix() if dream_path else None,
            next_startup_bundle_path=startup_path.as_posix(),
        )

    def _write_json(self, path: Path, payload: dict) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _build_checkpoint_id(self, boundary: BoundaryInput) -> str:
        fingerprint = sha256(
            "|".join(message.content for message in boundary.messages).encode("utf-8")
        ).hexdigest()[:10]
        return f"{boundary.trigger.value}-{fingerprint}"
