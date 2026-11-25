import { createClient } from '@supabase/supabase-js'
import type { Database } from './database.generated'

// Call once from app composition and pass the client to its feature repositories.
export function createBrowserDatabase(url: string, publishableKey: string) {
  if (!url || !publishableKey) throw new Error('Missing browser database configuration')
  return createClient<Database>(url, publishableKey, { auth: { flowType: 'pkce' } })
}
