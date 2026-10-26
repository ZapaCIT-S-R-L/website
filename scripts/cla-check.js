// CLA check: a pull request can merge only when its author has signed the CLA (CLA.md) by adding a row
// `| @username | Name | Date | CLA version |` to CLA-SIGNATURES.md. Org owners and members, and bots, don't sign.
// CLI (used by .github/workflows/ci.yml): PR_AUTHOR=... PR_ASSOCIATION=... node scripts/cla-check.js
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const NO_SIGNATURE_NEEDED = new Set(["OWNER", "MEMBER"]);

export function hasSigned(login, association, signatures) {
  if (NO_SIGNATURE_NEEDED.has(association) || login.endsWith("[bot]")) return true;
  const signed = signatures
    .split("\n")
    .map((line) => line.match(/^\|\s*@([A-Za-z0-9-_]+)\s*\|/))
    .filter(Boolean)
    .map((m) => m[1].toLowerCase());
  return signed.includes(login.toLowerCase());
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const login = process.env.PR_AUTHOR ?? "";
  const signatures = readFileSync(new URL("../CLA-SIGNATURES.md", import.meta.url), "utf8");
  if (hasSigned(login, process.env.PR_ASSOCIATION ?? "NONE", signatures)) {
    console.log(`CLA: @${login} is covered.`);
  } else {
    console.error(
      `CLA: @${login} hasn't signed yet. Read CLA.md, then add this row to CLA-SIGNATURES.md in this pull request:\n` +
        `| @${login} | Your name | ${new Date().toISOString().slice(0, 10)} | 1 |`,
    );
    process.exit(1);
  }
}
