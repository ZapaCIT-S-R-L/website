# zapakid.ro

Static landing site for the ZapaKid app: landing, contact and privacy in RO (`/`), DE (`/de/`) and EN (`/en/`).
No PHP, cookies, forms or third-party requests.

- Edit texts in `build.py`, run `python3 build.py`, commit the generated `.html` with it.
- At launch set `APP_STORE` / `GOOGLE_PLAY` in `build.py`: the "Soon" buttons become store links.
- Hosted on Cloudflare: Worker `zapakid-site` (`wrangler.jsonc`, `src/index.js`) serves the pages and redirects
  zapakid.ro / app.zapakid.ro to www and the archived portal URLs to the landing pages.
  **Deploys run in Gitea** (`.gitea/workflows/deploy.yml`) on every push to `main`; never from a laptop.
  Actions settings: secret `CLOUDFLARE_API_TOKEN`, variable `CLOUDFLARE_ACCOUNT_ID`. DNS/zone: `ZapaKid.ro/infra`.
- Until the nameservers move to Cloudflare, www.zapakid.ro is still the K3s copy (`zapakid-app`).
- The previous full site (kid/parent portal, grading, Știați că, admin, question generators) is parked on
  branch `archive/site-2026-10` / tag `archive-site-2026-10-19`.
