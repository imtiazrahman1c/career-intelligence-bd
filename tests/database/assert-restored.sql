do $checks$
begin
 if (select count(*) from public.dashboard_snapshots) <> 2 then raise exception 'Admin restore row count mismatch'; end if;
 if not exists(select 1 from public.dashboard_snapshots where is_published and jsonb_array_length(payload->'results')=2) then raise exception 'Published payload did not survive restore'; end if;
 if exists(select 1 from pg_tables where schemaname='public' and tablename in ('data_sources','collection_runs','dashboard_snapshots') and not rowsecurity) then raise exception 'RLS missing'; end if;
end $checks$;
set role anon;
do $checks$
begin
 if (select count(*) from public.dashboard_snapshots) <> 1 then raise exception 'Anonymous snapshot RLS failed'; end if;
 if (select count(*) from public.data_sources) <> 1 then raise exception 'Anonymous source RLS failed'; end if;
 if has_table_privilege(current_user,'public.dashboard_snapshots','INSERT') or has_table_privilege(current_user,'public.dashboard_snapshots','UPDATE') or has_table_privilege(current_user,'public.dashboard_snapshots','DELETE') then raise exception 'Unexpected anonymous write grant'; end if;
 if has_table_privilege(current_user,'public.collection_runs','SELECT') then raise exception 'Internal logs exposed'; end if;
end $checks$;
reset role;
set role authenticated;
do $checks$
begin
 if (select count(*) from public.dashboard_snapshots) <> 1 then raise exception 'Authenticated snapshot RLS failed'; end if;
 if (select count(*) from public.data_sources) <> 1 then raise exception 'Authenticated source RLS failed'; end if;
 if has_table_privilege(current_user,'public.dashboard_snapshots','INSERT') or has_table_privilege(current_user,'public.dashboard_snapshots','UPDATE') or has_table_privilege(current_user,'public.dashboard_snapshots','DELETE') then raise exception 'Unexpected authenticated write grant'; end if;
end $checks$;
reset role;
