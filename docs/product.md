# Product requirements and Software Requirements Specification v1

Status: selected engineering baseline pending team PR review. Owner: Mr-MarcelluS. Requirements are normative for the proposed MVP; research findings and untested assumptions are in [research](research.md).

## Outcome and target users

Help an ordinary adult Android user in India decide what to do with suspicious content and preserve useful records without silently uploading it. The product is an aid, not antivirus, an official reporting system, legal advice, or a guarantee of safety.

Three design personas (hypotheses, not interview findings): a banking user unsure about a KYC request; a student evaluating an advance-fee job; a distressed user who has paid or disclosed credentials. Prioritize the distressed user's immediate actions over filling out forms. English is the initial validated language; provide large text, TalkBack, plain language, and no color-only meaning.

## MVP scope

MUST: explicit paste/share of text; local indicators and explanations; uncertainty and input limitations; independent exposure questions; local incident creation/list/detail/timeline; selected screenshots with correctable local OCR; encrypted evidence preservation; user-controlled reviewed export; delete incident/all data; accessible source-linked response cards; offline operation.

SHOULD: link domain highlighting without clickable suspicious URLs, safe resume after process death, export redaction preview, storage-limit messages, user-entered official reference numbers. These are in the release backlog where specified.

EXCLUDED: automatic SMS/notification/contact scraping; default-SMS role; phone monitoring; installed-app scanning or APK execution; automatic URL visits/redirect expansion; cloud accounts/sync; social feeds; crowd reporting; automatic filing; claims of police integration; LLM chatbot; trained scam classifier; full forensic acquisition; encrypted backup/restore; multilingual detection claims. These require new evidence and ADRs, not leftover draft tasks.

Later candidates, in order: validated regional-language packs; recovery/backup design; opt-in reputation lookup; carefully evaluated on-device classifier; cloud sync only if user research demonstrates need and the team can support authorization and operations. An LLM may eventually help explain validated findings, but must not author official procedures or override exposure routing.

## User journeys

| Scenario / experience | Available information and limits | Ask (never ask for secrets) | Safe response and forbidden claim |
| --- | --- | --- | --- |
| Banking SMS threatening closure | Text, claimed sender, URL; sender identity unverified | Did you click, enter data, pay or install anything? | Verify using bank's own app/site/contact; do not say all KYC requests are fraud |
| WhatsApp KYC screenshot | Image and corrected text; OCR may miss digits | What action was requested; any exposure? | Separate original from corrected text; never authenticate logos/accounts from screenshot |
| Link clicked | User report; no device telemetry | Entered password/OTP, downloaded/installed, granted access? | Stop interacting; escalate according to actual exposure; never infer compromise from click alone |
| OTP/password disclosed | Disclosure category and account type | Was money moved? Is access still available? | Urgent official account/bank contact; use trusted device for recovery; never collect OTP/password itself |
| APK installed or remote access granted | User report of install/permissions | Is affected phone still used for banking? Any loss? | Stop sensitive activity on that device, use trusted device for official help; no clean-device certification or automatic reset |
| Money transferred | Time, amount, payment reference if known | Enough context for a checklist; fields optional | Surface bank/1930/NCRP immediately; preserve later; no recovery promise or mandatory wait for score |
| Job/investment offer | Advance-fee/return claims and contextual evidence | Payment or identity documents already shared? | Independent verification and exposure-led response; no declaration that an employer/person is criminal |
| Delivery, government/support impersonation | Claimed organization, demanded fee/secret/access | Same exposure categories | Explain pressure/request patterns; do not contact suspicious sender for verification |

Flow: intake preview → explicit Analyze → result with reasons and limitations → exposure questions (also reachable from home without content) → urgent actions where needed → optional save incident → add evidence/timeline → preview export or open official route. Saving is separate from analyzing. Never put an evidence-save step before urgent help. Cancelling before save discards draft private content; recreation must not place it in saved-state bundles.

