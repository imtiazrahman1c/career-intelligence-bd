# Career Intelligence BD dashboard

Run locally from the repository root:

    python -m http.server 8000 --directory web

The buildless dashboard reads the latest published aggregate sample from Supabase through read-only public access. Refresh re-reads that sample and does not start upstream collection. Never put secret/service-role keys in web/config.mjs.

Home has eight topic cards and detail views. Skills use experimental mentions, editorial occupation mappings and exercises. Tools and learning resources are curated. Business/outlook content cites its source and horizon. No application submission or CV collection is provided. Abroad preparation is a deferred module.

Current bounded collection: Himalayas up to 20 records; Jobicy up to 100 records, coverage version bounded-h20-j100-v2. These observations are not total vacancies, national demand or a representative global sample. Different methods or collection limits must not be read as comparable growth.

responsive-check.html is a noindex development harness for narrow iframe viewport checks. It is not a physical-device simulator and is not linked in product navigation.

Run checks:

    bash tests/run_checks.sh
    node scripts/data-health.mjs

For verified status, see docs/EXECUTION-CHECKPOINT-2026-11-11.md and docs/RECOVERY-RUNBOOK.md. READY staging is not a public release or a guarantee of production readiness.
