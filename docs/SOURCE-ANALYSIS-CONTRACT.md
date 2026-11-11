# Source and analysis contract
Verified: 2026-11-11. Documentation verification is NOT an ingestion or full licence approval.

| Source | Use | Access/cost evidence | Limitation/status |
|---|---|---|---|
| Himalayas | Descriptions and skill mentions | Public REST; free key documented; daily cache | Existing pilot. Not representative demand. Attribution/expiry/retention restrictions; review current terms before expanding. |
| Jobicy | Remote-work descriptions | Public API/RSS documentation | Existing pilot. Keep attribution; confirm archive/removal rules before history. |
| O*NET database | Tasks, skills and occupations | Downloadable database; general content CC BY 4.0 with noted exceptions | Candidate. US occupational context, not Bangladesh demand. Credit USDOL/ETA, link licence, mark translations/adaptations. No assumption that career tools share database licence. |
| ESCO | Occupation/skill IDs and relationships | Free downloads and web-service API | Candidate. Select explicit dataset version. API software licence is distinct from data reuse rules, which still require review. No demand measurement. |
| ILOSTAT | Country/sector labour statistics | Public download, bulk and API routes | Candidate. Verify indicator, units, observation flags, frequency, country coverage and specific reuse terms before publishing. Not live vacancies. |
| WEF Future of Jobs 2025 | Employer expectations through 2030 | Public report chapters | Editorial summaries linked in product. Not a fresh rolling five-year forecast or Bangladesh time series. |
| IEA World Energy Investment 2026 | Investment indicators | Public report; CC BY 4.0 indicated | One attributed summary implemented. 2026 estimates are estimates; investment is not revenue, hiring or business profitability. |
| Lightcast Global Job Postings | Broader posting analytics | Product/API docs confirmed; credentials/contract needed | Commercial candidate only. Quote, Bangladesh coverage, allowed public aggregates and retention unverified; no purchase or signup. |

Official documentation:
- https://himalayas.app/docs/remote-jobs-api
- https://himalayas.app/terms
- https://jobicy.com/jobs-rss-feed
- https://www.onetcenter.org/database.html
- https://www.onetcenter.org/license_db.html
- https://esco.ec.europa.eu/en/use-esco/download
- https://esco.ec.europa.eu/en/use-esco/use-esco-services-api/esco-web-service-api
- https://ilostat.ilo.org/data/
- https://ilostat.ilo.org/data/bulk/
- https://www.weforum.org/publications/the-future-of-jobs-report-2025/2-jobs-outlook
- https://www.weforum.org/publications/the-future-of-jobs-report-2025/3-skills-outlook
- https://www.iea.org/topics/investment
- https://docs.lightcast.io/lightcast-api/reference/overview-global-job-postings

## Required metadata for every insight
source URL; source version; geography; source publication date; observation period; checked_at; metric; unit; denominator; coverage; fact/interpretation/scenario; method version; transformation notes; reuse status; next review.
A source can inform one layer without covering every category.
Provider pages, API field presence and downloadable files do not prove the quality/coverage needed for public claims.

## Calculation rules
- Mentions are unique per observed posting, not necessarily required skills.
- Cross-source deduplication precedes unique market counts.
- Missing value != zero. No fabricated history.
- Comparable periods need the same geography, source set, method and coverage version; equal non-overlapping durations; complete collection; deduplicated counts.
- Percentage change with zero baseline is unavailable; show absolute change only.
- New module analysis/trends.py gates comparisons but is NOT connected to the live pipeline. Current first-page samples do not qualify as complete market coverage.
- Trend results describe observed unique postings, never total vacancies or hires.
- Employer outlook, observed postings and macro investment remain separate.
- AI drafts interpretations with source provenance; it cannot create unavailable measurements.

## Implementation order
1. Add version-pinned occupation/skill mapping with a small O*NET or ESCO sample after reuse review.
2. Validate mappings against representative descriptions, including negative/optional mentions.
3. Establish permitted history and deduplication before activating trend display.
4. Add ILOSTAT country context after indicator review.
5. Evaluate paid coverage only if documented gaps justify budget.

No user credentials or payment are required for this research checkpoint. Protected preview testing remains blocked pending explicit permission for temporary share-link access; do not retry or bypass that rejection.
