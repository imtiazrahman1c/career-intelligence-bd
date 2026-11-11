# Launch verification — 2026-11-11
Scoped check, not comprehensive security certification.

Verified live pg_policies: public source SELECT requires public_visible; snapshot SELECT requires is_published. anon/authenticated have no INSERT/UPDATE/DELETE on these tables, and no access to collection_runs.
Static public web scan found no secret-key, GitHub-token or private-key patterns; this is not a full repository-history audit.
35 Python tests and all JS checks passed, including mocked-DOM offline view rendering.

Bangladesh candidates: BBS Labour Force Survey listings, NSDA competency standards and National Skills Portal. Search-index discovery succeeded, but direct reads returned 502, timeout and empty readable content respectively. No API, data import, local demand count or training endorsement is confirmed. Source status is shown in the product.

Open gates:
- Temporary protected-preview share-link access was rejected by automatic review; explicit authorization required before retry.
- Browser/mobile/keyboard/click QA incomplete.
- Representative coverage and permitted deduplicated history incomplete.
- Bangladesh time series not imported.
- Backup restoration not rehearsed.
- Editorial reports and learning links need review tracking; job snapshot automation does not update them.
- collection_runs is not populated; use workflow logs and snapshot timestamps as current evidence.
- Owner final review and public release remain pending.

Do not call the platform production-ready yet.
