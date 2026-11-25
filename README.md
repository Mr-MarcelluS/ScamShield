# ScamShield

An independent student project for India: **share → understand → preserve → respond**.

The planned Android app helps people review suspicious text or screenshots, understand warning signs, preserve an incident locally, and find appropriate next steps. It cannot establish that content is safe, diagnose a compromised device, or guarantee recovery of money.

**Status:** product and architecture foundation; no application build exists yet. The implementation backlog is being reconciled against this design. Decisions become the team's accepted baseline when this documentation PR is reviewed and merged. Do not treat closed superseded issues as implemented features.

The repository is currently public. Use synthetic examples only. This project is not affiliated with the Indian government or Singapore's existing ScamShield service. Resolve the product-name collision before public distribution.

## Start here

- [Product requirements and SRS](docs/product.md)
- [Research, competitors, and official sources](docs/research.md)
- [Architecture and technology decisions](docs/architecture/design.md)
- [Database and component contracts](docs/architecture/contracts.md)
- [Security, privacy, and threat model](docs/security.md)
- [Testing and deployment](docs/testing-release.md)
- [Roadmap and team handoff](docs/planning/roadmap.md)
- [Issue-by-issue reconciliation](docs/planning/backlog.md)
- [Repository audit and execution record](docs/discovery-status.md)
- [Contributing](CONTRIBUTING.md)

## Recommended MVP

Native Kotlin/Compose Android app; deterministic local analysis; Room metadata and encrypted sensitive payloads; bundled Latin OCR with user correction; exposure questionnaire; incident timeline; explicit evidence export; dated official guidance. No login, cloud storage, automatic inbox access, suspicious-link fetching, or LLM is required.

The first demonstration is an offline text review followed by exposure questions, a saved incident, and response guidance. Screenshot ingestion and export follow that vertical slice.

## Development setup

For the foundation checks, install Python 3.11+ and run `python -m pip install -r requirements-dev.txt` then `python scripts/validate_foundation.py` from the repository root. These validate planning artifacts, not application behavior.

Android bootstrap is tracked in #9. It must pin Android Studio/JDK/Gradle/AGP/Kotlin versions together, check in the Gradle wrapper and dependency verification, and document build commands. No Android build command is advertised as working before that issue is complete. No `.env` or backend credentials are needed for the local MVP.
