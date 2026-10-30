# Dashboard development preview

Run from the repository root:

    python -m http.server 8000 --directory web

The buildless dashboard reads the latest published aggregate snapshot from Supabase through read-only public access. Reload re-reads the database; it does not fetch upstream jobs. Never put secret/service-role keys in web/config.mjs.

Staging deployment is READY. See docs/DEPLOYMENT-CHECKPOINT.md for verification and limits. Job search, extraction, automated collection and market trends are not implemented.

Checks:

    node tests/test_dashboard.mjs
    node tests/test_snapshot_client.mjs
    python -m unittest discover -s tests -v
