// zapakid.ro site Worker: every request comes here first (run_worker_first), then the static pages.
// zapakid.ro redirects to www; URLs of the archived portal redirect to the landing pages.
// Every response gets the security headers below (HSTS comes from the Cloudflare zone).
const SITE = "https://www.zapakid.ro";

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

function route(request, env) {
  const url = new URL(request.url);
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

export default {
  async fetch(request, env) {
    const res = await route(request, env);
    // Redirect and asset responses have immutable headers: copy into a new response.
    const out = new Response(res.body, res);
    for (const [name, value] of Object.entries(SECURITY_HEADERS)) out.headers.set(name, value);
    return out;
  },
};
