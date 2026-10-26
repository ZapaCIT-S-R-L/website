// The site describes ZapaKid v1 (end-to-end encrypted family chat) and nothing it doesn't do.
// Guards against old v0.1 claims (AI tutor, games, server-side translation) creeping back in.
import { test } from "node:test";
import assert from "node:assert/strict";

const BASE = (process.env.BASE_URL ?? "http://127.0.0.1:8787").replace(/\/$/, "");
const text = async (path) => (await (await fetch(BASE + path)).text()).replace(/<[^>]+>/g, " ");
const langs = { ro: "/", en: "/en/", de: "/de/" };
const e2e = { ro: "end-to-end", en: "end-to-end", de: "Ende-zu-Ende" };

// v0.1 features and processors that v1 doesn't have.
const gone =
  /Gemini|Vertex|AI tutor|tutore AI|KI-Tutor|robotel|Roboter-Freund|robot friend|monede|Münzen|coins|sudoku|șah|Schach|chess|traducere|Übersetzung|translat/i;

for (const [lang, base] of Object.entries(langs)) {
  for (const page of ["", "contact", "privacy"]) {
    test(`${base}${page} makes no v0.1 claims`, async () => {
      const found = (await text(base + page)).match(gone);
      assert.equal(found, null, `found "${found?.[0]}"`);
    });
  }

  test(`${base} pitches the encrypted family chat`, async () => {
    const t = await text(base);
    assert.ok(t.includes(e2e[lang]), `missing ${e2e[lang]}`);
    assert.match(t, /QR/);
  });

  test(`${base}privacy matches the v1 privacy notice (${lang})`, async () => {
    const t = await text(base + "privacy");
    for (const fact of [
      e2e[lang],
      "Cloudflare",
      "Twilio",
      "Apple",
      "Google",
      "privacy@zapakid.ro",
      "RO43395664",
      "ANSPDCP",
    ]) {
      assert.ok(t.includes(fact), `missing ${fact}`);
    }
    assert.match(t, /\b30\b/, "backup rotation (30 days)");
    assert.match(t, /\b5\b/, "consent record kept 5 years");
    assert.match(t, /\b18\b/, "parents are 18+");
  });
}
