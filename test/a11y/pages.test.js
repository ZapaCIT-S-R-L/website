// Accessibility: axe-core (WCAG 2.2 A + AA rules) on every page in a real headless Chromium, desktop and phone width.
// Fails on any violation. Run: BASE_URL=... npm run test:a11y (needs `npx playwright install chromium` once).
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { chromium } from "playwright";
import { AxeBuilder } from "@axe-core/playwright";

const BASE = (process.env.BASE_URL ?? "http://127.0.0.1:8787").replace(/\/$/, "");
const pages = ["/", "/contact", "/privacy", "/en/", "/en/contact", "/en/privacy", "/de/", "/de/contact", "/de/privacy"];
const viewports = { desktop: { width: 1280, height: 900 }, phone: { width: 390, height: 844 } };

let browser;
before(async () => (browser = await chromium.launch()));
after(async () => browser?.close());

for (const path of pages) {
  for (const [name, viewport] of Object.entries(viewports)) {
    test(`${path} (${name}) has no accessibility violations`, async () => {
      const context = await browser.newContext({ viewport });
      const page = await context.newPage();
      await page.goto(BASE + path);
      const { violations, passes } = await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"])
        .analyze();
      await context.close();
      const report = violations.map(
        (v) => `${v.id} (${v.impact}): ${v.help} — ${v.nodes.map((n) => n.target).join(", ")}`,
      );
      assert.ok(passes.length > 10, `axe ran only ${passes.length} passing rules`);
      assert.deepEqual(report, []);
    });
  }
}
