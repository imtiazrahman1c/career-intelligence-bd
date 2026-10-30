# Current-observation database design — draft

Not applied to Supabase yet. Pilot use only; do not activate indefinite raw archives.

## Proposed tables
- sources: ID, owner, docs URL, terms URL, terms_checked_at, attribution, permitted_use_status, retention_review_status, enabled.
- collection_runs: source, start/finish timestamps, HTTP status, page count, returned count, validation failures, pagination_complete, method_version. A bounded probe is never marked a complete source census.
- current_job_observations: source + source_job_id unique, title, employer, supplied source/application URL, normalized publication/expiry timestamp, observed_at, raw location restrictions, eligibility_status (unknown by default), content availability and method version. Store descriptions only after retention and expiry rules are approved; never expose raw source feeds for syndication.
- skills and skill_aliases: reviewed taxonomy, original term, canonical ID, mapping evidence/version.
- observation_skills: observed job, canonical skill, matching method, evidence and review status. An observed mention is not necessarily a requirement.
- aggregate_observations: optional future counts only after derived-data retention rights are clarified; source, scope, complete period and denominator required.

## Access
Enable RLS on exposed tables. Public clients get only approved current display data through a constrained query layer. Sources' internal review notes and collection logs are private. Writes are collector-only. No privileged database credentials in frontend code. Aggregates and derived data do not automatically escape upstream restrictions.

## Expiry
A job missing from a bounded or seven-day feed is not automatically closed. Use provider-supported status checks. Honor confirmed expiry/removal and source-specific caching rules. Do not label an old cached record as an active vacancy. Persist collection completeness separately from observed counts.

## Before migration
Inspect current dedicated project, current Supabase docs and advisory requirements. Confirm retention scope, then apply versioned migrations and verify access behavior. No personal user profiles needed for the first public read-only dashboard.
