# Test Plan

## Core Scenarios

1. Semantic checkpoints are emitted from session evidence.
2. Checkpoints remain source-linked to the backing evidence package.
3. The same checkpoint stream supports optimistic and boundary-based consumption.
4. Context assembly can use checkpoints to stay bounded on smaller-window models.

## Failure Checks

- checkpoint payloads should not lose source identity
- optimistic production should not create a second memory authority
- consumer replay should be idempotent or watermark-safe

## Evidence Of Completion

- at least one replay from evidence package to checkpoint stream
- one demonstration of bounded assembly using checkpoints instead of transcript replay
