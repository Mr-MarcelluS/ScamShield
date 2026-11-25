# Discovery and evidence register

Research reviewed 2026-11-25. This is desk research, not a user study or a measured comparison of detection accuracy. Official guidance, vendor descriptions, engineering inferences, and assumptions are separated below. Source availability does not prove a service works end to end.

## Problem findings

**Official guidance:** CERT-In describes phishing, advance-fee jobs, support impersonation, investment schemes and other social engineering patterns [R1]. RBI describes urgency, KYC impersonation, credential disclosure and unverified app installation [R2]. These support scenario coverage, not a quantitative ranking of India's most frequent scams.

**Inference:** uncertainty persists after receipt: users need to distinguish receiving a message from clicking, disclosing secrets, installing software, and transferring money. A risk score cannot answer those exposure questions. Evidence and reporting may be scattered between messaging, banking and official portals. A local incident workspace is a useful hypothesis; its demand remains unvalidated.

**Research limitation:** no interviews, device benchmark, representative labeled dataset or competitor hands-on test has been completed. Do not claim market superiority or real-world precision. #3 tests comprehension and workflow utility using fictional scenarios with 5–8 consenting adults; record findings without identities or raw communications. Convenience-sample results are not representative of India.

## Official pathways and routing

| Situation | Source-backed route | Product treatment |
| --- | --- | --- |
| Money lost or suspected financial cyber fraud | 1930 and NCRP; notify the bank through independently obtained official channels [R2, R3] | Show urgent actions before analysis or evidence forms; dialer opens only on tap; never auto-call or promise recovery |
| Other cybercrime | NCRP [R4] | Open official portal in external browser after user action; do not file on behalf of user |
| Suspected fraud communication | Chakshu/Sanchar Saathi [R3, R5] | Link to official portal and let it determine current eligibility; no invented integration API |
| Unsolicited marketing/spam | Separate communication complaint route on official service [R5] | Explain that spam and financial fraud reporting differ; no blanket fraud verdict |
| Lost device or unknown SIM connections | Other Sanchar Saathi services | Outside MVP: they solve different problems; do not fill the main response screen with unrelated government services |

The 2025 RBI circular describes a 30-day window for suspected communications. A March 2026 DoT/PIB release describes broader reporting categories and recommends prompt reporting, with seven-day wording for unsolicited communications. These are not interchangeable deadlines. The live Chakshu page returned 403 during direct retrieval, and the NCRP live form/FAQ timed out. Therefore do not hardcode eligibility windows, portal field sequences or a universal 24-hour deadline. The older NCRP instruction PDF found in search is explicitly titled for Delhi; it is not sufficient to generalize a current national procedure. #2 requires a manual live-form walkthrough before beta. Route users promptly even if an incident is old.

Prepare user-entered occurrence time, payment method, amount, transaction reference and relevant screenshots if available. These are a useful preparation checklist, not a claim about every mandatory portal field. Do not delay a bank/1930 contact to finish the checklist. An acknowledgement is not a filed FIR or proof of recovery. The app's incident status is local and never presented as official case status.

## Competitive assessment

ND means not established by the reviewed sources, **not absent**. Features and availability vary by market/device. Vendor statements have not been independently benchmarked.

| Product/service; users | Detection and primary value | Evidence / response | Privacy and limitations relevant here |
| --- | --- | --- | --- |
| Truecaller; consumer phone users | Caller identification, spam controls; current Scam Checker extends beyond caller ID [C1] | Community reporting; private incident vault ND | ROW summary says SMS content is processed on device; metadata and other data depend on features [C2]. Do not claim it uploads all SMS. Private evidence workflow is an area to validate, not a proven gap |
| Google Messages; Android messaging users | On-device spam patterns and link checks; newer enhanced protection adds cloud processing [C3] | Spam reporting/blocking; cross-app incident vault ND | Reporting can send content; processing depends on mode. Strong existing prevention should be complemented |
| Norton Genie; consumers reviewing suspicious content | AI plus threat intelligence; text/screenshot submission and explanations [C4] | Already provides next-step advice and acknowledges uncertainty; incident vault ND | Upload workflow; current product privacy notice applies [C5]. India-specific evidence workflow needs hands-on verification |
| Singapore ScamShield; Singapore residents | Message/link/number checks and blocking with official ecosystem [C6] | Reporting and response resources already exist | Privacy statement covers message/report processing [C7]. Different jurisdiction; direct product-name collision, not a template for Indian reporting |
| NCRP / 1930; victims in India | Official complaint/response pathway, not a message classifier | Official acknowledgement and tracking where supported [R4] | User submits data to authorities; ScamShield should direct, not impersonate or replace it |
| Chakshu; communication recipients in India | Official suspected-communication reporting [R5] | Supports telecom action; not financial-loss case handling | Submission to official portal; app does not copy or proxy reports |

