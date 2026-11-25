# Discovery status — 2026-11-25

Status: discovery blocked on external access; architecture and backlog not approved.

## Verified repository evidence

- Initial commit: `29875c621f35aae17285b823bd4c019e6471ffc9`.
- Tracked files: README.md and .gitignore only. No application, dependencies, build, tests, CI, or architecture documents.
- Remote advertises main at that same commit; local task branch is work.
- Initial working tree clean. Git HTTPS read access succeeds.
- No AGENTS.md found under /workspace.
- GitHub API request to repos/Mr-MarcelluS/ScamShield fails with Forbidden. Authentication variable presence was checked without reading its value. This does not establish missing credentials.
- Issues, labels, milestones, collaborators, rules, assignees and Projects remain uninspected. The reported 67 issues are user-provided context, not a verified count.

## Research access record

HTTPS retrieval was attempted for the following sources; each failed with proxy tunnel 403. No page contents were retrieved. These are research targets, not citations supporting product claims.

| Source | Intended question |
| --- | --- |
| https://www.cybercrime.gov.in/ | Current victim reporting routes, emergency guidance, evidence requirements |
| https://sancharsaathi.gov.in/sfc/ | Scope and current eligibility of suspicious communication reporting |
| https://www.rbi.org.in/ | Bank notification and customer protection guidance; avoid refund promises |
| https://www.truecaller.com/scam-alert | Current detection, response and privacy features |
| https://support.google.com/messages/answer/9327903 | Current Messages spam controls and processing model |
| https://developer.android.com/privacy-and-security | Android platform constraints and secure implementation guidance |

Additional research targets: CERT-In and MHA advisories, official PIB notices, Microsoft Defender and Norton offerings, Android/ML Kit documentation, OWASP MASVS. Verify each relevant page, publication date, scope and limitations before citing it. Do not treat absence of documented competitor features as proof those features do not exist.

## Product hypotheses to test

These are recommendations for investigation, not research findings:

1. A user-initiated Android share/paste workflow may cover more channels with fewer permissions than SMS interception or notification monitoring.
2. Exposure questions (clicked, disclosed credentials, installed software, paid) may determine useful next steps more reliably than a binary scam verdict.
3. Local explainable indicators, incident records and user-controlled evidence export may provide a useful first demonstration without a server or LLM.
4. OCR may improve screenshot handling but needs device, script, accuracy and download feasibility checks. Correctable OCR must not replace original evidence.
5. Reporting guidance should be curated, dated and source-linked. Reporting suspicious communications and reporting financial loss must remain distinct pathways.
6. No account or cloud sync may be preferable for the first release. Evaluate device loss, recovery, encrypted storage, deletion and export tradeoffs explicitly.

Do not publish official response instructions until independently verified. Never fetch a submitted suspicious URL, install submitted APKs, promise safety, or claim evidence authenticity merely because a hash matches.

## Discovery scenarios and unanswered questions

| Scenario | Required context | Product boundary to investigate |
| --- | --- | --- |
| Bank SMS or WhatsApp KYC | Claimed sender, requested action, exposure | Text cannot establish sender identity |
| Link clicked | Information entered, downloads, permissions | A click alone cannot establish compromise |
| OTP disclosed | Which account, timing, transaction status; never request the OTP itself | Exposure guidance must not depend on detection score |
| APK installed | Installation and permissions, affected device | No malware execution or claim of device remediation |
| Money transferred | Payment channel, time, available reference | Urgent official pathways; no recovery guarantee |
| Job/investment offer | Advance fees, identity requests, payment history | Indicators and uncertainty, not legal adjudication |

Interview a small consented convenience sample with synthetic scenarios; label findings nonrepresentative. Measure comprehension, completion time and unsafe interpretations. Do not collect real victim communications.

## Decision gates

1. Audit live issues, milestones, collaborators, Projects, settings and branches with pagination. Preserve an audit snapshot without private content in logs.
2. Verify official routes and competitor capabilities using accessible primary sources; separate official facts, vendor claims, observations and assumptions.
3. Compare native Kotlin/Compose against Flutter; local Room against cloud storage; deterministic analysis against classifiers and LLMs; bundled OCR against downloaded models. Consider team skills, device support, offline operation, privacy and cost.
4. Establish PRD/SRS and measurable acceptance criteria, then architecture, schemas, component contracts, threat model and release/test strategy. A local-only design needs typed internal contracts rather than an invented REST backend.
5. Build dependency-ordered issues from that architecture. Map every existing issue to keep/edit/merge/split/defer/supersede with explanation and successor references. Verify usernames and assignment eligibility before assigning.
6. Reconcile the existing board instead of creating a duplicate. Never delete issues in bulk. Use reviewed branches and PRs for source changes.

## Team planning constraints

User-supplied handles: Mr-MarcelluS, haneeshraj14-design, siriramya28. Account existence and repository access are not yet verified. Do not describe proposed ownership as actual GitHub assignment.

Assess availability and skills before final ownership. Candidate workstreams are Android experience/integration, domain analysis/evaluation, and incident persistence/privacy/response content. Each needs a primary owner and a different reviewer; rotate integration duty. No permanent backend role is needed unless the architecture actually requires a backend.

## Resume procedure

The environment configuration draft contains narrowly scoped research and api.github.com domain additions. The save succeeded; it does not activate networking or publish a snapshot. Review and save those changes in environment settings, then publish the environment.

After networking updates, retry the same read-only requests. Use existing platform authentication first. If GitHub returns an authorization error after connectivity is restored, diagnose repository/API scope separately; do not ask for raw tokens in chat.

Audit with gh api (paginate collection endpoints): repository metadata, branches, issues with all states, labels, milestones with all states, collaborators, and accessible rules. Use GraphQL for existing Projects and field options. Record inaccessible settings honestly. Export the existing issue mapping before any mutation. Verify every mutation by reading back the resulting object.

No application features, GitHub issues, assignments, milestones, or board changes have been made by this discovery pass.

## Public visibility update

The owner explicitly changed the repository to public and instructed that it remain public until they change it themselves. Do not change repository visibility.

Anonymous GitHub HTML access now succeeds. The issues page reports 67 open issues; the milestones page reports nine open milestones S0–S8, all at zero completion. The first issue page exposes #43–#67, including previously assumed backend, PostgreSQL, synchronization and deployment work. These choices require independent evaluation, not automatic adoption. Full issue bodies and pagination still require audit. The anonymous Projects page reports zero visible projects; this does not establish that no private board exists.

GitHub API and official research requests still fail with proxy 403. Public visibility solves anonymous repository viewing, not the environment's separate domain restrictions. No GitHub mutations were performed.
