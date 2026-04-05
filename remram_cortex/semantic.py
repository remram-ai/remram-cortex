from __future__ import annotations

import re
from collections import Counter
from hashlib import sha256

from .models import (
    BoundaryInput,
    BoundaryTrigger,
    DreamHook,
    EvidencePointer,
    GraphitiEpisodePackage,
    Layer3Claim,
    Layer3Relationship,
    Layer4SupportBody,
    NotionCandidate,
    QmdMutation,
    QmdMutationBatch,
    ReflectionHook,
    SemanticCheckpoint,
    SupportBodyType,
    TrustState,
    utc_now,
)

STOPWORDS = {
    "about",
    "after",
    "again",
    "also",
    "because",
    "been",
    "before",
    "being",
    "between",
    "could",
    "every",
    "first",
    "from",
    "have",
    "layer",
    "layers",
    "local",
    "memory",
    "other",
    "phase",
    "should",
    "that",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "this",
    "want",
    "with",
    "would",
    "your",
}

IDENTITY_PATTERNS = [
    (re.compile(r"\bmy name is ([A-Za-z][A-Za-z' -]+)", re.IGNORECASE), "identity", "user_name"),
    (re.compile(r"\bcall me ([A-Za-z][A-Za-z' -]+)", re.IGNORECASE), "identity", "preferred_name"),
]

PREFERENCE_PATTERNS = [
    re.compile(r"\bi prefer ([^.?!]+)", re.IGNORECASE),
    re.compile(r"\bplease ([^.?!]+)", re.IGNORECASE),
]

PROJECT_PATTERNS = [
    re.compile(r"\bi(?:'m| am) working on ([^.?!]+)", re.IGNORECASE),
    re.compile(r"\bwe(?:'re| are) building ([^.?!]+)", re.IGNORECASE),
]

BELIEF_PATTERN = re.compile(r"\b(should|must|need to|important)\b", re.IGNORECASE)


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _snippet(value: str, words: int = 14) -> str:
    parts = value.split()
    if len(parts) <= words:
        return value.strip()
    return " ".join(parts[:words]).strip() + "..."


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return ordered


