# Backlog and reconciliation

Prepared from all 67 original issues. Original descriptions, labels, milestones and assignments are preserved in [original-backlog.json](original-backlog.json). Reused numbers retain history. Superseded/deferred issues close as not planned with explanation and successor/decision reference; none is deleted or falsely marked implemented. [backlog.json](backlog.json) is the structured plan.

## Active deliverables

| Issue | Deliverable | Owner | Milestone | Days | Dependencies |
| --- | --- | --- | --- | --- | --- |
| #1 | Review and accept product, architecture and privacy baseline | Mr-MarcelluS | M1 | 2 | None |
| #2 | Validate and maintain official India response guidance | haneeshraj14-design | M1 | 2 | None |
| #3 | Validate user journeys and accessible prototype with synthetic scenarios | siriramya28 | M1 | 3 | None |
| #9 | Bootstrap pinned Android app, core and data modules | Mr-MarcelluS | M2 | 3 | #1 |
| #14 | Implement versioned domain contracts and fixture compatibility | Mr-MarcelluS | M2 | 2 | #1, #9 |
| #15 | Add Android CI, dependency checks and test foundations | haneeshraj14-design | M2 | 2 | #9 |
| #16 | Implement share and paste intake with safe result states | siriramya28 | M2 | 3 | #9, #14 |
| #20 | Implement explainable local text indicators and coverage handling | haneeshraj14-design | M2 | 4 | #14 |
| #24 | Implement bounded structural URL parsing without network access | haneeshraj14-design | M2 | 3 | #14 |
| #21 | Demonstrate offline text-to-incident-to-response vertical slice | siriramya28 | M2 | 2 | #16, #20, #24, #36, #43, #44, #55 |
| #36 | Implement encrypted incident repository and migration-safe persistence | Mr-MarcelluS | M2 | 4 | #14 |
| #43 | Implement independent exposure questionnaire and urgent-help entry | siriramya28 | M2 | 2 | #14, #16 |
| #44 | Implement curated guidance catalog and exposure routing | haneeshraj14-design | M2 | 3 | #2, #14 |
| #55 | Implement and audit vault authentication, backup exclusion and deletion | Mr-MarcelluS | M2 | 4 | #9, #14 |
| #39 | Build incident list, detail and local timeline management | siriramya28 | M3 | 3 | #36, #55, #21 |
| #40 | Preserve immutable encrypted evidence with crash-safe file handling | Mr-MarcelluS | M3 | 4 | #36, #55, #21 |
| #30 | Implement selected screenshot import and review | siriramya28 | M4 | 2 | #40 |
| #32 | Integrate bundled Latin OCR with correction and offline tests | siriramya28 | M4 | 4 | #30, #20, #24 |
| #58 | Evaluate risk rules on held-out synthetic and adversarial cases | haneeshraj14-design | M5 | 4 | #20, #24, #32 |
| #65 | Run release security, accessibility and device acceptance suite | haneeshraj14-design | M5 | 4 | #39, #40, #32, #58, #68, #15 |
| #66 | Prepare reproducible synthetic end-to-end demonstration | siriramya28 | M5 | 1 | #65 |
| #67 | Finalize release handoff, privacy notice and distinct product identity | Mr-MarcelluS | M5 | 2 | #65, #66 |
| #68 | Export selected evidence and incident summary with consent | Mr-MarcelluS | M3 | 4 | #39, #40 |

## Complete original-issue mapping

