# Experimental analysis checkpoint — 2026-10-30

Implemented editorial-mentions-v1: 14 skill IDs grouped into three editorial career exploration paths. This is a small provisional vocabulary, not an official taxonomy or validated recommendation system.

Run: python collectors/probe_sources.py --analyze

Raw job descriptions are processed in memory only. Output contains aggregate counts, not text or job identities. Each source ID counts once; missing IDs are excluded. Duplicate conflicting rows use the first occurrence. Cross-source deduplication remains pending.

Skill mentions include optional and negated phrases; never label these counts as requirements, demand or career suitability. HTML scripts/styles are excluded and matching uses word boundaries. Extraction accuracy has not been evaluated against human-labelled real descriptions.

Location output only recognises explicit Bangladesh/BD or worldwide/anywhere/global structured tokens. All other values remain unknown, including empty restrictions, Remote, APAC and US-only. Recognised values still require human review of work authorisation, timezone and employer restrictions. It does not infer rejection or verified eligibility.

Live bounded probe succeeded for 20 records per source. Himalayas: SQL 2, Python 3; Jobicy: SQL 1, Python 3. These are separate convenience samples, not population estimates. Location signals: 39 unknown, 1 worldwide requiring review. See analysis-probe-summary.json for full aggregate output.

Validation: 12 Python tests passed, including source errors, deduplication, missing IDs, word boundaries, HTML, repeated mentions and uncertain location handling.

Not connected to the published dashboard or database yet. Next: review extraction against a human-labelled sample, adopt an authoritative taxonomy mapping, then publish labelled experimental aggregates. No claim of completed job filtering or verified Bangladesh eligibility.
