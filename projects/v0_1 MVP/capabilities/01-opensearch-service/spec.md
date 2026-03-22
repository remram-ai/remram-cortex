# OpenSearch Service Capability Spec

## 1. Purpose

Provide the search and indexing service Cortex uses for knowledge retrieval, ranking inputs, and traceable query execution.

## 2. Capability Boundary

This capability is responsible for:

- bringing up an OpenSearch service usable by Cortex
- defining Cortex index mappings
- storing knowledge documents and retrieval metadata
- supporting hybrid lexical plus vector retrieval inputs

This capability is not responsible for:

- artifact persistence
- reflection decisions
- chat UX

## 3. MVP Requirements

- one usable OpenSearch service for local development
- index creation for Cortex knowledge documents
- mappings for governance fields, typed signals, canonical text, vectors, and ranking metadata
- support for bounded query execution used by retrieval
- enough logging or diagnostics to debug query behavior

## 4. Functional Requirements

- service can be started and reached from Cortex
- index mapping supports the current retrieval model
- documents can be inserted, updated, and queried
- retrieval traces can reference underlying score contributors

## 5. Deferred

- high-availability deployment
- multi-index optimization
- production-scale shard tuning
