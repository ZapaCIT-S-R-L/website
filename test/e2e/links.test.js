// Broken-link check over real HTTP: every same-site link and resource on every page must resolve.
// Links to other sites (zapacit.com, GitHub) are not fetched: CI must not depend on them.
import { test } from "node:test";
import assert from "node:assert/strict";

const BASE = (process.env.BASE_URL ?? "http://127.0.0.1:8787").replace(/\/$/, "");
const SITE = "https://www.zapakid.ro";
const pages = ["/", "/contact", "/privacy", "/en/", "/en/contact", "/en/privacy", "/de/", "/de/contact", "/de/privacy"];

// Same-site targets of href= and src=, as paths. Absolute www.zapakid.ro URLs (canonical, hreflang) count as same-site.
function targets(html) {
  const found = new Set();
  for (const [, url] of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const parsed = new URL(url, SITE); // compare origins: "https://www.zapakid.ro.evil.com" is not same-site
    if (parsed.origin === SITE) found.add(parsed.pathname + parsed.search);
  }
  return found;
}

for (const page of pages) {
  test(`every same-site link on ${page} resolves`, async () => {
    const html = await (await fetch(BASE + page)).text();
    const links = targets(html);
    assert.ok(links.size > 5, `found ${links.size} links`);
    for (const path of links) {
      const res = await fetch(BASE + path, { redirect: "manual" });
      assert.equal(res.status, 200, `${page} links to ${path}: ${res.status}`);
    }
  });
}

test("every page links to the same page in the other two languages", async () => {
  for (const page of pages) {
    const html = await (await fetch(BASE + page)).text();
    const rest = page.replace(/^\/(en|de)\//, "/");
    for (const [lang, prefix] of [
      ["ro", ""],
      ["en", "/en"],
      ["de", "/de"],
    ]) {
      const href = `${SITE}${prefix}${rest}`;
      assert.match(html, new RegExp(`<link rel="alternate" hreflang="${lang}" href="${href}">`), `${page} -> ${lang}`);
    }
  }
});
