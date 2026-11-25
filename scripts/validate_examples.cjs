const assert = require("node:assert/strict");
const path = require("node:path");

const compiled = path.resolve(process.argv[2]);
const { readListFilters, writeListFilters, listView } = require(path.join(compiled, "list-state.js"));
const { createInventoryService, inventoryListKey } = require(path.join(compiled, "inventory-api.js"));

async function main() {
  const current = new URLSearchParams("search=old&page=4&mode=compact");
  assert.deepEqual(readListFilters(current), { search: "old", page: 4 });
  for (const page of ["-1", "2.2", "invalid", "9007199254740992"]) {
    assert.equal(readListFilters(new URLSearchParams({ page })).page, 1);
  }
  const changed = writeListFilters(current, { search: " new ", page: 4 });
  assert.equal(changed.toString(), "search=new&mode=compact");
  assert.equal(writeListFilters(current, { search: "old", page: 5 }).get("page"), "5");
  assert.equal(current.get("page"), "4");

  assert.equal(listView({ status: "pending" }, true), "loading");
  assert.equal(listView({ status: "success", rowCount: 0 }, true), "no-matches");
  assert.equal(listView({ status: "success", rowCount: 0 }, false), "empty");
  assert.equal(listView({ status: "success", rowCount: 1 }, false), "ready");
  assert.equal(listView({ status: "error", hasData: false }, false), "initial-error");
  assert.equal(listView({ status: "error", hasData: true, rowCount: 1 }, true), "stale-error");

  const filters = { search: "bolt", page: 1 };
  assert.notDeepEqual(inventoryListKey("A", filters), inventoryListKey("B", filters));
  const signal = new AbortController().signal;
  const list = { items: [{ id: "bolt", quantity: 2 }], totalPages: 1 };
  const service = createInventoryService(async (request) => {
    assert.deepEqual(request, { params: filters, signal });
    return list;
  });
  assert.deepEqual(await service.list(filters, signal), list);
  await assert.rejects(createInventoryService(async () => null).list(filters), /Invalid inventory list/);
  const invalidItem = createInventoryService(async () => ({
    items: [{ id: "bolt", quantity: -1 }],
    totalPages: 1,
  }));
  await assert.rejects(invalidItem.list(filters), /Invalid inventory item/);
  console.log("Neutral example assertions passed.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
