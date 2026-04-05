create schema if not exists cortex;

do $$
begin
    if not exists (
        select 1
        from pg_type
        where typname = 'phase1_support_body_type'
    ) then
        create type cortex.phase1_support_body_type as enum (
            'conversation_summary',
            'segment_summary',
            'concept_support',
            'fact_candidate',
            'belief_candidate',
            'retrieval_record'
        );
    end if;
end
$$;

create table if not exists cortex.phase1_support_body (
    support_body_id text primary key,
    anchor_id text not null,
    session_id text not null,
    checkpoint_id text not null,
    body_type cortex.phase1_support_body_type not null,
    trust_state text not null default 'tentative',
    title text not null,
    summary text not null,
    retrieval_text text not null,
    source_evidence jsonb not null,
    tags jsonb not null default '[]'::jsonb,
    metadata jsonb not null default '{}'::jsonb,
    body jsonb not null,
    created_at timestamptz not null default now()
);

create index if not exists idx_phase1_support_body_session
    on cortex.phase1_support_body (session_id, checkpoint_id);

create index if not exists idx_phase1_support_body_anchor
    on cortex.phase1_support_body (anchor_id, body_type);

create index if not exists idx_phase1_support_body_retrieval_tsv
    on cortex.phase1_support_body
    using gin (to_tsvector('english', retrieval_text));

comment on table cortex.phase1_support_body is
    'Phase 1 Layer 4 chat-derived support bodies. This schema is the appliance-facing Postgres contract; the current repo scaffold only stages matching JSON payloads locally.';

comment on column cortex.phase1_support_body.source_evidence is
    'Layer 5 evidence pointers back to runtime evidence. Layer 4 remains operationally authoritative but does not own Layer 5 lifecycle.';

comment on column cortex.phase1_support_body.body is
    'Body-specific JSON payload for summaries, concept support, fact candidates, belief candidates, and retrieval records.';

comment on column cortex.phase1_support_body.metadata is
    'Operational metadata only. Embedding columns are intentionally deferred until the appliance embedding contract is pinned.';
