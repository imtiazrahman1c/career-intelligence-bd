# Collection runbook

Run all offline checks from repository root:

    bash tests/run_checks.sh

Collect aggregate counts only:

    python -m collectors.refresh_snapshot --output /tmp/career-snapshot.json

Collect counts and minimal attributed job display metadata:

    python -m collectors.refresh_snapshot --include-listings --output /tmp/career-snapshot.json

Both sources must succeed before the output file is atomically replaced. Counts, analysis version, timestamp, source IDs and listing link hosts are validated. Additional listing fields such as job descriptions are rejected. The collector does not publish to Supabase, use database credentials or schedule itself. The manual GitHub workflow collects aggregates only into an ephemeral runner file.

## Current delivery status

Implemented: database-connected aggregate overview; source filter; experimental skill mentions and career vocabulary filter; attributed job sample with title/company search and location-signal filter; four source-checked AI tool entries; two-platform guide; deep links and Back/Forward navigation; Hind Siliguri typography; freshness messages; CI offline checks.

Not complete: scheduled database publication, job-availability status checks, cross-source deduplication, representative Bangladesh labour-market data, extraction accuracy evaluation with human labels, authoritative taxonomy mapping, comparable historical trend analysis, mobile browser verification, submission report and production release.

## Before publishing a new listing snapshot

Review source conditions and attribution. Inspect only minimal metadata, retain original source links, and validate all tests. Publish via a trusted server-side process; never grant public writes or place a database secret in the dashboard. Verify the published payload through the public read path and test search in a browser. Current UI hides listings after 24 hours; this is a freshness rule, not proof that a vacancy is open. No provider's full job description is retained.

## Source references checked 2026-10-30

- https://himalayas.app/docs/remote-jobs-api
- https://himalayas.app/terms
- https://jobicy.com/jobs-rss-feed

Availability is not rechecked by the current display-metadata collector. Bangladesh eligibility remains unverified. Do not publish these sample counts as market demand.

## Jobicy availability check

    python -m collectors.refresh_snapshot --include-listings --check-availability --output /tmp/career-snapshot.json

Uses one bounded Jobicy batch-status request. Closed records are removed. Active means active at collection time, not guaranteed active when a user clicks. Missing, duplicate, malformed or failed status results remain unknown. Himalayas uses at most 20 individual API checks, with four requests in flight and no retries; HTTP 410 means closed, other failures remain unknown. No database publication occurs automatically. Dashboard labels distinguish active-at-collection from unknown; neither guarantees availability when applying.