| Original | Action | Successor / decision | Reason |
| --- | --- | --- | --- |
| #1 S0.1 — Finalize ScamShield MVP scope | edit | #1 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #2 S0.2 — Research official cyber-fraud reporting pathways | edit | #2 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #3 S0.3 — Define ScamShield user journey | edit | #3 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #4 S0.4 — Define ScamShield system architecture | supersede | #1 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #5 S0.5 — Design ScamShield database schema | supersede | #36 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #6 S0.6 — Define ScamShield REST API contract | supersede | #14 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #7 S0.7 — Design deterministic risk engine | supersede | #20 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #8 S0.8 — Create ScamShield threat model | supersede | #55 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #9 S1.1 — Initialize Android project architecture | edit | #9 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #10 S1.2 — Implement Compose navigation and MVVM foundation | supersede | #16 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #11 S1.3 — Initialize FastAPI backend | defer | #1 | No remote computation is required; backend is deferred by ADR-001. |
| #12 S1.4 — Configure PostgreSQL SQLAlchemy and Alembic | defer | #1 | Server database is deferred; Room persistence is owned by #36. |
| #13 S1.5 — Implement authentication foundation | defer | #1 | Server accounts/tokens are excluded; local vault authentication is owned by #55. |
| #14 S1.6 — Implement risk indicator/risk band data structures | edit | #14 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #15 S1.7 — Establish automated testing foundation | edit | #15 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #16 S2.1 — Build Android text analysis screen | edit | #16 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #17 S2.2 — Integrate Retrofit with analysis API | supersede | #21 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #18 S2.3 — Implement POST /api/v1/analysis/text | supersede | #20 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #19 S2.4 — Implement analysis request validation and response schema | supersede | #14 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #20 S2.5 — Implement initial scam indicators | edit | #20 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #21 S2.6 — Integrate end-to-end text analysis vertical slice | edit | #21 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #22 S2.7 — Implement analysis loading error and uncertainty states | supersede | #16 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #23 S3.1 — Implement suspicious entity extraction | supersede | #20 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #24 S3.2 — Implement URL detection and normalization | edit | #24 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #25 S3.3 — Implement structural URL risk analysis | supersede | #24 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #26 S3.4 — Implement basic typosquatting detection | defer | #1 | Domain-similarity scoring needs a maintained allowlist and false-positive evaluation; structural parsing remains in #24. |
| #27 S3.5 — Expand explainable risk scoring | supersede | #20 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #28 S3.6 — Build synthetic risk-engine evaluation dataset | supersede | #58 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #29 S3.7 — Build automated risk-engine test suite | supersede | #58 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #30 S4.1 — Implement Android screenshot/image picker | edit | #30 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #31 S4.2 — Implement screenshot preview and review | supersede | #30 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #32 S4.3 — Integrate on-device ML Kit OCR | edit | #32 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #33 S4.4 — Handle OCR failure and empty-text cases | supersede | #32 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #34 S4.5 — Connect OCR output to analysis pipeline | supersede | #32 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #35 S4.6 — Validate screenshot privacy and local OCR behavior | supersede | #32 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #36 S5.1 — Implement Incident backend model and API | edit | #36 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #37 S5.2 — Implement Evidence backend model and API | supersede | #40 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #38 S5.3 — Implement incident ownership authorization | supersede | #36 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #39 S5.4 — Build incident list and detail screens | edit | #39 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #40 S5.5 — Implement evidence capture and metadata storage | edit | #40 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #41 S5.6 — Implement incident timeline | supersede | #39 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #42 S5.7 — Test IDOR/BOLA protections | supersede | #55 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #43 S6.1 — Build incident response questionnaire | edit | #43 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #44 S6.2 — Design safe incident response guidance | edit | #44 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #45 S6.3 — Integrate verified official response pathways | supersede | #44 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #46 S6.4 — Implement Room offline persistence | supersede | #36 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #47 S6.5 — Implement offline-first incident behavior | supersede | #21 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #48 S6.6 — Implement WorkManager synchronization | defer | #1 | No cloud replicas exist in MVP; background sync would add unnecessary data transmission. |
| #49 S6.7 — Implement synchronization retry/conflict handling | defer | #1 | No cloud sync or distributed conflicts exist; local operation recovery belongs to #36. |
| #50 S7.1 — Harden authentication and token handling | supersede | #55 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #51 S7.2 — Perform authorization and IDOR/BOLA audit | supersede | #55 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #52 S7.3 — Harden backend input validation | supersede | #14 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #53 S7.4 — Perform SQL injection security testing | supersede | #36 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #54 S7.5 — Harden evidence/file uploads | supersede | #40 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #55 S7.6 — Secure Android local storage and credentials | edit | #55 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #56 S7.7 — Implement API rate limiting and abuse controls | defer | #1 | No public API exists to rate-limit; bounded local input belongs to #14 and #24. |
| #57 S7.8 — Audit logs for sensitive information | supersede | #65 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #58 S7.9 — Evaluate risk-engine false positives and false negatives | edit | #58 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #59 S8.1 — Containerize FastAPI backend with Docker | defer | #1 | No backend runtime is selected, so containerization has no MVP deployable. |
| #60 S8.2 — Deploy backend with HTTPS | defer | #1 | No backend runtime is selected; signed Android distribution belongs to #65/#67. |
| #61 S8.3 — Configure production PostgreSQL | defer | #1 | No PostgreSQL server is selected; local migrations belong to #36. |
| #62 S8.4 — Document REST API | supersede | #14 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #63 S8.5 — Create architecture documentation | supersede | #1 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #64 S8.6 — Document threat model and security decisions | supersede | #55 | Consolidate overlapping work into a complete verifiable local-first deliverable; not marked implemented. |
| #65 S8.7 — Create testing and evaluation report | edit | #65 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #66 S8.8 — Prepare final 5–7 minute demonstration scenario | edit | #66 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |
| #67 S8.9 — Complete final README and project documentation | edit | #67 | Retain issue reference; revise to local-first deliverable with owner, dependencies and testable acceptance. |

