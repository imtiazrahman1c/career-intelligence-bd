# Source feasibility checkpoint — 2026-10-30

## Live verification
The standard-library Python probe fetched one page of 20 records from each public source. Both returned HTTP 200. Each sample had 20 unique source IDs and non-empty titles, companies, descriptions, application links, publication fields and location fields. These are field-presence checks, not validated eligibility or quality claims. No raw job text was committed.

Himalayas also supplied categories, seniority, expiryDate, timezone restrictions and salary fields. Jobicy supplied jobIndustry, jobLevel, jobType and salary fields. Salary completeness has not been measured. Source IDs are not cross-source deduplication.

See source-probe-summary.json for the timestamp and measured counts. Reported totalCount is provider metadata, NOT collected records or evidence of market coverage. The first page is not representative of our three career families or Bangladesh.

## Usage review
- Himalayas docs: https://himalayas.app/docs/remote-jobs-api
- Himalayas API-specific terms: https://himalayas.app/terms (API users section)
- Jobicy docs and fair use: https://jobicy.com/jobs-rss-feed

Himalayas permits own-site personal/commercial integration with visible attribution, supplied applicationLink, no third-party feed redistribution, private keys and expired-job removal. This is not blanket permission for permanent raw historical archives.

Jobicy documents own-product use with attribution and supplied listing links. Public feed covers the latest seven days; absence from this window does not prove closure. Use documented status checks. Historical aggregate retention and removal implications remain to be resolved before long-term storage.

## Decision
Both are technically viable PILOT sources. Proceed with source adapters and a current-observation interface; do not publish claims of national demand or start indefinite historical retention. Missing eligibility remains unknown. No raw feed or JobPosting structured-data syndication.

## Tests
Run from repository root:

    python -m unittest discover -s tests -v
    python collectors/probe_sources.py

Four tests passed: failed-payload rejection, malformed-row rejection, empty-feed handling and duplicate/missing-field measurement. Live probe exited 0. Full ingestion, scheduled execution, cross-source deduplication, role matching and frontend are not implemented.
