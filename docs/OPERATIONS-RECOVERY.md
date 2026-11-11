# Operations and recovery — 2026-11-11

## Routine
Check latest successful publish workflow and latest published snapshot timestamp. Schedule is 11:49/23:49 Asia/Dhaka, but runner delays are possible. A successful deployment is not proof of data freshness or browser correctness.
Review editorial register: Bangladesh source availability every 7 days, learning links every 30 days, report/occupation summaries every 90 days. Review intervals are internal policy; content is not automatically reverified.
When reviewing, open the original source, check dates/coverage/cost/access, update checked date only after actual review and run checks.

## Failed collection
Inspect workflow step/log error without copying credentials. Preserve last valid snapshot. Do not replace missing records with zeros, AI estimates or unrelated sources.
Retry only a transient failure after identifying cause. Respect provider rate limits; never loop retries.
If data remains stale, keep the warning; static source-backed guides should remain available.
collection_runs is not populated by current publisher. Do not treat it as an execution audit.

## Bad published snapshot
Identify exact affected snapshot and validate a known-good one before any publication-flag change. Export/retain an authorized recovery copy before changing data. Never bulk delete history to fix one bad row.
Any change to published flags must be reviewed for its effect on the public latest-snapshot query. Verify read-back after mutation.
No restore or bad-snapshot recovery has been rehearsed; this document is a procedure, not evidence of recovery capability.

## Bad frontend release
Keep the last known-good deployment ID and corresponding Git commit. Stage and verify a fix or use the platform-supported rollback after checking its target and aliases. Avoid promoting staging to public production as a troubleshooting shortcut.
Current browser QA is blocked on protected preview access. Temporary share-link creation needs explicit user authorization after prior automatic-review rejection.

## Backup and release gates
Confirm backup availability/retention and perform a non-production restore rehearsal before claiming backup readiness. Do not assume free plan includes any particular recovery feature.
Before public launch: visual/mobile/keyboard tests, source coverage disclosure, error paths, owner review, domain/release configuration and post-release smoke test.
