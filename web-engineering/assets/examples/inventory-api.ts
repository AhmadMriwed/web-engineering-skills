import type { ListFilters } from "./list-state.js";

export type InventoryItem = Readonly<{ id: string; quantity: number }>;
type ListResponse = Readonly<{ items: InventoryItem[]; totalPages: number }>;
type Transport = (request: {
  params: ListFilters;
  signal?: AbortSignal;
}) => Promise<unknown>;

function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object";
}

function parseItem(value: unknown): InventoryItem {
  if (
    !isRecord(value) || typeof value.id !== "string" || !value.id ||
    typeof value.quantity !== "number" || !Number.isSafeInteger(value.quantity) ||
    value.quantity < 0
  ) {
    throw new Error("Invalid inventory item");
  }
  return { id: value.id, quantity: value.quantity };
}

function parseList(value: unknown): ListResponse {
  if (
    !isRecord(value) || !Array.isArray(value.items) ||
    typeof value.totalPages !== "number" || !Number.isSafeInteger(value.totalPages) ||
    value.totalPages < 0
  ) {
    throw new Error("Invalid inventory list");
  }
  return { items: value.items.map(parseItem), totalPages: value.totalPages };
}

export function inventoryListKey(scope: string, filters: ListFilters) {
  return ["inventory", scope, "list", filters.search, filters.page] as const;
}

export function createInventoryService(transport: Transport) {
  return {
    async list(params: ListFilters, signal?: AbortSignal): Promise<ListResponse> {
      return parseList(await transport({ params, signal }));
    },
  };
}
