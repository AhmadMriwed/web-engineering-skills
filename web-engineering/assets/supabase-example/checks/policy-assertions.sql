begin;
set local role authenticated;
set local request.jwt.claim.sub = '00000000-0000-0000-0000-000000000001';
do $$
begin
  if (select array_agg(title) from public.notes) is distinct from array['Studio notes'] then
    raise exception 'owner visibility';
  end if;
  if not public.rename_note((select id from public.notes where title = 'Studio notes'), 'Edited') then
    raise exception 'owner rename';
  end if;
  insert into public.notes (workspace_id, title) values ('10000000-0000-0000-0000-000000000001', 'Temporary');
  delete from public.notes where title = 'Temporary';
  if not found then raise exception 'owner delete'; end if;
  begin
    insert into public.notes (workspace_id, title) values ('10000000-0000-0000-0000-000000000002', 'Forbidden');
    raise exception 'foreign workspace insert accepted';
  exception when insufficient_privilege then null;
  end;
  begin
    insert into public.notes (workspace_id, owner_id, title) values
      ('10000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', 'Forged');
    raise exception 'forged owner accepted';
  exception when insufficient_privilege then null;
  end;
  begin
    update public.notes set owner_id = '00000000-0000-0000-0000-000000000002';
    raise exception 'owner reassignment accepted';
  exception when insufficient_privilege then null;
  end;
  begin
    insert into public.notes (workspace_id, title) values ('10000000-0000-0000-0000-000000000001', '  ');
    raise exception 'blank title accepted';
  exception when check_violation then null;
  end;
  insert into storage.objects (bucket_id, name) values ('note-files', '00000000-0000-0000-0000-000000000001/sample.txt');
  begin
    insert into storage.objects (bucket_id, name) values ('note-files', '00000000-0000-0000-0000-000000000002/sample.txt');
    raise exception 'foreign prefix accepted';
  exception when insufficient_privilege then null;
  end;
end $$;
set local request.jwt.claim.sub = '00000000-0000-0000-0000-000000000002';
do $$
begin
  if (select array_agg(title) from public.notes) is distinct from array['Edited'] then
    raise exception 'admin scope';
  end if;
  if public.rename_note((select id from public.notes where title = 'Edited'), 'Blocked') then
    raise exception 'admin took ownership of edit';
  end if;
  delete from public.notes where title = 'Edited';
  if found then raise exception 'read-only admin deleted note'; end if;
  if exists (select 1 from storage.objects where bucket_id = 'note-files') then
    raise exception 'foreign file listed';
  end if;
  delete from storage.objects where bucket_id = 'note-files';
  if found then raise exception 'foreign file deleted'; end if;
end $$;
set local request.jwt.claim.sub = '00000000-0000-0000-0000-000000000004';
do $$
begin
  if exists (select 1 from public.notes) then raise exception 'peer read'; end if;
  update public.notes set title = 'Unwanted';
  if found then raise exception 'peer update'; end if;
end $$;
set local request.jwt.claim.sub = '00000000-0000-0000-0000-000000000003';
do $$
begin
  if (select array_agg(title) from public.notes) is distinct from array['Workshop notes'] then
    raise exception 'tenant isolation';
  end if;
end $$;
reset role;
delete from private.members where user_id = '00000000-0000-0000-0000-000000000001';
set local role authenticated;
set local request.jwt.claim.sub = '00000000-0000-0000-0000-000000000001';
do $$
begin
  if exists (select 1 from public.notes) then raise exception 'revoked membership visible'; end if;
  delete from storage.objects where bucket_id = 'note-files';
  if not found then raise exception 'owner file delete'; end if;
end $$;
reset role;
set local role anon;
set local request.jwt.claim.sub = '';
do $$
begin
  begin
    perform 1 from public.notes;
    raise exception 'anonymous read';
  exception when insufficient_privilege then null;
  end;
  begin
    if exists (select 1 from storage.objects where bucket_id = 'note-files') then
      raise exception 'anonymous file read';
    end if;
  exception when insufficient_privilege then null;
  end;
  begin
    perform public.rename_note(null, 'Forbidden');
    raise exception 'anonymous RPC execution';
  exception when insufficient_privilege then null;
  end;
end $$;
rollback;
