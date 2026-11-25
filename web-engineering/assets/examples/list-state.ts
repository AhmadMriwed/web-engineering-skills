export type ListFilters = Readonly<{ search: string; page: number }>;

function positivePage(page: number): number {
  return Number.isSafeInteger(page) && page > 0 ? page : 1;
}

export function readListFilters(params: URLSearchParams): ListFilters {
  return {
    search: (params.get("search") ?? "").trim(),
    page: positivePage(Number(params.get("page"))),
  };
}

export function writeListFilters(
  current: URLSearchParams,
  nextFilters: ListFilters,
): URLSearchParams {
  const next = new URLSearchParams(current);
  const search = nextFilters.search.trim();
  const page = search === readListFilters(current).search
    ? positivePage(nextFilters.page)
    : 1;

  if (search) next.set("search", search);
  else next.delete("search");

  if (page > 1) next.set("page", String(page));
  else next.delete("page");

  return next;
}

type Snapshot =
  | { status: "pending" }
  | { status: "error"; hasData: false }
  | { status: "success"; rowCount: number }
  | { status: "error"; hasData: true; rowCount: number };

export function listView(snapshot: Snapshot, hasFilters: boolean) {
  if (snapshot.status === "pending") return "loading";
  if (snapshot.status === "error") {
    return snapshot.hasData ? "stale-error" : "initial-error";
  }
  if (snapshot.rowCount > 0) return "ready";
  return hasFilters ? "no-matches" : "empty";
}
