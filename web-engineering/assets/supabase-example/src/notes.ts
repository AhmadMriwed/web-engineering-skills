import type { SupabaseClient } from '@supabase/supabase-js'
import type { Database } from './database.generated'

export async function listNotes(client: SupabaseClient<Database>, workspaceId: string, signal: AbortSignal) {
  const { data, error } = await client.from('notes')
    .select('id,title,created_at')
    .eq('workspace_id', workspaceId)
    .order('created_at', { ascending: false })
    .order('id', { ascending: false })
    .limit(30)
    .abortSignal(signal)
  if (error) throw new Error('Could not load notes', { cause: error })
  return data
}

function validateTitle(title: string) {
  const name = title.trim()
  if (!name || [...name].length > 120) throw new RangeError('Enter a title up to 120 characters')
  return name
}

export async function addNote(client: SupabaseClient<Database>, workspaceId: string, title: string) {
  const name = validateTitle(title)
  const input: Database['public']['Tables']['notes']['Insert'] = { workspace_id: workspaceId, title: name }
  const { error } = await client.from('notes').insert(input)
  if (error) throw new Error('Could not create note', { cause: error })
}

export async function renameNote(client: SupabaseClient<Database>, noteId: string, title: string) {
  const name = validateTitle(title)
  const { data, error } = await client.rpc('rename_note', { note_id: noteId, new_title: name })
  if (error) throw new Error('Could not rename note', { cause: error })
  return data === true
}
