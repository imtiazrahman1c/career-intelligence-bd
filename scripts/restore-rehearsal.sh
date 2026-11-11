#!/usr/bin/env bash
set -euo pipefail
# Guard against accidentally running a rehearsal against a real database.
[[ "${GITHUB_ACTIONS:-}" == true ]] || { echo 'This rehearsal requires the disposable CI service.'; exit 1; }
[[ "${POSTGRES_CONTAINER:-}" =~ ^[a-f0-9]{12,64}$ ]] || { echo 'Invalid disposable service container.'; exit 1; }
work="${RUNNER_TEMP:?}/career-restore"
mkdir -p "$work"
node scripts/snapshot-backup.mjs export "$work/aggregate.json"
node scripts/restore-fixture.mjs "$work/aggregate.json" "$work/fixture.sql"
docker exec "$POSTGRES_CONTAINER" psql -U postgres -v ON_ERROR_STOP=1 -c 'create role anon nologin; create role authenticated nologin; create role service_role nologin bypassrls;'
docker exec "$POSTGRES_CONTAINER" createdb -U postgres career_restore_source
docker exec -i "$POSTGRES_CONTAINER" psql -U postgres -d career_restore_source -v ON_ERROR_STOP=1 < supabase/migrations/20261030103126_initial_readonly_probe_dashboard.sql
docker exec -i "$POSTGRES_CONTAINER" psql -U postgres -d career_restore_source -v ON_ERROR_STOP=1 < "$work/fixture.sql"
docker exec -i "$POSTGRES_CONTAINER" psql -U postgres -d career_restore_source -v ON_ERROR_STOP=1 < tests/database/assert-restored.sql
docker exec "$POSTGRES_CONTAINER" pg_dump -U postgres --format=custom --no-owner career_restore_source > "$work/application.dump"
docker exec "$POSTGRES_CONTAINER" createdb -U postgres career_restore_target
docker exec -i "$POSTGRES_CONTAINER" pg_restore -U postgres --exit-on-error --no-owner -d career_restore_target < "$work/application.dump"
docker exec -i "$POSTGRES_CONTAINER" psql -U postgres -d career_restore_target -v ON_ERROR_STOP=1 < tests/database/assert-restored.sql
echo 'PASS application schema, aggregate payload, restored RLS and read-only grants in a second disposable PostgreSQL database.'