class SemanticProcessor:
    def process(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint_id: str,
        evidence_pointer: EvidencePointer,
    ) -> tuple[
        SemanticCheckpoint,
        QmdMutationBatch,
        list[Layer4SupportBody],
        GraphitiEpisodePackage,
        ReflectionHook,
        DreamHook | None,
    ]:
        user_messages = [message for message in boundary.messages if message.role == "user"]
        conversation_text = " ".join(message.content for message in user_messages)
        keywords = self._extract_keywords(conversation_text)
        conversation_summary = self._build_conversation_summary(boundary, keywords)
        notion_candidates = self._extract_notion_candidates(
            user_messages=user_messages,
            keywords=keywords,
            checkpoint_id=checkpoint_id,
            evidence_pointer=evidence_pointer,
        )
        segment_summaries = [
            f"Segment {index + 1}: {_snippet(message.content)}"
            for index, message in enumerate(user_messages)
        ]
        semantic_checkpoint = SemanticCheckpoint(
            checkpoint_id=checkpoint_id,
            session_id=boundary.session_id,
            conversation_id=boundary.conversation_id,
            trigger=boundary.trigger,
            generated_at=utc_now(),
            conversation_summary=conversation_summary,
            segment_summaries=segment_summaries,
            keywords=keywords,
            notion_candidates=notion_candidates,
        )
        qmd_batch = self._build_qmd_batch(
            boundary=boundary,
            checkpoint_id=checkpoint_id,
            notion_candidates=notion_candidates,
        )
        support_bodies = self._build_layer4_support_bodies(
            boundary=boundary,
            checkpoint=semantic_checkpoint,
            evidence_pointer=evidence_pointer,
            keywords=keywords,
        )
        graphiti_package = self._build_graphiti_package(
            boundary=boundary,
            checkpoint=semantic_checkpoint,
            support_bodies=support_bodies,
            evidence_pointer=evidence_pointer,
        )
        reflection_hook = self._build_reflection_hook(
            boundary=boundary,
            checkpoint=semantic_checkpoint,
            support_bodies=support_bodies,
        )
        dream_hook = self._build_dream_hook(
            boundary=boundary,
            checkpoint=semantic_checkpoint,
            support_bodies=support_bodies,
        )
        return (
            semantic_checkpoint,
            qmd_batch,
            support_bodies,
            graphiti_package,
            reflection_hook,
            dream_hook,
        )

    def _extract_keywords(self, conversation_text: str) -> list[str]:
        tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", conversation_text.lower())
        filtered = [token for token in tokens if token not in STOPWORDS]
        counts = Counter(filtered)
        return [token for token, _ in counts.most_common(5)]

    def _build_conversation_summary(self, boundary: BoundaryInput, keywords: list[str]) -> str:
        last_user_message = next(
            (message.content for message in reversed(boundary.messages) if message.role == "user"),
            "",
        )
        topic_text = ", ".join(keywords[:3]) if keywords else "current work"
        return (
            f"Conversation centered on {topic_text}. "
            f"Latest user signal: {_snippet(last_user_message)}"
        )

    def _extract_notion_candidates(
        self,
        *,
        user_messages: list,
        keywords: list[str],
        checkpoint_id: str,
        evidence_pointer: EvidencePointer,
    ) -> list[NotionCandidate]:
        candidates: list[NotionCandidate] = []
        for message in user_messages:
            content = message.content.strip()
            for pattern, notion_kind, tag in IDENTITY_PATTERNS:
                match = pattern.search(content)
                if not match:
                    continue
                captured = match.group(1).strip()
                candidates.append(
                    self._notion_candidate(
                        checkpoint_id=checkpoint_id,
                        anchor_id=f"{notion_kind}:{_slug(tag)}",
                        kind=notion_kind,
                        statement=f"{tag.replace('_', ' ')}: {captured}",
                        confidence=0.92,
                        evidence_pointer=evidence_pointer,
                        tags=[tag],
                    )
                )
            for pattern in PREFERENCE_PATTERNS:
                match = pattern.search(content)
                if match:
                    captured = match.group(1).strip()
                    candidates.append(
                        self._notion_candidate(
                            checkpoint_id=checkpoint_id,
                            anchor_id=f"preference:{_slug(captured)}",
                            kind="preference",
                            statement=f"user preference: {captured}",
                            confidence=0.78,
                            evidence_pointer=evidence_pointer,
                            tags=["preference"],
                        )
                    )
            for pattern in PROJECT_PATTERNS:
                match = pattern.search(content)
                if match:
                    captured = match.group(1).strip()
                    candidates.append(
                        self._notion_candidate(
                            checkpoint_id=checkpoint_id,
                            anchor_id=f"project:{_slug(captured)}",
                            kind="project",
                            statement=f"active project: {captured}",
                            confidence=0.81,
                            evidence_pointer=evidence_pointer,
                            tags=["workspace"],
                        )
                    )
            if BELIEF_PATTERN.search(content):
                candidates.append(
                    self._notion_candidate(
                        checkpoint_id=checkpoint_id,
                        anchor_id=f"belief:{_slug(_snippet(content, 8))}",
                        kind="belief",
                        statement=_snippet(content, 18),
                        confidence=0.64,
                        evidence_pointer=evidence_pointer,
                        tags=["belief"],
                    )
                )
        for keyword in keywords[:3]:
            candidates.append(
                self._notion_candidate(
                    checkpoint_id=checkpoint_id,
                    anchor_id=f"concept:{keyword}",
                    kind="concept",
                    statement=f"conversation repeatedly referenced concept '{keyword}'",
                    confidence=0.58,
                    evidence_pointer=evidence_pointer,
                    tags=["concept"],
                )
            )
        unique_candidates: list[NotionCandidate] = []
        seen_keys: set[str] = set()
        for candidate in candidates:
            key = f"{candidate.anchor_id}|{candidate.statement}"
            if key in seen_keys:
                continue
            unique_candidates.append(candidate)
            seen_keys.add(key)
        return unique_candidates

    def _notion_candidate(
        self,
        *,
        checkpoint_id: str,
        anchor_id: str,
        kind: str,
        statement: str,
        confidence: float,
        evidence_pointer: EvidencePointer,
        tags: list[str],
    ) -> NotionCandidate:
        trust_state = TrustState.TENTATIVE if confidence >= 0.7 else TrustState.LOW_CONFIDENCE
        notion_hash = sha256(
            f"{checkpoint_id}|{anchor_id}|{statement}".encode("utf-8")
        ).hexdigest()[:12]
        return NotionCandidate(
            notion_id=f"notion-{notion_hash}",
            anchor_id=anchor_id,
            kind=kind,
            statement=statement,
            confidence=confidence,
            trust_state=trust_state,
            cross_thread_eligible=confidence >= 0.7,
            evidence_refs=[evidence_pointer],
            tags=tags,
        )

    def _build_qmd_batch(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint_id: str,
        notion_candidates: list[NotionCandidate],
    ) -> QmdMutationBatch:
        mutations = [
            QmdMutation(
                operation="upsert_tentative_notion",
                notion_id=candidate.notion_id,
                anchor_id=candidate.anchor_id,
                query_text=candidate.statement,
                ttl_hours=168,
                cross_thread_eligible=candidate.cross_thread_eligible,
                reason="boundary-triggered semantic checkpoint",
            )
            for candidate in notion_candidates
        ]
        return QmdMutationBatch(
            checkpoint_id=checkpoint_id,
            session_id=boundary.session_id,
            trigger=boundary.trigger,
            mutations=mutations,
            generated_at=utc_now(),
        )

    def _build_layer4_support_bodies(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint: SemanticCheckpoint,
        evidence_pointer: EvidencePointer,
        keywords: list[str],
    ) -> list[Layer4SupportBody]:
        support_bodies: list[Layer4SupportBody] = []
        support_bodies.append(
            Layer4SupportBody(
                support_body_id=f"l4-{checkpoint.checkpoint_id}-conversation",
                body_type=SupportBodyType.CONVERSATION_SUMMARY,
                anchor_id=f"conversation:{boundary.conversation_id}",
                session_id=boundary.session_id,
                checkpoint_id=checkpoint.checkpoint_id,
                title="Conversation Summary",
                summary=checkpoint.conversation_summary,
                retrieval_text=checkpoint.conversation_summary,
                trust_state=TrustState.TENTATIVE,
                evidence_refs=[evidence_pointer],
                tags=["conversation", *keywords[:3]],
                metadata={"trigger": boundary.trigger.value},
                body={"segments": checkpoint.segment_summaries},
            )
        )
        for index, segment in enumerate(checkpoint.segment_summaries):
            support_bodies.append(
                Layer4SupportBody(
                    support_body_id=f"l4-{checkpoint.checkpoint_id}-segment-{index + 1}",
                    body_type=SupportBodyType.SEGMENT_SUMMARY,
                    anchor_id=f"conversation:{boundary.conversation_id}",
                    session_id=boundary.session_id,
                    checkpoint_id=checkpoint.checkpoint_id,
                    title=f"Segment {index + 1}",
                    summary=segment,
                    retrieval_text=segment,
                    trust_state=TrustState.TENTATIVE,
                    evidence_refs=[evidence_pointer],
                    tags=["segment"],
                    metadata={"segment_number": index + 1},
                    body={"segment_summary": segment},
                )
            )
        for candidate in checkpoint.notion_candidates:
            body_type = SupportBodyType.BELIEF_CANDIDATE
            if candidate.kind in {"identity", "preference", "project"}:
                body_type = SupportBodyType.FACT_CANDIDATE
            if candidate.kind == "concept":
                body_type = SupportBodyType.CONCEPT_SUPPORT
            support_bodies.append(
                Layer4SupportBody(
                    support_body_id=f"l4-{candidate.notion_id}",
                    body_type=body_type,
                    anchor_id=candidate.anchor_id,
                    session_id=boundary.session_id,
                    checkpoint_id=checkpoint.checkpoint_id,
                    title=candidate.anchor_id,
                    summary=candidate.statement,
                    retrieval_text=candidate.statement,
                    trust_state=candidate.trust_state,
                    evidence_refs=[evidence_pointer],
                    tags=candidate.tags,
                    metadata={"confidence": candidate.confidence},
                    body={
                        "statement": candidate.statement,
                        "cross_thread_eligible": candidate.cross_thread_eligible,
                    },
                )
            )
        retrieval_text = " ".join(
            _dedupe_preserve_order(
                [checkpoint.conversation_summary, *keywords, *checkpoint.segment_summaries[:2]]
            )
        )
        support_bodies.append(
            Layer4SupportBody(
                support_body_id=f"l4-{checkpoint.checkpoint_id}-retrieval",
                body_type=SupportBodyType.RETRIEVAL_RECORD,
                anchor_id=f"conversation:{boundary.conversation_id}",
                session_id=boundary.session_id,
                checkpoint_id=checkpoint.checkpoint_id,
                title="Retrieval Record",
                summary="Lexical retrieval record for the checkpoint",
                retrieval_text=retrieval_text,
                trust_state=TrustState.TENTATIVE,
                evidence_refs=[evidence_pointer],
                tags=["retrieval", *keywords[:3]],
                metadata={"keyword_count": len(keywords)},
                body={"keywords": keywords, "summary": checkpoint.conversation_summary},
            )
        )
        return support_bodies

    def _build_graphiti_package(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint: SemanticCheckpoint,
        support_bodies: list[Layer4SupportBody],
        evidence_pointer: EvidencePointer,
    ) -> GraphitiEpisodePackage:
        support_by_anchor: dict[str, list[Layer4SupportBody]] = {}
        for support_body in support_bodies:
            support_by_anchor.setdefault(support_body.anchor_id, []).append(support_body)
        claims: list[Layer3Claim] = []
        relationships: list[Layer3Relationship] = []
        for candidate in checkpoint.notion_candidates:
            if candidate.confidence < 0.58:
                continue
            supporting_ids = [
                body.support_body_id for body in support_by_anchor.get(candidate.anchor_id, [])
            ]
            claims.append(
                Layer3Claim(
                    claim_id=f"claim-{candidate.notion_id}",
                    anchor_id=candidate.anchor_id,
                    statement=candidate.statement,
                    confidence=candidate.confidence,
                    trust_state=candidate.trust_state,
                    evidence_refs=[evidence_pointer],
                    support_body_ids=supporting_ids,
                )
            )
        concept_anchors = sorted(
            {candidate.anchor_id for candidate in checkpoint.notion_candidates if candidate.kind == "concept"}
        )
        for source, target in zip(concept_anchors, concept_anchors[1:]):
            relationship_hash = sha256(
                f"{source}|related_to|{target}".encode("utf-8")
            ).hexdigest()[:12]
            relationships.append(
                Layer3Relationship(
                    relationship_id=f"rel-{relationship_hash}",
                    source_anchor_id=source,
                    relation="related_to",
                    target_anchor_id=target,
                    confidence=0.55,
                    trust_state=TrustState.TENTATIVE,
                )
            )
        return GraphitiEpisodePackage(
            episode_id=f"episode-{checkpoint.checkpoint_id}",
            session_id=boundary.session_id,
            conversation_id=boundary.conversation_id,
            checkpoint_id=checkpoint.checkpoint_id,
            trigger=boundary.trigger,
            summary=checkpoint.conversation_summary,
            evidence_refs=[evidence_pointer],
            claims=claims,
            relationships=relationships,
            metadata={
                "message_count": len(boundary.messages),
                "support_body_count": len(support_bodies),
                "raw_transcript_included": False,
            },
        )

    def _build_reflection_hook(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint: SemanticCheckpoint,
        support_bodies: list[Layer4SupportBody],
    ) -> ReflectionHook:
        low_confidence = [
            candidate.notion_id for candidate in checkpoint.notion_candidates if candidate.confidence < 0.7
        ]
        anchor_counts = Counter(candidate.anchor_id for candidate in checkpoint.notion_candidates)
        duplicate_anchors = [anchor for anchor, count in anchor_counts.items() if count > 1]
        cleanup_actions = [f"expire_low_confidence:{notion_id}" for notion_id in low_confidence]
        cleanup_actions.extend(f"merge_duplicate_anchor:{anchor}" for anchor in duplicate_anchors)
        promotion_candidates = [
            candidate.anchor_id for candidate in checkpoint.notion_candidates if candidate.cross_thread_eligible
        ]
        layer4_updates = [body.support_body_id for body in support_bodies[:5]]
        return ReflectionHook(
            hook_id=f"reflection-{checkpoint.checkpoint_id}",
            session_id=boundary.session_id,
            checkpoint_id=checkpoint.checkpoint_id,
            trigger=boundary.trigger,
            qmd_cleanup_actions=cleanup_actions,
            promotion_candidates=promotion_candidates,
            layer4_updates=layer4_updates,
            reason="Keep Layer 2 lean and stage durable-memory promotion candidates.",
        )

    def _build_dream_hook(
        self,
        *,
        boundary: BoundaryInput,
        checkpoint: SemanticCheckpoint,
        support_bodies: list[Layer4SupportBody],
    ) -> DreamHook | None:
        if boundary.trigger == BoundaryTrigger.TURN_END:
            return None
        consolidation_candidates = [
            candidate.anchor_id for candidate in checkpoint.notion_candidates if candidate.confidence >= 0.75
        ]
        relationship_review = [
            body.anchor_id for body in support_bodies if body.body_type == SupportBodyType.CONCEPT_SUPPORT
        ]
        return DreamHook(
            hook_id=f"dream-{checkpoint.checkpoint_id}",
            session_id=boundary.session_id,
            checkpoint_id=checkpoint.checkpoint_id,
            trigger=boundary.trigger,
            consolidation_candidates=consolidation_candidates,
            relationship_review=relationship_review,
            reason="Slower consolidation over chat-derived evidence for Layer 3 and Layer 4 alignment.",
        )
