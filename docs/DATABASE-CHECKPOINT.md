# Database checkpoint — 2026-10-30

Dedicated project: career-intelligence-bd. Remote migration initial_readonly_probe_dashboard applied successfully (20261030103126).

Created data_sources, collection_runs and dashboard_snapshots. All have RLS enabled. anon/authenticated can only SELECT public-visible sources and published snapshots; cannot INSERT, UPDATE or DELETE. collection_runs has no client grants or policies (intentional deny by default).

Seeded two source reference rows and one published aggregate probe snapshot: 20 records per source, checked at 2026-10-30T10:00:49.544485+00:00. No raw job descriptions stored. Historical data retention remains unresolved; collection automation is not active.

Verification: actual public REST read using frontend loader returned two sources/40 observations. Transactional test added an unpublished snapshot, switched to anon, observed one published row and zero unpublished rows, and rolled back test data. Catalog checks confirmed public writes are not granted. Security advisors reported one INFO notice for collection_runs having no policy, expected for a client-inaccessible table; no warning/error was returned.

Client config contains only a publishable key, not service_role or database credentials. Database failure yields an error/empty state; the application does not silently substitute old bundled data. Last checked timestamp remains visible. Browser integration QA, CORS behavior, deployment, full ingestion schema, skill taxonomy and scheduling are pending.
