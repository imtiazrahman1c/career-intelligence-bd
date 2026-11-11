# Skill mention extraction v2

11 November 2026

Method identifier: editorial-mentions-v2. Existing saved snapshots remain unchanged; subsequent collection runs import the new identifier.

Changes:
- Inline tags no longer split words such as Py<strong>thon</strong>.
- Block boundaries still separate words.
- Explicit HTML hidden subtrees and template/script/style content are excluded.
- Self-closing hidden tags do not hide the rest of the description.
- NFKC normalization supports compatibility forms and consistent whitespace.

Validation: five new regression cases; 40 Python tests and all JavaScript suites passed locally.

Limitations: static HTML parsing is not a browser/CSS visibility engine. External CSS, arbitrary inline display rules, malformed HTML recovery and visual layout are not fully modeled. Mentions can be optional, negative or ambiguous; they do not prove requirements, proficiency, suitability or demand. No real-world accuracy percentage has been measured. Labels/vocabulary remain editorial.

Comparisons across v1 and v2 must not be treated as market growth. The separate comparison gate checks method_version, but that gate is not yet wired to a published historical trend feature. Reprocessing approved historical records with a common method would be necessary for a comparable series.

No database migration, production promotion or manual collection was performed for this code change.
