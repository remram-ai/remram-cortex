from __future__ import annotations

from hashlib import sha256

from .config import CortexSettings
from .models import ContextBlock, PolicyBundle, StartupBundle, utc_now


class PolicyResolver:
    def resolve(
        self,
        *,
        mode: str = "standard",
        preference_overlays: dict[str, str] | None = None,
    ) -> PolicyBundle:
        overlays = preference_overlays or {}
        role_definition = (
            "Cortex policy overlay for OpenClaw. "
            "Keep OpenClaw session mechanics native, keep runtime evidence inspectable, "
            "and prefer bounded context assembly over transcript replay."
        )
        approval_posture = "confirm_destructive_or_externalized_actions"
        prompt_budget = {
            "policy_tokens": 500,
            "hot_continuity_tokens": 800,
            "durable_orientation_tokens": 500,
            "knowledge_pointer_tokens": 350,
        }
        tool_rules = {
            "allow_without_extra_approval": ["read", "search", "inspect"],
            "require_explicit_approval": ["write", "network_admin", "shell_destructive"],
            "defer_to_openclaw_runtime": ["sandbox", "session_reset", "plugin_install"],
        }
        bundle_hash = sha256(
            f"{mode}|{approval_posture}|{sorted(overlays.items())}".encode("utf-8")
        ).hexdigest()[:12]
        return PolicyBundle(
            bundle_id=f"policy-{bundle_hash}",
            mode=mode,
            role_definition=role_definition,
            approval_posture=approval_posture,
            prompt_budget=prompt_budget,
            tool_rules=tool_rules,
            preference_policy=overlays,
        )


class StartupBundleAssembler:
    def __init__(self, settings: CortexSettings) -> None:
        self._settings = settings

    def assemble(
        self,
        *,
        session_id: str,
        conversation_id: str,
        policy_bundle: PolicyBundle,
        hot_continuity: list[str],
        durable_orientation: list[str],
        knowledge_pointers: list[str],
    ) -> StartupBundle:
        bundle_hash = sha256(
            "|".join(
                [
                    session_id,
                    conversation_id,
                    policy_bundle.bundle_id,
                    *hot_continuity,
                    *durable_orientation,
                    *knowledge_pointers,
                ]
            ).encode("utf-8")
        ).hexdigest()[:12]
        blocks = [
            ContextBlock(order=1, layer="layer1", kind="policy", payload=policy_bundle),
            ContextBlock(
                order=2,
                layer="layer2",
                kind="hot_continuity",
                payload=hot_continuity[: self._settings.max_hot_continuity_items],
            ),
            ContextBlock(
                order=3,
                layer="layer3",
                kind="durable_orientation",
                payload=durable_orientation[: self._settings.max_durable_orientation_items],
            ),
            ContextBlock(
                order=4,
                layer="layer4",
                kind="knowledge_pointers",
                payload=knowledge_pointers[: self._settings.max_knowledge_pointer_items],
            ),
        ]
        return StartupBundle(
            bundle_id=f"startup-{bundle_hash}",
            session_id=session_id,
            conversation_id=conversation_id,
            blocks=blocks,
            generated_at=utc_now(),
        )
