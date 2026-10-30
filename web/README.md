# Dashboard scaffold

From the repository root:

    python -m http.server 8000 --directory web

Open http://localhost:8000 in a browser. This buildless milestone uses a saved aggregate probe snapshot, not a live search or database connection. The source selector changes sample totals and field-completeness panels. Snapshot reload reads the saved file; it does not poll upstream providers. Six navigation views have explicit preparation/empty states where features are not implemented.

Checks:

    node --check web/app.js
    node tests/test_dashboard.mjs
    python -m unittest discover -s tests -v

Not yet verified in a browser. Not deployed. Database schema, ingestion schedule, job search, skill counts and trend engine are pending.
