# zapakid.ro

Static landing site for the ZapaKid app: landing, contact and privacy in RO (`/`), DE (`/de/`) and EN (`/en/`).
No PHP, cookies, forms or third-party requests.

- Edit texts in `build.py`, run `python3 build.py`, commit the generated `.html` with it.
- At launch set `APP_STORE` / `GOOGLE_PLAY` in `build.py`: the "Soon" buttons become store links.
- Hosted on Cloudflare: Worker `zapakid-site` (`wrangler.jsonc`, `src/index.js`) serves the pages and redirects
  zapakid.ro to www and the archived portal URLs to the landing pages.
- Lint: `npm run lint` (Prettier, ESLint, Ruff; `npm run format` fixes formatting). Editors pick up `.editorconfig`.
- Unit tests: `npm test` (the Worker's redirects, `test/worker.test.js`; translation parity, `test/test_build.py`).
- Accessibility: `npx playwright install chromium` once, then `BASE_URL=http://127.0.0.1:8787 npm run test:a11y`
  (axe-core, WCAG 2.2 AA, desktop and phone width).
- End-to-end tests: `npx wrangler dev --local-upstream www.zapakid.ro` in one terminal, then
  `BASE_URL=http://127.0.0.1:8787 npm run test:e2e` (`test/e2e/site.test.js`). Against the live site:
  `BASE_URL=https://www.zapakid.ro LIVE=1 npm run test:e2e`.

## How changes ship

1. Open a pull request. CI (`.github/workflows/ci.yml`) runs lint and the unit tests, checks the pages match `build.py`,
   builds the Worker (dry run), runs the end-to-end tests on a local server and scans the whole history for credentials.
2. A maintainer reviews and merges it.
3. The merge to `main` deploys to Cloudflare (`.github/workflows/deploy.yml`, environment `production`), runs the
   end-to-end tests against www.zapakid.ro and rolls back to the previous version if they fail.

## Versions

Every deploy tags the merged commit `vMAJOR.MINOR.PATCH` before it goes live (`scripts/next-version.js`), and the
Cloudflare version gets the same tag:

- no label: patch (`v1.0.4` → `v1.0.5`)
- label `minor`: a large feature (`v1.0.4` → `v1.1.0`)
- label `major`: a change that breaks compatibility with the previous version (`v1.3.7` → `v2.0.0`)

Add the label to the PR before merging it.
Never deploy from a laptop.

## License

[AGPL-3.0](LICENSE). Contributions need the CLA, see [CONTRIBUTING.md](CONTRIBUTING.md).
Security issues: see [SECURITY.md](SECURITY.md).