## Acceptance and testing by issue

### #1 — Review and accept product, architecture and privacy baseline

Review PRD/SRS, technology alternatives, ADRs, database, contracts, threat model and release gates. Confirm team skills and weekly capacity; adjust estimates before bootstrap.

Acceptance:

- All three developers record review of their interfaces and responsibilities
- PR is merged with cross-workstream approval; assumptions and exclusions are explicit
- Any changed decision updates ADR, contract and affected backlog before feature work

Testing: Run foundation validation and trace each SRS requirement to an owned issue. No application implementation is claimed.

### #2 — Validate and maintain official India response guidance

Verify bank/1930/NCRP and Chakshu routing using current official sources. Complete the live-form verification that automated access could not perform, without submitting fictional reports.

Acceptance:

- Record live route access date, category distinctions and sources; reconcile timing differences without inventing deadlines
- Review contracts/guidance.json with another developer and record reviewer/date
- Financial-loss route takes priority; no claim of automated filing or guaranteed recovery

Testing: Check allowed destinations, stale/review-age behavior, no sensitive query parameters and correct urgent route on paid=YES.

### #3 — Validate user journeys and accessible prototype with synthetic scenarios

Create low-fidelity intake, results, exposure, incident and export flows. Test with 5–8 consenting adults using fictional messages; do not retain identifying data.

Acceptance:

- Record task completion and misunderstandings with counts and limitations
- No participant interprets no-signals result as guaranteed safe; revise copy otherwise
- Record team skills/access needs and unsupported-language expectations

Testing: TalkBack/focus and 200% text review on prototype where possible; check urgent help is reachable without analysis.

### #9 — Bootstrap pinned Android app, core and data modules

Create Kotlin/Compose app, pure Kotlin core and Android data modules with manual injection. Pin compatible JDK/Gradle/AGP/Kotlin/dependencies and check in verified wrapper.

Acceptance:

- Fresh checkout builds documented debug artifact and runs core tests
- Module dependencies keep core free of Android and I/O
- Merged manifest has minimal permissions; no network or inbox access; toolchain documented

Testing: Clean build, wrapper/dependency checksum verification, emulator launch and module boundary check.

### #14 — Implement versioned domain contracts and fixture compatibility

Implement AnalysisInput/Result, ExposureAnswers, repository command/result and guidance identifiers from shared schemas. Define UTF-16 spans and code-point limits.

Acceptance:

- Kotlin fixtures match JSON v1 examples and reject unsupported versions
- Errors distinguish validation, key, storage and cancellation failures without private payloads
- Contract changes require ADR and both consumer owners reviewing

Testing: Boundary lengths, enum values, missing fields, Unicode spans and serialized round trip.

### #15 — Add Android CI, dependency checks and test foundations

Extend foundation workflow with core tests, Android lint and build; add Room/UI test harness. Pin Actions, minimal permissions, no real data artifacts.

Acceptance:

- Clean PR runs reproducible tests/build/lint
- Document physical-device tests CI cannot prove
- Record stable check names before proposing required-check settings

Testing: Demonstrate one intentional fixture failure is caught locally, then restore passing tests; inspect artifact/log content.

### #16 — Implement share and paste intake with safe result states

Build navigation, text preview, explicit analyze, cancellation, result/uncertainty and empty/error states. No inbox or clipboard monitoring.

Acceptance:

- User can paste/share up to 20k code points and review before analysis
- Suspicious URLs are defanged and never navigated; original text remains available to user
- Oversize/unsupported/empty input is explained; process recreation does not persist plaintext drafts

Testing: Share intent injection, oversized/Unicode text, cancel, rotation/process death, TalkBack and large font tests.

### #20 — Implement explainable local text indicators and coverage handling

