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
  ["https://app.zapakid.ro/anything", "https://www.zapakid.ro/", "app host goes to the landing page"],
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

for (const path of ["/", "/en/", "/de/contact", "/privacy", "/application", "/apiary"]) {
  test(`www${path} is served from the static assets`, async () => {
    const res = await get(`https://www.zapakid.ro${path}`);
    assert.equal(res.status, 200);
    assert.equal(await res.text(), path);
  });
}
