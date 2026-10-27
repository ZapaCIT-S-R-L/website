// zapakid.ro site Worker: every request comes here first (run_worker_first), then the static pages.
// zapakid.ro redirects to www; URLs of the archived portal redirect to the landing pages.
// Every response gets the security headers below (HSTS comes from the Cloudflare zone).
// HTML pages get the deployed version in the footer: deploy.yml passes VERSION and VERSION_URL.
const SITE = "https://www.zapakid.ro";
const REPO = "https://github.com/ZapaCIT-S-R-L/zapakid-website";

// The pages have no scripts, no inline styles and only same-origin images and CSS, so nothing else is allowed.
const SECURITY_HEADERS = {
  "Content-Security-Policy":
    "default-src 'none'; img-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
  "X-Frame-Options": "DENY",
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "no-referrer",
  "Cross-Origin-Opener-Policy": "same-origin",
  "Permissions-Policy":
    "accelerometer=(), browsing-topics=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()",
};

// Sign in with Apple on Android returns here (api PR #8); the app's App Link normally opens it before the page loads.
const APPLE_RETURN = "/app/apple";

function route(request, env) {
  const url = new URL(request.url);
  if (url.hostname === "zapakid.ro" && url.pathname === APPLE_RETURN) {
    return appleReturn(request, env);
  }
  if (url.hostname !== "www.zapakid.ro") {
    return Response.redirect(SITE + url.pathname + url.search, 301);
  }
  if (/^\/(app|api|db)(\/|$)/.test(url.pathname)) {
    return Response.redirect(SITE + "/", 301);
  }
  const old = url.pathname.match(/^\/((?:de|en)\/)?(?:pricing|terms|cookies)(?:\.html)?$/);
  if (old) {
    return Response.redirect(SITE + "/" + (old[1] ?? ""), 301);
  }
  return env.ASSETS.fetch(request);
}

// Serves app/apple.html, never cached or indexed (the URL fragment carries a one-time sign-in code).
async function appleReturn(request, env) {
  const res = await env.ASSETS.fetch(new Request(SITE + APPLE_RETURN, request));
  const out = new Response(res.body, res);
  out.headers.set("X-Robots-Tag", "noindex");
  out.headers.set("Cache-Control", "no-store");
  return out;
}

// Fills the footer placeholders in HTML pages; everything else passes through as is.
async function withVersion(res, env) {
  if (!(res.headers.get("content-type") ?? "").startsWith("text/html")) return res;
  const html = (await res.text())
    .replaceAll("__VERSION_URL__", env.VERSION_URL || REPO)
    .replaceAll("__VERSION__", env.VERSION || "dev");
  const out = new Response(html, res);
  out.headers.delete("etag"); // the asset's ETag no longer matches the body
  return out;
}

export default {
  async fetch(request, env) {
    const res = await withVersion(await route(request, env), env);
    // Redirect and asset responses have immutable headers: copy into a new response.
    const out = new Response(res.body, res);
    for (const [name, value] of Object.entries(SECURITY_HEADERS)) out.headers.set(name, value);
    return out;
  },
};