Build deterministic bounded rules for explicit secret/APK requests, pressure plus sensitive action and advance-fee patterns. Treat negation/quoted safety advice carefully; no LLM.

Acceptance:

- Findings have stable IDs, spans and explanation keys with rulesVersion
- NO_SIGNALS never asserts safety; unsupported content is UNASSESSED
- Repeated phrases do not inflate severity; behavior matches frozen rule policy

Testing: Unit cases for benign alerts, negations, mixed/unsupported language, adversarial repetition and 20k latency budget.

### #24 — Implement bounded structural URL parsing without network access

Extract up to 20 URL candidates, preserve originals, normalize host for display and explain structural cues. Avoid live fetch, redirects, executable schemes and unvalidated domain reputation.

Acceptance:

- IP/userinfo/punycode/short-link cues explain limitations rather than asserting fraud
- Parser enforces candidate/length bounds and maps spans to reviewed text
- No DNS/HTTP requests or clickable submitted links; malformed input fails safely

Testing: Test encoded separators, suffix deception, IPv6, ports, Unicode, punctuation and pathological regex inputs.

### #21 — Demonstrate offline text-to-incident-to-response vertical slice

Integrate intake, local findings, exposure routing, minimal authenticated save/reopen and curated guidance. This is the first end-to-end value demonstration, before screenshot/export completion.

Acceptance:

- Synthetic case completes whole flow in airplane mode and reopens after restart
- Urgent financial-loss help works from home without a message or saved incident
- Record a reproducible demo and current limitations; no real call/report is made

Testing: End-to-end UI test plus physical-device walkthrough; raw storage/log checks and no app-network traffic.

### #36 — Implement encrypted incident repository and migration-safe persistence

Implement Room metadata and encrypted sensitive payloads, per-incident IDs/keys, timeline/exposure records, transactional create/update, and delete recovery. Pair with #55 before accepting real evidence.

Acceptance:

- Offline create/get/list/update/delete obey contracts and FK ownership
- Staging/deletion recovery is idempotent under crash and storage-full conditions
- Versioned migration preserves data; no destructive fallback or plaintext notes/title/message columns

Testing: Room migration, cross-incident references, repeated create idempotency, interrupted save/delete and ciphertext inspection.

### #43 — Implement independent exposure questionnaire and urgent-help entry

Ask clicked, secret disclosed, installed/remote access and paid with YES/NO/UNKNOWN. Do not request actual credentials. Permit urgent help without analysis.

Acceptance:

- Answers persist only on explicit save and can be changed with timeline event
- Unknown is not coerced to no; paid=YES surfaces urgent help before evidence forms
- Accessible questions use non-blaming language and work offline

Testing: All answer states, no-content entry, back navigation, TalkBack and safe cancellation.

### #44 — Implement curated guidance catalog and exposure routing

Load versioned reviewed guidance; deterministic routing independent of risk score. Support exact allowlisted browser destinations and user-triggered dialer via UI.

Acceptance:

- All 81 exposure combinations have expected action ordering
- Paid=YES includes bank/1930/NCRP; stale bundle does not hide urgent basics
- Source/date and local-only action progress shown; no procedure generated from message text

Testing: Schema/destination checks, invalid bundle fallback, 90-day staleness, unknown answers and no private URL parameters.

### #55 — Implement and audit vault authentication, backup exclusion and deletion

Build device-authenticated Keystore wrapping and incident data-key envelope. Require secure device lock for durable save, lock on background timeout, test backup/D2D exclusions and lost-key handling.

Acceptance:

- Authenticated reads fail closed while locked and after key invalidation; no silent reset
- Sensitive files/DB/cache excluded from cloud and device-transfer backups on supported OS versions
- Delete-all destroys keys and removes local copies; user sees recovery/export limits

Testing: GCM tamper/AAD swap, lock/biometric changes, backup inspection, logcanary, process death and cache cleanup. Independent security review required.

### #39 — Build incident list, detail and local timeline management

Complete case navigation, edit/append event actions, archive/reopen, user-entered official references and delete confirmations. Do not imitate official case status.

Acceptance:

- Saved cases list/reopen offline with paginated metadata
- Archive is separate from deletion; user-entered reference explicitly labeled
- Timeline keeps assessment versions and distinguishes user-reported times from import times

Testing: Empty/large lists, update/archive/delete, corrupt/key-unavailable states, accessibility and process recreation.

### #40 — Preserve immutable encrypted evidence with crash-safe file handling

