# Aggregate recovery runbook

## Scope
This backs up only the published dashboard aggregates readable with the existing public key. It does not back up Supabase Auth, database roles, RLS policies, server secrets, private tables, storage, or the entire Postgres project. GitHub preserves the application/schema source separately. SHA-256 detects accidental corruption; it is not an authenticity signature.

## Export and verify
From the repository root, using Node:

    node scripts/snapshot-backup.mjs export /absolute/new-file.json
    node scripts/snapshot-backup.mjs verify /absolute/new-file.json

Export refuses to replace an existing file. Neither operation prints credentials or complete payloads. Raw listing metadata is excluded. The daily GitHub Actions workflow exports the public sample and retains the artifact for 14 days. Its first scheduled execution must be checked; committing a workflow does not prove the scheduler or artifact upload ran.

## Recovery
1. Download the selected artifact from this repository's Actions run.
2. Verify it with the command above and inspect its original collection timestamp and coverage version.
3. An authorized maintainer can restore the verified aggregate payload to dashboard_snapshots, keeping the original checked_at, using a server-side write path. Do not grant anonymous writes, change timestamps to make old data look fresh, or replace a newer working snapshot without investigation.
4. Read it using the public client and run data-health. A recovered old sample should still show stale.
5. If the whole database was lost, separately restore schema/policies and server configuration from reviewed migrations and the provider backup. This aggregate file alone is insufficient.

## Rehearsal completed 11 November 2026
- Exported the real published 16:34:24 Bangladesh sample (120 observations, 2 sources).
- Parsed it again, verified its checksum and validated the restored payload locally.
- Regression tests reject corrupt envelopes and preserve analysis values.
- No destructive database rollback or full Postgres restore was performed.

## Remote artifact retrieval rehearsal
Backup workflow run 43023818595 completed successfully and uploaded artifact 13856251375 (career-public-aggregate). Downloaded it via the GitHub connector, verified the ZIP digest against GitHub's artifact metadata, extracted only career-aggregate-backup.json, then ran the backup verifier successfully. The preserved collection timestamp was 2026-11-11T10:34:24.878114+00:00. No write-back, fabricated timestamp or production rollback was performed.
