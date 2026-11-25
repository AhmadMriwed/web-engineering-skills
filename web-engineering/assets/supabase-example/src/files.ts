import type { SupabaseClient } from '@supabase/supabase-js'
import type { Database } from './database.generated'

export async function uploadTextFile(client: SupabaseClient<Database>, file: File) {
  if (file.size > 1024 * 1024 || file.type !== 'text/plain') throw new TypeError('Choose a text file up to 1 MiB')
  const { data, error } = await client.auth.getUser()
  if (error || !data.user) throw new Error('Sign in before uploading')
  const path = data.user.id + '/' + crypto.randomUUID() + '.txt'
  const { error: uploadError } = await client.storage.from('note-files').upload(path, file, { upsert: false })
  if (uploadError) throw new Error('Upload failed', { cause: uploadError })
  return path
}
