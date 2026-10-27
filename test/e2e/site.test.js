// End-to-end tests over real HTTP, against a running site.
//   CI, before merge:  BASE_URL=http://127.0.0.1:8787 (wrangler dev --local-upstream www.zapakid.ro)
//   after each deploy: BASE_URL=https://www.zapakid.ro LIVE=1 (adds the apex and HTTPS checks)
// Run: BASE_URL=... npm run test:e2e
import { test } from "node:test";
import assert from "node:assert/strict";

const BASE = (process.env.BASE_URL ?? "http://127.0.0.1:8787").replace(/\/$/, "");
const LIVE = process.env.LIVE === "1";
const get = (path, base = BASE) => fetch(base + path, { redirect: "manual" });
// Locally the Location header points at the dev server, live at www: compare path and query only.
const target = (res) => {
  const u = new URL(res.headers.get("location"));
  return u.pathname + u.search;
};

const pages = ["/", "/contact", "/privacy", "/en/", "/en/contact", "/en/privacy", "/de/", "/de/contact", "/de/privacy"];
for (const path of pages) {
  test(`page ${path} is served as HTML`, async () => {
    const res = await get(path);
    assert.equal(res.status, 200);
    assert.match(res.headers.get("content-type"), /text\/html/);
    assert.match(await res.text(), /ZapaKid/);
  });
}

for (const path of ["/favicon.png", "/apple-touch-icon.png", "/site.css", "/robots.txt", "/img/robot.jpg"]) {
  test(`asset ${path} is served`, async () => {
    assert.equal((await get(path)).status, 200);
  });
}

test("unknown page returns the 404 page", async () => {
  const res = await get("/no-such-page");
  assert.equal(res.status, 404);
  assert.match(await res.text(), /ZapaKid/);
});

// Public repo, public site: source, config and tooling must never be served as assets.
const privateFiles = [
  "/build.py",
  "/package.json",
  "/package-lock.json",
  "/wrangler.jsonc",
  "/src/index.js",
  "/README.md",
  "/LICENSE",
  "/SECURITY.md",
  "/CONTRIBUTING.md",
  "/.assetsignore",
  "/.gitignore",
  "/.github/workflows/deploy.yml",
  "/test/worker.test.js",
  "/test/e2e/site.test.js",
];
for (const path of privateFiles) {
  test(`repo file ${path} is not served`, async () => {
    assert.equal((await get(path)).status, 404);
  });
}

for (const [from, to] of [
  ["/pricing", "/"],
  ["/de/terms.html", "/de/"],
  ["/en/cookies", "/en/"],
  ["/app/kid", "/"],
  ["/api/v1/x", "/"],
]) {
  test(`old URL ${from} redirects to ${to}`, async () => {
    const res = await get(from);
    assert.equal(res.status, 301);
    assert.equal(target(res), to);
  });
}

test("apex zapakid.ro redirects to www, keeping the path", { skip: !LIVE && "live only" }, async () => {
  const res = await get("/en/privacy?x=1", "https://zapakid.ro");
  assert.equal(res.status, 301);
  assert.equal(res.headers.get("location"), "https://www.zapakid.ro/en/privacy?x=1");
});

test("plain HTTP is upgraded to HTTPS", { skip: !LIVE && "live only" }, async () => {
  const res = await get("/", "http://www.zapakid.ro");
  assert.ok([301, 308].includes(res.status), `status ${res.status}`);
  assert.match(res.headers.get("location"), /^https:\/\/www\.zapakid\.ro\//);
});

const REPO = "https://github.com/ZapaCIT-S-R-L/zapakid-website";
for (const [path, home] of [
  ["/", "/"],
  ["/en/contact", "/en/"],
  ["/de/privacy", "/de/"],
]) {
  test(`footer on ${path}: ZapaKid @ version | Contact | Privacy | hello@zapakid.ro`, async () => {
    const html = await (await get(path)).text();
    const footer = html.match(/<footer>([\s\S]*?)<\/footer>/)[1];
    assert.match(
      footer,
      new RegExp(
        `^\\s*<span class="brand"><a href="${home}">ZapaKid</a> @ <a class="version" href="([^"]+)">([^<]+)</a></span>`,
      ),
    );
    const [, href, version] = footer.match(/class="version" href="([^"]+)">([^<]+)</);
    if (LIVE) {
      assert.match(version, /^v\d+\.\d+\.\d+$/);
      assert.ok(
        href === `${REPO}/tree/${version}` || href.match(new RegExp(`^${REPO}/compare/v[\\d.]+\\.\\.\\.${version}$`)),
        href,
      );
    } else {
      assert.equal(version, "dev");
      assert.equal(href, REPO);
    }
    assert.match(footer, new RegExp(`<a href="${home}contact">[^<]+</a><a href="${home}privacy">[^<]+</a>`));
    assert.match(footer, /<a href="mailto:hello@zapakid\.ro">hello@zapakid\.ro<\/a>/);
    assert.doesNotMatch(html, /__VERSION/);
  });
}

test("no page mentions the old contact@ address", async () => {
  for (const path of pages) assert.doesNotMatch(await (await get(path)).text(), /contact@zapakid\.ro/, path);
});

test("the Apple return page on the apex answers 200, noindex", { skip: !LIVE && "live only (apex host)" }, async () => {
  const res = await get("/app/apple", "https://zapakid.ro");
  assert.equal(res.status, 200);
  assert.equal(res.headers.get("x-robots-tag"), "noindex");
  assert.match(await res.text(), /ZapaKid/);
});
