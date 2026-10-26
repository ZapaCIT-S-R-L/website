// Tests for the site Worker (src/index.js): redirects to www, archived portal URLs, static pages.
// Run: npm test (Node's built-in test runner, no dependencies).
import { test } from "node:test";
import assert from "node:assert/strict";
import worker from "../src/index.js";

// Stands in for the ASSETS binding: answers 200 with the path it was asked for.
const env = { ASSETS: { fetch: async (req) => new Response(new URL(req.url).pathname, { status: 200 }) } };
const get = (url) => worker.fetch(new Request(url), env);

const redirects = [
  ["https://zapakid.ro/en/privacy?x=1", "https://www.zapakid.ro/en/privacy?x=1", "apex keeps path and query"],
  ["https://zapakid.ro/", "https://www.zapakid.ro/", "apex root"],
  ["https://www.zapakid.ro/app/kid", "https://www.zapakid.ro/", "archived /app portal"],
  ["https://www.zapakid.ro/api/v1/health", "https://www.zapakid.ro/", "archived /api"],
  ["https://www.zapakid.ro/db", "https://www.zapakid.ro/", "archived /db"],
  ["https://www.zapakid.ro/pricing", "https://www.zapakid.ro/", "old pricing page"],
  ["https://www.zapakid.ro/de/terms.html", "https://www.zapakid.ro/de/", "old German terms page"],
  ["https://www.zapakid.ro/en/cookies", "https://www.zapakid.ro/en/", "old English cookies page"],
];

for (const [from, to, why] of redirects) {
  test(`301 ${from} -> ${to} (${why})`, async () => {
    const res = await get(from);
    assert.equal(res.status, 301);
    assert.equal(res.headers.get("location"), to);
  });
}

// The exact values are checked end to end in test/e2e/headers.test.js; here: every kind of response has them.
const securityHeaders = [
  "content-security-policy",
  "x-frame-options",
  "x-content-type-options",
  "referrer-policy",
  "cross-origin-opener-policy",
  "permissions-policy",
];
for (const url of ["https://www.zapakid.ro/", "https://zapakid.ro/en/", "https://www.zapakid.ro/pricing"]) {
  test(`security headers on ${url}`, async () => {
    const res = await get(url);
    for (const name of securityHeaders) assert.ok(res.headers.get(name), name);
  });
}

for (const path of ["/", "/en/", "/de/contact", "/privacy", "/application", "/apiary"]) {
  test(`www${path} is served from the static assets`, async () => {
    const res = await get(`https://www.zapakid.ro${path}`);
    assert.equal(res.status, 200);
    assert.equal(await res.text(), path);
  });
}

// Footer version: pages carry __VERSION__ / __VERSION_URL__ placeholders, the Worker fills them from env.
const page = '<footer><a href="__VERSION_URL__">__VERSION__</a></footer>';
const htmlEnv = (vars) => ({
  ...vars,
  ASSETS: { fetch: async () => new Response(page, { headers: { "content-type": "text/html; charset=utf-8" } }) },
});

test("the footer shows the deployed version and links to its changes", async () => {
  const url = "https://github.com/ZapaCIT-S-R-L/website/compare/v1.0.4...v1.0.5";
  const res = await worker.fetch(
    new Request("https://www.zapakid.ro/"),
    htmlEnv({ VERSION: "v1.0.5", VERSION_URL: url }),
  );
  assert.equal(await res.text(), `<footer><a href="${url}">v1.0.5</a></footer>`);
});

test("without a deployed version the footer says dev and links to the repo", async () => {
  const res = await worker.fetch(new Request("https://www.zapakid.ro/"), htmlEnv({}));
  assert.equal(await res.text(), '<footer><a href="https://github.com/ZapaCIT-S-R-L/website">dev</a></footer>');
});

test("non-HTML responses are passed through untouched", async () => {
  const css = "a::after { content: '__VERSION__'; }";
  const env = {
    VERSION: "v9.9.9",
    ASSETS: { fetch: async () => new Response(css, { headers: { "content-type": "text/css" } }) },
  };
  const res = await worker.fetch(new Request("https://www.zapakid.ro/site.css"), env);
  assert.equal(await res.text(), css);
});

// Sign in with Apple on Android returns to https://zapakid.ro/app/apple#code=…&state=… (an App Link, api PR #8).
// That one apex URL serves a page instead of redirecting; the fragment never reaches the server.
test("https://zapakid.ro/app/apple serves the return page, not a redirect", async () => {
  const res = await get("https://zapakid.ro/app/apple");
  assert.equal(res.status, 200);
  assert.equal(await res.text(), "/app/apple");
  assert.equal(res.headers.get("x-robots-tag"), "noindex");
  assert.equal(res.headers.get("cache-control"), "no-store");
  assert.ok(res.headers.get("content-security-policy"), "security headers still apply");
});

for (const url of ["https://zapakid.ro/app/apple/x", "https://zapakid.ro/app/other", "https://zapakid.ro/app/Apple"]) {
  test(`${url} still redirects to www`, async () => {
    assert.equal((await get(url)).status, 301);
  });
}

test("https://www.zapakid.ro/app/apple still redirects like the rest of /app", async () => {
  const res = await get("https://www.zapakid.ro/app/apple");
  assert.equal(res.status, 301);
  assert.equal(res.headers.get("location"), "https://www.zapakid.ro/");
});
