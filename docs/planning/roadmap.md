# Roadmap and team handoff

## Delivery sequence

The 67-issue draft becomes 23 focused deliverables across five milestones. Twenty-two issue references are reused and one export task is added. Thirty-five overlapping issues are superseded and ten unnecessary/future tasks are deferred with explanations. No issue is deleted. Existing milestone IDs 1–5 are reused; empty legacy milestones 6–9 are closed with migration notes. Their original names remain in the audit record.

| Milestone | Exit gate | Parallel work / critical dependencies |
| --- | --- | --- |
| M1 Decisions and validation | #1 accepted with reviewed PRD/SRS/ADRs; #2 source verification; #3 user-flow findings | Requirements review, official-route review and prototype validation can run together |
| M2 Offline text slice | #21 proves share/paste → explanation → exposure → authenticated save/reopen → guidance offline | After #9/#14, UI (#16/#43), rules (#20/#24/#44) and persistence/vault (#36/#55) run separately against contracts; integrate continuously |
| M3 Evidence workflow | Full incident management, immutable encrypted originals and reviewed export | #39 and #40 can proceed together after the slice; export depends on both |
| M4 Screenshot/OCR | #30/#32 prove offline image review and correction without original mutation | OCR fixtures can be prepared earlier; actual import waits for safe vault path |
| M5 Evaluated beta | #58/#65 pass measured quality/safety gates, then #66/#67 handoff | Evaluation and documentation preparation can run in parallel; release waits on all gates |

Milestones are gates, not rigid departmental silos. Shared contracts are defined before feature implementation. #1 acceptance is the start gate for bootstrap; #2 validation gates guidance release. No current application is claimed complete.

## Team ownership

Assignments reflect a proposed balanced architecture, not verified personal expertise. All three handles are verified repository collaborators and eligible assignees. Confirm availability and Kotlin learning needs in #1; trade tasks through reviewed issues if necessary.

| Developer | Primary ownership | Start now | Next after decisions | Review partner |
| --- | --- | --- | --- | --- |
| Mr-MarcelluS | Architecture integration, build bootstrap, contracts, encrypted persistence/export, release docs | #1 | #9 → #14, then #36/#55; coordinate #40 and export | haneeshraj14-design reviews crypto/storage; siriramya28 reviews app-facing contracts |
| haneeshraj14-design | Threat/rule analysis, official guidance, evaluation and test infrastructure | #2 | #15, #20/#24/#44 after their dependencies | Mr-MarcelluS reviews deterministic contracts; siriramya28 reviews explanation/guidance comprehension |
| siriramya28 | User research, Compose flows, exposure, incident UI, screenshot/OCR, demo | #3 | #16 → #43; #21 integrates, later #39/#30/#32 | haneeshraj14-design reviews safety copy; Mr-MarcelluS reviews persistence and image boundaries |

One primary assignee owns completion; supporting reviewers are explicit in the issue/document. Effort totals are approximately 25/22/20 focused workdays (one planning day = four productive hours), not equal issue counts. At an assumed 10–12 hours per developer per week, 268 base hours plus 30% contingency suggests roughly 10–12 weeks; calendar dates are intentionally unset because examinations, availability and Kotlin experience are unknown. Review effort is shared and included in contingency. Re-estimate after M1 and the first slice.

Rotate weekly integration duty among all three; it means checking contract drift and blocked work, not owning every merge. Limit each developer to one active build task plus one review. Use fakes/fixtures to unblock consumer development while repository adapters are built. Do not make UI wait for a nonexistent backend.

## Shared source of truth across three chats

Every developer starts from latest merged main and reads README, their issue, contracts and ADRs. Put cross-cutting decisions in a PR, not only a chat transcript. Include changed fields/enums and affected consumers. A domain developer cannot silently change risk bands; a storage developer cannot change IDs/envelopes without migration and UI review. The revised docs are proposed until the PR merges, and GitHub issue bodies point to that review gate.

Definition of Done: linked reviewed PR; acceptance evidence; appropriate automated tests; no private data/secrets; changed docs/contracts/migrations included; relevant security/accessibility checks; another developer can reproduce; merged build passing. Close as completed only after these are true. A superseded issue is closed as not planned, never completed.

## Existing project board: access limitation and precise owner steps

`gh project list --owner Mr-MarcelluS --format json` returned “Resource not accessible by integration” for existing Projects nodes. That confirms an access limitation, not an empty account or permission to create a duplicate. Board identity, fields, views and items could not be inspected or changed in this session. Repository issues/milestones remain the usable source of truth.

Owner action after opening the **existing** board:

1. Locate the board linked to Mr-MarcelluS/ScamShield in GitHub Projects; do not create another. If needed, grant this GitHub connection read/write access to Projects through its installation/app settings. Do not share tokens in chat.
2. Keep useful existing views. Add missing repository issues from the active table in backlog.md; verify each is present once. Keep closed history accessible in an “All history” table, and filter the main work view to open issues from this repository.
3. Use existing equivalent statuses or configure Backlog, Ready, In progress, In review, Done. Mark #1/#2/#3 Ready; all dependent work Backlog until dependencies clear. Closed superseded/deferred work should be excluded from active completion metrics, not counted as shipped.
4. Group work by milestone and add assignee/priority columns. Add a security/testing view filtered by those existing labels. Use one consistent `risk-engine` label; retain the unused legacy label rather than deleting it without need.
5. Enable issue-close automation only with the above distinction: Done means delivered for active tasks; closed-as-not-planned remains history. Verify with an existing issue rather than creating dummy project work.
6. Record board URL, view/filter settings and a snapshot in a small follow-up PR to this execution record. If connection access is enabled, a later automated pass can reconcile exact fields/items.

No Project statuses/views/automation are reported as successfully changed here. No repository visibility, collaborator permissions or main-branch protections are changed.
