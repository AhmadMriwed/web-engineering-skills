create schema if not exists private;
create table public.workspaces (
  id uuid primary key,
  name text not null
);
create table private.members (
  workspace_id uuid references public.workspaces on delete cascade,
  user_id uuid references auth.users on delete cascade,
  is_admin boolean not null default false,
  primary key (workspace_id, user_id)
);
create table public.notes (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces on delete cascade,
  owner_id uuid not null default auth.uid() references auth.users on delete cascade,
  title text not null check (length(btrim(title)) between 1 and 120),
  created_at timestamptz not null default now()
);
create index notes_workspace_recent on public.notes (workspace_id, created_at desc, id desc);
create index notes_owner on public.notes (owner_id);

alter table private.members enable row level security;
alter table public.workspaces enable row level security;
alter table public.notes enable row level security;
revoke all on schema private from public;
grant usage on schema private to authenticated;
revoke all on public.workspaces, public.notes from public, anon, authenticated;
grant select, insert, delete on public.notes to authenticated;
grant update (title) on public.notes to authenticated;

create function private.is_member(target uuid, require_admin boolean default false)
returns boolean language sql stable security definer set search_path = ''
as $$
  select exists (
    select 1 from private.members
    where workspace_id = target and user_id = (select auth.uid())
      and (not require_admin or is_admin)
  )
$$;
revoke all on function private.is_member(uuid, boolean) from public, anon;
grant execute on function private.is_member(uuid, boolean) to authenticated;

create policy notes_read on public.notes for select to authenticated
using (private.is_member(workspace_id) and (owner_id = (select auth.uid()) or private.is_member(workspace_id, true)));
create policy notes_create on public.notes for insert to authenticated
with check (private.is_member(workspace_id) and owner_id = (select auth.uid()));
create policy notes_update on public.notes for update to authenticated
using (private.is_member(workspace_id) and owner_id = (select auth.uid()))
with check (private.is_member(workspace_id) and owner_id = (select auth.uid()));
create policy notes_delete on public.notes for delete to authenticated
using (private.is_member(workspace_id) and owner_id = (select auth.uid()));

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('note-files', 'note-files', false, 1048576, array['text/plain']);

create policy note_files_read on storage.objects for select to authenticated
using (bucket_id = 'note-files' and (storage.foldername(name))[1] = (select auth.uid())::text);
create policy note_files_create on storage.objects for insert to authenticated
with check (bucket_id = 'note-files' and (storage.foldername(name))[1] = (select auth.uid())::text);
create policy note_files_delete on storage.objects for delete to authenticated
using (bucket_id = 'note-files' and (storage.foldername(name))[1] = (select auth.uid())::text);

create function public.rename_note(note_id uuid, new_title text)
returns boolean language sql security invoker set search_path = ''
as $$
  with changed as (
    update public.notes set title = new_title where id = note_id returning id
  )
  select exists (select 1 from changed)
$$;
revoke all on function public.rename_note(uuid, text) from public, anon;
grant execute on function public.rename_note(uuid, text) to authenticated;