**Recommendation:** compete on an understandable local case workflow and exposure-led response, not on claiming better detection. Current products already explain scams and offer guidance. Before public launch, review naming and choose a distinct identity if needed (#67); keep the repository name and history for now.

## Feasibility evidence and unknowns

Bundled ML Kit OCR avoids first-use model download but adds app size; Latin and Devanagari are distinct models [T1]. OCR script support does not imply scam-analysis language coverage. Start with English analysis and Latin screenshots, accept manual text, and explicitly flag unsupported languages. Hindi/Devanagari requires separate rules, evaluation and translated guidance before promotion. Do not imply Tamil/Telugu support from a generic OCR claim.

Android backup behavior differs by OS and transfer mode; excluding sensitive data requires explicit policies and tests [T2]. Share intents and picker access allow user-selected content without reading the inbox [T3]. App-owned storage and the Keystore support the proposed vault, with lost-key and compromised-device limits [T4]. No public government submission or bank-recovery API was established in this research.

## Source register

All links checked/reviewed on 2026-11-25; dates below are publication dates when confirmed. Search-index evidence is labeled. Recheck reporting links before each release; review guidance at least monthly while actively maintained.

- **R1 — Official, 2024-10-24, opened:** [CERT-In CIAD-2024-0050](https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2024-0050&pageid=PUBVLNOTES02). Scam patterns and prevention.
- **R2 — Official, 2024-02-02, opened:** [RBI KYC fraud warning](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=57244). Bank confirmation, credential protection, prompt reporting.
- **R3 — Official, 2025-01-17, opened:** [RBI voice/SMS safeguards](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12770). Suspected communication versus victim reporting.
- **R4 — Official, search-index text; direct page timed out:** [NCRP FAQ](https://cybercrime.gov.in/webform/FAQ.aspx). Complaint categories and acknowledgement tracking; live interface unverified.
- **R5 — Official, 2026-03-16, opened:** [DoT/PIB Chakshu notice](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2240592&lang=2&reg=48). Expanded communication reporting, financial-loss exclusion.
- **C1 — Vendor, 2026-09-28, search-index text:** [Truecaller Scam Checker launch](https://corporate.truecaller.com/newsroom/press-release/truecaller-scam-checker-brings-together-scam-detection-and-community-intelligence?id=CF9222986F234D5B).
- **C2 — Vendor, opened:** [Truecaller ROW privacy summary](https://www.truecaller.com/privacy-summary-row).
- **C3 — Vendor, search-index text:** [Messages privacy](https://support.google.com/messages/answer/9327903) and [new Android protections](https://blog.google/security/new-android-scam-protections/).
- **C4 — Vendor, modified 2025-06-16, opened:** [Norton Genie FAQ](https://support.norton.com/sp/en/ca/norton-download-install/current/solutions/v20230717145233467).
- **C5 — Vendor, search-index text:** [Norton product privacy notice](https://asia.norton.com/privacy/products-privacy-notice).
- **C6 — Official Singapore product, search-index text:** [What is ScamShield](https://www.scamshield.gov.sg/about-scamshield/what-is-scamshield/).
- **C7 — Official Singapore product, search-index text:** [Privacy statement](https://www.scamshield.gov.sg/privacy/).
- **T1 — Platform documentation, opened:** [ML Kit Android OCR](https://developers.google.com/ml-kit/vision/text-recognition/v2/android). Pin compatible versions during #9/#32; page summary and setup differ on minimum API, so use the actual setup requirements and test.
- **T2 — Platform documentation, opened:** [Android backup security](https://developer.android.com/privacy-and-security/risks/backup-best-practices).
- **T3 — Platform documentation, verification required during #16:** [Receiving shared data](https://developer.android.com/training/sharing/receive). This link is an implementation reference, not a completed platform test.
- **T4 — Platform documentation, verification required during #55:** [Android Keystore](https://developer.android.com/privacy-and-security/keystore). Validate actual selected key policy on target devices.