Implement validated file staging, immutable original bytes/digests, metadata, per-case limits and original/derived distinction. Use generated paths and safe ContentResolver handling.

Acceptance:

- Original decrypted bytes hash matches import; correction never overwrites original
- 10MiB/20MP, 25 items/case and 250MiB total limits fail with clear errors
- Interrupted imports/deletes cannot expose plaintext or leave visible partial records

Testing: Hostile provider, revoked URI, malformed MIME, traversal, decompression bounds, disk-full and staged-crash recovery tests.

### #30 — Implement selected screenshot import and review

Add picker/share image adapter, safe preview, MIME/magic checks and byte/pixel limits. Allow only single PNG/JPEG import; no broad gallery permission.

Acceptance:

- User can select, preview and cancel without durable save
- Refused URI/format/oversize errors are useful and preserve existing case
- Original image is passed through immutable vault path only on explicit save

Testing: Permission/grant revocation, cancelled picker, huge image header, process death and no plaintext cache residue.

### #32 — Integrate bundled Latin OCR with correction and offline tests

Run bundled on-device ML Kit OCR on bounded decode, display editable text and mark it as derived. Route confirmed text through same analysis contract.

Acceptance:

- Cold-start OCR works in airplane mode with bundled model
- Empty/failure/unsupported script returns correction/manual input options
- Corrected text and assessment are separate from immutable original; model/license/toolchain pinned

Testing: Clean/blurred/rotated/mixed-script test images; cancellation, p95 latency, byte-level original preservation and network/SDK behavior audit.

### #58 — Evaluate risk rules on held-out synthetic and adversarial cases

Build development and held-out sets totaling at least 120 synthetic cases with template separation, two-person annotation and recorded limitations.

Acceptance:

- Report category confusion matrices, precision/recall, coverage, abstentions and uncertainty intervals
- Evaluate SRS targets without tuning on holdout or mislabeling unsupported as benign
- Version rules/dataset and publish failures plus allowed product claims

Testing: Reproducible evaluation command, leakage/duplicate review, high-concern precision target 0.90 and suspicious recall target 0.80 on held-out synthetic set.

### #65 — Run release security, accessibility and device acceptance suite

Execute release matrix including all exposure combinations, UI/accessibility, storage migration, privacy/network, URI grants and signing/upgrade. Record actual results and remaining limitations.

Acceptance:

- No known critical/high defects; every SRS acceptance has evidence
- Backup/D2D, key-loss, delete/export and interrupted-operation tests pass on documented devices
- Reference-device latency and usability outcomes recorded with real counts, not assumed success

Testing: Full offline journey, canary leakage checks, crash/recovery injection, TalkBack/200% text and signed artifact install/upgrade tests.

### #66 — Prepare reproducible synthetic end-to-end demonstration

Prepare 5–7 minute demo of review, exposure, save/reopen, screenshot/OCR, reviewed export and delete. Use only fictional messages and reserved domains.

Acceptance:

- Demo script and expected outputs reproducible from clean test setup
- No actual call/report/submitted suspicious URL or APK execution
- Known language/detection/device-recovery limitations are demonstrated or stated

Testing: Dry run on target device within time budget; another teammate follows the script.

### #67 — Finalize release handoff, privacy notice and distinct product identity

Publish accurate setup, test results, build/signing/distribution and maintenance instructions. Resolve confusion with Singapore government ScamShield before public distribution; do not rename repository without a separate decision.

Acceptance:

- README distinguishes implemented from planned and links current artifacts
- Privacy/retention/export/recovery notice matches measured behavior
- Naming and non-affiliation review resolved; release owner checks current distribution obligations and licenses

Testing: Fresh developer setup walkthrough, link check, release certificate/checksum verification and documentation review by both teammates.

### #68 — Export selected evidence and incident summary with consent

Create one-way evidence export with text summary and versioned JSON manifest, selection/redaction preview and optional original files. Export crosses the app trust boundary and is not a backup/restore feature.

Acceptance:

- Preview shows exact included originals/derivatives; default summary contains no unintended private fields
- Manifest identifies selected files, original/derived status, byte counts and SHA-256 without keys/internal paths
- Temporary FileProvider grants/caches expire after 15 minutes and startup cleanup; user warned recipient copies cannot be recalled

Testing: Subset/redaction tests, byte digest verification, hostile filenames, recipient access scope, expiry/cancel/restart cleanup and archive manifest schema check.

