from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class CortexSettings:
    data_root: Path = Path(".runtime/cortex")
    hot_transcript_retention_days: int = 90
    max_hot_continuity_items: int = 6
    max_durable_orientation_items: int = 4
    max_knowledge_pointer_items: int = 6

    @property
    def runtime_evidence_root(self) -> Path:
        return self.data_root / "layer5" / "runtime_evidence"

    @property
    def semantic_checkpoint_root(self) -> Path:
        return self.data_root / "staging" / "semantic_checkpoints"

    @property
    def qmd_mutation_root(self) -> Path:
        return self.data_root / "staging" / "qmd_mutations"

    @property
    def layer4_outbox_root(self) -> Path:
        return self.data_root / "staging" / "layer4_support_bodies"

    @property
    def layer3_outbox_root(self) -> Path:
        return self.data_root / "outbox" / "layer3_graphiti"

    @property
    def reflection_hook_root(self) -> Path:
        return self.data_root / "hooks" / "reflection"

    @property
    def dream_hook_root(self) -> Path:
        return self.data_root / "hooks" / "dream"

    @property
    def startup_bundle_root(self) -> Path:
        return self.data_root / "staging" / "startup_bundles"

    @property
    def openclaw_hook_event_root(self) -> Path:
        return self.data_root / "ingest" / "openclaw_hook_events"

    def ensure_layout(self) -> None:
        for path in (
            self.runtime_evidence_root,
            self.semantic_checkpoint_root,
            self.qmd_mutation_root,
            self.layer4_outbox_root,
            self.layer3_outbox_root,
            self.reflection_hook_root,
            self.dream_hook_root,
            self.startup_bundle_root,
            self.openclaw_hook_event_root,
        ):
            path.mkdir(parents=True, exist_ok=True)
