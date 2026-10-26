# zapakid.ro

Static landing site for the ZapaKid app: landing, contact and privacy in RO (`/`), DE (`/de/`) and EN (`/en/`).
No PHP, cookies, forms or third-party requests.

- Edit texts in `build.py`, run `python3 build.py`, commit the generated `.html` with it.
- At launch set `APP_STORE` / `GOOGLE_PLAY` in `build.py`: the "Soon" buttons become store links.
- Hosted on Cloudflare: Worker `zapakid-site` (`wrangler.jsonc`, `src/index.js`) serves the pages and redirects
  zapakid.ro / app.zapakid.ro to www and the archived portal URLs to the landing pages.
- Tests: `npm test` (the Worker's redirects, `test/worker.test.js`).

## How changes ship

1. Open a pull request. CI (`.github/workflows/ci.yml`) runs the tests, checks the pages match `build.py`
   and scans the whole history for credentials.
2. A maintainer reviews and merges it.
3. The merge to `main` deploys to Cloudflare (`.github/workflows/deploy.yml`, environment `production`).
   Never deploy from a laptop.

## License

[AGPL-3.0](LICENSE). Contributions need the CLA, see [CONTRIBUTING.md](CONTRIBUTING.md).
Security issues: see [SECURITY.md](SECURITY.md).
