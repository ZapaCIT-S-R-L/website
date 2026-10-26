// Security headers and the privacy promise ("no cookies, no third-party requests"), over real HTTP.
// Same BASE_URL / LIVE switches as site.test.js.
import { test } from "node:test";
import assert from "node:assert/strict";

const BASE = (process.env.BASE_URL ?? "http://127.0.0.1:8787").replace(/\/$/, "");
const LIVE = process.env.LIVE === "1";
const get = (path) => fetch(BASE + path, { redirect: "manual" });

const pages = ["/", "/contact", "/privacy", "/en/", "/en/contact", "/en/privacy", "/de/", "/de/contact", "/de/privacy"];

const expected = {
  "content-security-policy":
    "default-src 'none'; img-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
  "x-frame-options": "DENY",
  "x-content-type-options": "nosniff",
  "referrer-policy": "no-referrer",
  "cross-origin-opener-policy": "same-origin",
  "permissions-policy":
    "accelerometer=(), browsing-topics=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()",
};

// Every kind of response carries the headers: a page, an asset, the 404 page and a redirect.
for (const path of ["/", "/en/privacy", "/site.css", "/no-such-page", "/pricing"]) {
  test(`security headers on ${path}`, async () => {
    const res = await get(path);
    for (const [name, value] of Object.entries(expected)) {
      assert.equal(res.headers.get(name), value, name);
    }
  });
}

test("HSTS is set for a year, with subdomains", { skip: !LIVE && "live only (set by Cloudflare)" }, async () => {
  assert.match((await get("/")).headers.get("strict-transport-security") ?? "", /max-age=31536000; includeSubDomains/);
});

for (const path of pages) {
  test(`page ${path} sets no cookies and loads nothing from other sites`, async () => {
    const res = await get(path);
    assert.equal(res.headers.get("set-cookie"), null);
    const html = await res.text();
    assert.doesNotMatch(html, /<script/i, "no scripts");
    // Resources (src=, stylesheets, icons) must be same-origin; plain <a> links to other sites are fine.
    const resources = [
      ...html.matchAll(/\ssrc="([^"]*)"/g),
      ...html.matchAll(/<link[^>]*rel="(?:stylesheet|icon|apple-touch-icon)"[^>]*href="([^"]*)"/g),
    ].map((m) => m[1]);
    assert.ok(resources.length > 0, "found the page's resources");
    for (const url of resources) {
      assert.ok(url.startsWith("/") && !url.startsWith("//"), `third-party resource ${url}`);
    }
  });
}

test("the stylesheet loads nothing from other sites", async () => {
  const css = await (await get("/site.css")).text();
  for (const [, url] of css.matchAll(/url\(\s*['"]?([^'")]+)/g)) {
    assert.ok(!/^(https?:)?\/\//.test(url), `third-party url() ${url}`);
  }
  assert.doesNotMatch(css, /@import/);
});
