# Security, privacy architecture and threat model

Owner: haneeshraj14-design; storage implementation owner: Mr-MarcelluS; UI consent owner: siriramya28. Review against the [OWASP MASVS](https://mas.owasp.org/MASVS/) during #55/#65; this document is a threat model, not a security certification.

## Assets and trust boundaries

Assets: private messages/screenshots, payment references, incident notes, keys, export files, guidance integrity and user trust. Boundaries: external share sender → app; selected URI provider → decoder; UI → authenticated vault; app → recipient via export; guidance card → browser/dialer; source dependencies/CI → signed release.

Adversaries include malicious message senders, hostile Android apps/content providers, someone using an unlocked/shared phone, repository attackers and an accidentally overbroad export recipient. A rooted/compromised OS or malware with active screen control is outside reliable protection. Even strong local encryption cannot assure confidentiality while the user is viewing data on a compromised phone.

## Threats, controls and verification

| Threat | Required control | Verification / residual risk |
| --- | --- | --- |
| Forged sender or government identity | Treat content/branding as unverified; no authority claims; source-linked guidance | Synthetic impersonation and naming review; text alone cannot authenticate sender |
| Malicious intents and path traversal | Export only share receiver; never accept file paths as authority; ContentResolver streams, generated filenames, strict type/size limits | Adversarial provider, revoked grant, symlink/path and URI tests; external providers remain untrusted |
| Image decompression bomb / corrupt image | Check header and streamed byte limit; ≤20MP, bounded decode off UI thread; reject animated/unsupported formats | Oversize, malformed, mislabeled image tests; keep decoder libraries updated |
| Evidence/metadata theft | Private app storage, encrypted sensitive payloads/files, authenticated Keystore-wrapped keys, hidden recent-screen previews | Inspect raw DB/files/logs, locked-vault access tests; counts/timestamps remain metadata |
| Unauthorized local object access | Repository checks vault unlock; all components unexported except narrow share receiver; verify evidence and communication belong to requested incident | Cross-incident ID tests, exported component scan, URI grant tests. No current server IDOR surface; future API must enforce user ownership server-side |
| Payload tampering or cross-incident substitution | AES-GCM with identity/purpose AAD; immutable original digest; fail closed | Swap ciphertext/header, change tag, truncate file, invalidate key; hash is not proof of authenticity |
| Key loss / device loss | Clear warning before save; KEY_UNAVAILABLE state; deliberate delete/reset only | Device lock/biometric enrollment changes and reinstall tests; no recovery claim and no silent regeneration over existing data |
| Backup or D2D leak | Explicit cloud and device-transfer exclusions for DB/files/cache/key wrappers on old/new Android formats; no plaintext saved-instance state | Inspect backup/transfer behavior on supported OS versions; manifest flag alone is insufficient |
| Logs, notifications, analytics leak | No analytics/ad SDK, no raw exception/input logs, generic notifications only, no clipboard polling | Search build/logcat/exported diagnostics for synthetic canaries; no user content in CI artifacts |
| Unsafe export | Unlock + selection + preview + warning; generated filenames, private cache, FileProvider narrow temporary read grants; purge after 15 minutes and startup | Recipient reads selected files only; expired grants revoked and temp files removed. Recipient copies cannot be recalled |
| Persistence inconsistency | Staging journal, READY visibility, restart reconciliation, idempotent deletion | Crash injection between each save/delete step; storage-full behavior; no orphan plaintext |
| SQL injection | Room bound parameters; no concatenated SQL from content | Hostile strings in fields/query tests; no raw SQL search UI |
| False confidence / prompt injection | No LLM; literal untrusted content cannot change guidance rules; no safe verdict | Benign/adversarial/unsupported cases; urgent exposure overrides finding level |
| Supply-chain/release tampering | Pinned dependencies and CI actions, Gradle verification, minimal permissions, reviewed PRs, signed release, SBOM/license review | Clean checkout reproduction, signature/checksum verification, dependency review before release |

## Authentication and key policy

Urgent guidance and unsaved text review require no login. First durable save explains local retention and asks for device credential/biometric vault setup. Require a secure device lock for persistent evidence; if absent, allow unsaved guidance and explain setup. After backgrounding for one minute or on device lock, close vault access and clear decrypted caches. Authentication timeout/key invalidation behavior is a device-tested requirement, not assumed from a UI lock icon. Do not write plaintext keys to preferences, logs or backups. No custom PIN database or password recovery service.

Temporary export is intentionally readable to the selected recipient; this is the only deliberate evidence disclosure in MVP. Preview distinguishes redacted derivatives from selected originals and warns if originals still contain secrets. Do not silently redact or alter preserved originals. Default export includes summary/manifest; original files require selection. Guidance browser URLs never include messages, account identifiers or analytics parameters.

## Data lifecycle and retention

- Draft text/image: memory/private temporary decode only; discard on cancel, completion without save, background eviction and process restart. Never auto-save pasted content.
- Saved case: retained locally until user deletes; show storage use and offer review/removal, with no automatic evidence purge. Warn before saving actual secrets; app never requests them as structured fields.
- Limits: 20k text code points; 10MiB/20MP per image; 25 evidence items per incident and 250MiB total encrypted evidence budget initially. Reject gracefully and offer export/delete; never remove another case to make room.
- Delete: tombstone → revoke/remove wrapped incident key → remove dependent rows/files/temp exports. Retry interrupted cleanup. “Delete all” destroys vault keys then removes local data. Flash wear leveling means no claim of forensic secure erase; already exported copies remain with recipients. Deleting an incident does not remove the source screenshot from its original app or gallery.
- No developer server or telemetry retention. Source repository/test artifacts use synthetic content only. User diagnostics are an explicit minimal structured report with no private text/images.

## Future network gate

Do not add INTERNET permission, reputation lookup, LLM, cloud sync or crash collection casually. Require a new data-flow/privacy review, per-action informed opt-in, redaction preview, provider retention review, transport TLS, scoped credentials, rate/file limits, server-side ownership checks and deletion tests. URLs can contain secrets; hash/reputation queries are not automatically anonymous. SSRF/DNS rebinding/redirect defense becomes mandatory if a future server fetches URLs. Never put provider secrets into an APK.

Legal/privacy obligations for a public product require a separate current review before launch. This design does not claim DPDP compliance merely because processing is local. The naming review and understandable privacy notice are release gates, with no government affiliation implied.
