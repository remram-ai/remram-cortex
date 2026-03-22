# Git Service Dependency

Git Service is a service-shaped dependency that provides the local Git substrate used by the Cortex Git provider.

Unlike OpenSearch, this dependency does not yet have a promoted canonical platform item in `remram/platform/`, so its local spec and regression plan remain here for now.

## Local Documents

- [spec.md](spec.md)
- [regression-plan.md](regression-plan.md)

## Intended Direction

If this service becomes a shared platform surface rather than a Cortex-local dependency, its canonical documentation should move into `remram/platform/services/` and this folder should become a pointer or thin overlay.
