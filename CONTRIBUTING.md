# Contributing

Use one branch per verifiable issue and a pull request to main. Main already requires one approval, approval after the last push, resolved review threads and squash merging; never bypass those rules. Existing source history stays intact.

Read [product requirements](docs/product.md), [contracts](docs/architecture/contracts.md), [ADRs](docs/architecture/design.md) and your [issue](docs/planning/backlog.md) before coding. Decision status is proposed until reviewed and merged. Implementation starts after #1; no broad feature work belongs in the foundation PR.

Run `python -m pip install -r requirements-dev.txt` then `python scripts/validate_foundation.py`. Android build/test commands will be added by #9/#15 after they work from a fresh checkout. Never commit local.properties, signing keys, tokens, victim messages or screenshots. Use reserved example domains and synthetic fixtures. Do not call real helplines or submit test complaints.

Change a cross-team contract by documenting the reason in an ADR, updating schema/examples, naming affected consumers and requesting a reviewer from their workstream. Preserve schema migrations and old assessment versions. Source docs and merged contracts override a development chat's assumptions.

A task is done when its acceptance/tests have evidence in a reviewed, merged PR, documentation matches actual behavior, security/privacy implications are reviewed and another teammate can reproduce the result. Superseded issues are not completed software. See the roadmap for ownership and review rotation.

Report a suspected vulnerability privately to a repository maintainer using GitHub's private reporting feature if enabled, or an agreed private team channel. Do not put exploit payloads containing personal data or credentials in public issues. No private-reporting feature is assumed enabled by this document.