## Functional SRS and traceability

| ID | Requirement and verifiable acceptance | Delivery issues |
| --- | --- | --- |
| F01 | Accept 1–20,000 Unicode code points via paste or ACTION_SEND text; preview and cancel; reject oversize input without truncation | #16, #14 |
| F02 | Return versioned findings and evidence spans locally; unknown/unsupported inputs show LIMITED or UNSUPPORTED; no Safe verdict or probability | #20, #24, #58 |
| F03 | Exposure answers are independent yes/no/unknown for click, secret disclosure, install/remote access, payment; guidance works without analysis | #43, #44 |
| F04 | Save an incident with assessment snapshot, exposures and events atomically; reopen offline after process restart | #36, #39, #21 |
| F05 | Import one user-selected PNG/JPEG at a time, ≤10 MiB and ≤20 MP; retain original bytes, correct OCR separately | #30, #32, #40 |
| F06 | Preserve originals with digest and source metadata; timestamp is app-observed unless user-supplied; hash is not authenticity proof | #40 |
| F07 | Export selected originals plus human-readable summary and machine-readable manifest after preview/consent; warn recipient obtains readable data | export issue in backlog |
| F08 | Delete one incident or all data with confirmation, including files, metadata, thumbnails and temporary exports; interrupted deletion resumes | #36, #55 |
| F09 | Show dated curated actions and exact official destinations; no content in URL parameters; user initiates browser/dialer action | #2, #44 |
| F10 | Maintain local incident states OPEN/ARCHIVED; archive does not delete; user-entered official reference does not imply synchronization | #39 |
| F11 | Enforce authenticated vault access; allow unsaved review and urgent guidance without vault setup | #55 |
| F12 | Explain local retention, deletion, export and device-loss limitations before first save; no silent uploads or analytics | #55, #67 |

## Quality requirements and success measures

N01: zero app-originated network requests during review/save/OCR/export tests; merged manifest must not request INTERNET, SMS, contacts, call-log, broad storage or accessibility-service access. External browser/dialer actions are explicit exceptions outside app processing.

N02: on a documented reference device, local text analysis p95 ≤500 ms for 20k characters; OCR p95 ≤5 s on bounded images. Record actual device/OS and cold/warm runs; these are targets, not measured results. No work that blocks UI thread for image decode or encryption.

N03: every exposure combination must route deterministically; paid=yes always surfaces financial-loss guidance even with empty or low-signal input. All corruption/key-unavailable tests fail closed without losing unrelated incidents.

N04: 200% font scaling and TalkBack can complete primary journey; touch targets ≥48 dp, meaningful focus order, contrast checked, no color-only severity.

N05: a held-out synthetic set of at least 120 cases across suspicious/benign/ambiguous categories reports confusion matrix, coverage and abstentions. Target high-concern precision ≥0.90 and suspicious-example recall ≥0.80 on this set, with class counts and uncertainty intervals; no extrapolation to real users. Failure means revise rules/claims, not secretly retune the holdout. Safety acceptance also requires all urgent-response tests, regardless of classifier metrics.

N06: 5–8 consented participants use fictional scenarios; target ≥80% complete save/find-guidance tasks unaided and none interprets a no-signal result as a safety guarantee. Report numerator/denominator and limitations. Fix dangerous misunderstanding before beta.

N07: release has no known critical/high security defects, tested schema migration without destructive fallback, complete deletion and recovery-from-interruption tests, and reproducible setup. Device loss/uninstall/key loss can make local records unrecoverable; communicate clearly.

## Scope control

Any new data destination, permission, language claim, model, official procedure or schema/interface break requires an ADR, affected contract fixtures, a reviewer from another workstream, and backlog changes before implementation. If capacity slips, keep the text-to-guidance-to-incident slice and postpone OCR to a later beta; do not cut privacy or urgent response controls. Deadline and weekly availability are unconfirmed; roadmap estimates are planning assumptions.
