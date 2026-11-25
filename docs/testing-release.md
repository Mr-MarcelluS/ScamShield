# Testing, deployment and release strategy

## Verification layers

| Layer | Required evidence | Owner |
| --- | --- | --- |
| Foundation | JSON syntax/schema examples, full 67-issue mapping, assignee validity, acyclic dependencies, local links | Mr-MarcelluS |
| Domain | Request/negation matching, coverage, repeatability, bounded URL parsing, all exposure combinations, guidance ordering | haneeshraj14-design |
| Storage | Room migrations/FKs, ciphertext swap rejection, interrupted save/delete, idempotency, storage full and key invalidation | Mr-MarcelluS, reviewed by haneeshraj14-design |
| UI | Share/paste/cancel, large fonts/TalkBack, process recreation, urgent help without content, source-link confirmation | siriramya28 |
| OCR | Clean/blurred/rotated/mixed-script images, OCR-empty and cancellation, offline cold start, correction vs original | siriramya28, reviewed by Mr-MarcelluS |
| Security | Raw DB/file/log canaries, backup and transfer exclusions, URI grants/expiry, exported components, permission and network inspection | haneeshraj14-design |
| System | Offline share → findings → exposure → save → restart → reopen → add screenshot → export → delete | All, #65 owns evidence |

At bootstrap, use JUnit for pure core, Android instrumented tests for Room/Keystore/URI behavior, Compose UI tests for primary screens. Run unit/lint on each PR and instrumented/emulator checks where CI supports them; physical-device crypto/backup tests are a release gate. CI should never process real reports or upload private screenshots. Foundation CI is provided now; application CI belongs to #15 after #9.

## Evaluation protocol

Create at least 120 synthetic cases before tuning: balanced suspicious/benign/ambiguous examples with English scenarios across KYC, job, delivery, OTP, support/APK, payment/investment and impersonation. Include negated safety advice, legitimate transaction alerts, obfuscated/Unicode links, quoted scams and unsupported scripts. Separate development and locked holdout by scenario templates to avoid near-duplicate leakage. Have two people label independently, reconcile disagreements and record annotation rules. Store text and labels with synthetic provenance, never harvested victim messages.

Report per-category confusion matrix, precision/recall of high-concern and concern outputs, abstention/coverage, counts and uncertainty intervals. Unknown/unsupported is not a benign success. The target thresholds in the SRS are release criteria on this synthetic set, not real-world accuracy claims. Include failed examples and false confidence observations. A changed rule version requires rerunning the fixed set; do not relabel failures to pass.

Exposure router: test all 3^4=81 combinations of clicked/secret/installed/paid YES/NO/UNKNOWN. paid=YES always includes urgent bank/1930/NCRP actions; installed=YES includes trusted-device advice; UNKNOWN prompts without dismissing risk. Test independent access from home. Content result must never suppress exposure actions.

Measure text and OCR p95 on a named physical reference device over at least 30 timed runs per size class, including cold/warm OCR and airplane mode. Record Android version, RAM, image sizes and library versions. Min SDK 26 is the proposed support floor; test API 26, 31 and the current target SDK at bootstrap, plus one physical device. It is an engineering choice, not a claim that older Android is unsupported by OCR itself.

## Release/deployment architecture

No runtime service, database host or paid AI account is required. Developer machines → reviewed PR → GitHub Actions checks → reviewed release commit → signed Android artifact → consented testers. Keep release signing keys outside git and public CI logs. First beta may be manually signed by the release owner on a controlled machine; record certificate fingerprint and SHA-256 artifact checksum. Do not distribute debug builds containing real evidence. Play internal testing is optional and requires account/policy readiness; do not provision hosting or incur charges automatically.

#9 pins reproducible toolchain and dependency verification. #15 adds Android jobs after wrapper exists. #65 verifies fresh install and upgrade migration. Existing branch rules require another person's approval, last-push approval and resolved review threads; use squash merge and do not bypass protection. Set required checks only after stable job names and successful runs exist.

Release gate: accepted requirements/ADRs/contracts; all MVP dependencies closed as completed with evidence; no known critical/high findings; safety and accessibility tests passed; official destinations reviewed and live forms walked through in #2; privacy notice accurate; name/affiliation review in #67; signing/upgrade/delete tests; measured limitations in evaluation report. Official reporting links opening is not evidence that a complaint was submitted.

Rollback: retain previous signed build and its compatible schema policy; never downgrade a DB destructively. Prefer a forward fix if schema downgrade is unsafe. A bad rules/guidance bundle is replaced in a new signed app release; old assessment snapshots keep their recorded version. Without a backend there is no instant remote kill switch; stale guidance should retain broad official help and suppress brittle procedural details.

## Demo and handoff

Five–seven minute synthetic demo: paste fictional KYC text with an `example.invalid` link → inspect indicators → disclose no secrets → save case → restart in airplane mode → attach fictional screenshot and correct OCR → change paid answer to YES and show urgent pathways → preview selected export → delete case. Never actually call 1930, submit an official complaint, visit a suspicious URL or install an APK during testing.

Publish a test report with actual results, not prefilled success. This foundation PR does not implement or validate the Android app. Open issues #58/#65/#66/#67 own evaluation, release verification, demonstration and handoff respectively.
