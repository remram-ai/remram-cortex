from __future__ import annotations

from dataclasses import asdict, dataclass, field, fields, is_dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class BoundaryTrigger(str, Enum):
    TURN_END = "turn_end"
    SESSION_END = "session_end"
    CHECKPOINT = "checkpoint"


class SupportBodyType(str, Enum):
    CONVERSATION_SUMMARY = "conversation_summary"
    SEGMENT_SUMMARY = "segment_summary"
    CONCEPT_SUPPORT = "concept_support"
    FACT_CANDIDATE = "fact_candidate"
    BELIEF_CANDIDATE = "belief_candidate"
    RETRIEVAL_RECORD = "retrieval_record"


class TrustState(str, Enum):
    TENTATIVE = "tentative"
    LOW_CONFIDENCE = "low_confidence"
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    INVALIDATED = "invalidated"
    STALE_SUPPORT = "stale_support"


@dataclass(frozen=True, slots=True)
class ChatMessage:
    role: str
    content: str
    timestamp: str | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ChatMessage":
        return cls(
            role=str(payload["role"]),
            content=str(payload["content"]),
            timestamp=payload.get("timestamp"),
        )


@dataclass(frozen=True, slots=True)
class BoundaryInput:
    session_id: str
    conversation_id: str
    user_id: str
    trigger: BoundaryTrigger
    messages: list[ChatMessage]
    checkpoint_label: str | None = None
    recorded_at: datetime = field(default_factory=utc_now)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "BoundaryInput":
        raw_messages = payload.get("messages", [])
        trigger = BoundaryTrigger(payload["trigger"])
        return cls(
            session_id=str(payload["session_id"]),
            conversation_id=str(payload["conversation_id"]),
            user_id=str(payload["user_id"]),
            trigger=trigger,
            messages=[ChatMessage.from_dict(item) for item in raw_messages],
            checkpoint_label=payload.get("checkpoint_label"),
            recorded_at=_coerce_datetime(payload.get("recorded_at")) or utc_now(),
        )


@dataclass(frozen=True, slots=True)
class PolicyBundle:
    bundle_id: str
    mode: str
    role_definition: str
    approval_posture: str
    prompt_budget: dict[str, int]
    tool_rules: dict[str, list[str]]
    preference_policy: dict[str, str]


@dataclass(frozen=True, slots=True)
class ContextBlock:
    order: int
    layer: str
    kind: str
    payload: Any


@dataclass(frozen=True, slots=True)
class StartupBundle:
    bundle_id: str
    session_id: str
    conversation_id: str
    blocks: list[ContextBlock]
    generated_at: datetime


@dataclass(frozen=True, slots=True)
class EvidencePointer:
    evidence_id: str
    evidence_class: str
    uri: str
    sha256: str
    captured_at: datetime


@dataclass(frozen=True, slots=True)
class RuntimeEvidenceRecord:
    pointer: EvidencePointer
    session_id: str
    conversation_id: str
    user_id: str
    trigger: BoundaryTrigger
    checkpoint_id: str
    policy_bundle_id: str
    checkpoint_label: str | None
    captured_at: datetime
    message_count: int
    messages: list[ChatMessage]


@dataclass(frozen=True, slots=True)
class NotionCandidate:
    notion_id: str
    anchor_id: str
    kind: str
    statement: str
    confidence: float
    trust_state: TrustState
    cross_thread_eligible: bool
    evidence_refs: list[EvidencePointer]
    tags: list[str]


@dataclass(frozen=True, slots=True)
class QmdMutation:
    operation: str
    notion_id: str
    anchor_id: str
    query_text: str
    ttl_hours: int
    cross_thread_eligible: bool
    reason: str


@dataclass(frozen=True, slots=True)
class QmdMutationBatch:
    checkpoint_id: str
    session_id: str
    trigger: BoundaryTrigger
    mutations: list[QmdMutation]
    generated_at: datetime


@dataclass(frozen=True, slots=True)
class Layer4SupportBody:
    support_body_id: str
    body_type: SupportBodyType
    anchor_id: str
    session_id: str
    checkpoint_id: str
    title: str
    summary: str
    retrieval_text: str
    trust_state: TrustState
    evidence_refs: list[EvidencePointer]
    tags: list[str]
    metadata: dict[str, Any]
    body: dict[str, Any]


@dataclass(frozen=True, slots=True)
class Layer3Claim:
    claim_id: str
    anchor_id: str
    statement: str
    confidence: float
    trust_state: TrustState
    evidence_refs: list[EvidencePointer]
    support_body_ids: list[str]


@dataclass(frozen=True, slots=True)
class Layer3Relationship:
    relationship_id: str
    source_anchor_id: str
    relation: str
    target_anchor_id: str
    confidence: float
    trust_state: TrustState


@dataclass(frozen=True, slots=True)
class GraphitiEpisodePackage:
    episode_id: str
    session_id: str
    conversation_id: str
    checkpoint_id: str
    trigger: BoundaryTrigger
    summary: str
    evidence_refs: list[EvidencePointer]
    claims: list[Layer3Claim]
    relationships: list[Layer3Relationship]
    metadata: dict[str, Any]


@dataclass(frozen=True, slots=True)
class ReflectionHook:
    hook_id: str
    session_id: str
    checkpoint_id: str
    trigger: BoundaryTrigger
    qmd_cleanup_actions: list[str]
    promotion_candidates: list[str]
    layer4_updates: list[str]
    reason: str


@dataclass(frozen=True, slots=True)
class DreamHook:
    hook_id: str
    session_id: str
    checkpoint_id: str
    trigger: BoundaryTrigger
    consolidation_candidates: list[str]
    relationship_review: list[str]
    reason: str


@dataclass(frozen=True, slots=True)
class SemanticCheckpoint:
    checkpoint_id: str
    session_id: str
    conversation_id: str
    trigger: BoundaryTrigger
    generated_at: datetime
    conversation_summary: str
    segment_summaries: list[str]
    keywords: list[str]
    notion_candidates: list[NotionCandidate]


@dataclass(frozen=True, slots=True)
class Phase1RunResult:
    checkpoint_id: str
    evidence_path: str
    semantic_checkpoint_path: str
    qmd_mutation_path: str
    layer4_outbox_path: str
    layer3_outbox_path: str
    reflection_hook_path: str
    dream_hook_path: str | None
    next_startup_bundle_path: str


def _coerce_datetime(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def to_primitive(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Path):
        return value.as_posix()
    if is_dataclass(value):
        return {field.name: to_primitive(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, list):
        return [to_primitive(item) for item in value]
    if isinstance(value, tuple):
        return [to_primitive(item) for item in value]
    if isinstance(value, dict):
        return {str(key): to_primitive(item) for key, item in value.items()}
    return value


def dataclass_dict(value: Any) -> dict[str, Any]:
    if not is_dataclass(value):
        raise TypeError("value must be a dataclass instance")
    raw = asdict(value)
    return to_primitive(raw)
