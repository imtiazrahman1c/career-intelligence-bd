create table public.data_sources (
 source_key text primary key check (source_key in ('himalayas','jobicy')),
 display_name text not null,
 documentation_url text not null check (documentation_url like 'https://%'),
 access_status text not null default 'pilot',
 retention_status text not null default 'review_pending',
 public_visible boolean not null default false
);
create table public.collection_runs (
 id uuid primary key default gen_random_uuid(),
 source_key text not null references public.data_sources(source_key),
 started_at timestamptz not null default now(),
 completed_at timestamptz,
 status text not null check (status in ('running','success','failed')),
 sample_count integer check (sample_count >= 0),
 pagination_complete boolean not null default false,
 method_version text not null default 'probe-v1'
);
create table public.dashboard_snapshots (
 id uuid primary key default gen_random_uuid(),
 checked_at timestamptz not null unique,
 payload jsonb not null check (jsonb_typeof(payload) = 'object' and jsonb_typeof(payload->'results') = 'array'),
 is_published boolean not null default false,
 created_at timestamptz not null default now()
);
create index dashboard_snapshots_published_time_idx on public.dashboard_snapshots(checked_at desc) where is_published;
create index collection_runs_source_time_idx on public.collection_runs(source_key,started_at desc);
alter table public.data_sources enable row level security;
alter table public.collection_runs enable row level security;
alter table public.dashboard_snapshots enable row level security;
revoke all on public.data_sources, public.collection_runs, public.dashboard_snapshots from anon, authenticated;
grant select on public.data_sources, public.dashboard_snapshots to anon, authenticated;
grant all on public.data_sources, public.collection_runs, public.dashboard_snapshots to service_role;
create policy sources_public_read on public.data_sources for select to anon, authenticated using (public_visible);
create policy snapshots_published_read on public.dashboard_snapshots for select to anon, authenticated using (is_published);
comment on table public.dashboard_snapshots is 'Aggregate feasibility metadata only; no raw job content or eligibility claims.';
