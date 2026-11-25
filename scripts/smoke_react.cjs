const assert = require("node:assert/strict");
const path = require("node:path");
const { JSDOM } = require("jsdom");
const React = require("react");

const compiled = path.resolve(process.argv[2]);
const { listView, readListFilters, writeListFilters } = require(path.join(compiled, "list-state.js"));
const { createInventoryService } = require(path.join(compiled, "inventory-api.js"));
const dom = new JSDOM('<div id="root"></div>', { url: "https://example.invalid/items" });
global.window = dom.window;
global.document = dom.window.document;
global.IS_REACT_ACT_ENVIRONMENT = true;
const { createRoot } = require("react-dom/client");
const { act, createElement: h } = React;

function Dashboard({ signedIn, rtl, snapshot, items = [] }) {
  React.useEffect(() => {
    document.documentElement.dir = rtl ? "rtl" : "ltr";
    document.documentElement.lang = rtl ? "ar" : "en";
  }, [rtl]);

  if (!signedIn) return h("main", null, h("h1", null, "Sign in"));
  const filters = readListFilters(new URLSearchParams(window.location.search));
  const view = listView(snapshot, Boolean(filters.search));
  function applyFilter(event) {
    event.preventDefault();
    const search = new FormDataForDom(event.currentTarget).get("search");
    const params = writeListFilters(new URLSearchParams(window.location.search), {
      search, page: filters.page,
    });
    window.history.replaceState(null, "", "/items?" + params);
  }
  const content = view === "ready"
    ? h("table", null, h("tbody", null, items.map(item =>
      h("tr", { key: item.id }, h("td", null, item.id), h("td", null, item.quantity)))))
    : h("p", { role: view === "initial-error" ? "alert" : "status" }, view);
  return h(React.Fragment, null,
    h("nav", { "aria-label": "Inventory" }, h("a", { href: "/items" }, "Items")),
    h("main", null,
      h("h1", null, "Inventory"),
      h("form", { onSubmit: applyFilter },
        h("label", null, "Search", h("input", { name: "search" })),
        h("button", null, "Apply")),
      content));
}

const FormDataForDom = dom.window.FormData;
const root = createRoot(document.getElementById("root"));

async function render(props) {
  await act(async () => root.render(h(Dashboard, props)));
}

async function main() {
  try {
    const signedIn = { signedIn: true, rtl: true };
    await render({ signedIn: false });
    assert.equal(document.querySelector("main h1").textContent, "Sign in");
    assert.equal(document.querySelector("nav"), null);
    await render({ ...signedIn, snapshot: { status: "pending" } });
    assert.equal(document.querySelector('[role="status"]').textContent, "loading");
    assert.equal(document.documentElement.dir, "rtl");
    assert.equal(document.documentElement.lang, "ar");

    window.history.replaceState(null, "", "/items?page=4");
    document.querySelector("input").value = "bolt";
    await act(async () => document.querySelector("form").dispatchEvent(
      new window.Event("submit", { bubbles: true, cancelable: true }),
    ));
    assert.equal(window.location.search, "?search=bolt");
    await render({ ...signedIn, snapshot: { status: "success", rowCount: 0 } });
    assert.equal(document.querySelector('[role="status"]').textContent, "no-matches");
    await render({ ...signedIn, snapshot: { status: "error", hasData: false } });
    assert.equal(document.querySelector('[role="alert"]').textContent, "initial-error");

    const service = createInventoryService(async () => ({
      items: [{ id: "bolt", quantity: 2 }], totalPages: 1,
    }));
    const { items } = await service.list(readListFilters(new URLSearchParams(window.location.search)));
    await render({ ...signedIn, items, snapshot: { status: "success", rowCount: items.length } });
    assert.equal(document.querySelector("tbody td").textContent, "bolt");
    assert.equal(document.querySelector("nav a").getAttribute("href"), "/items");
    console.log("React DOM smoke passed.");
  } finally {
    await act(async () => root.unmount());
    dom.window.close();
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
