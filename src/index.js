// zapakid.ro site Worker: every request comes here first (run_worker_first), then the static pages.
// zapakid.ro and app.zapakid.ro redirect to www; URLs of the archived portal redirect to the landing pages.
const SITE = "https://www.zapakid.ro";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname !== "www.zapakid.ro") {
      return Response.redirect(SITE + (url.hostname === "zapakid.ro" ? url.pathname + url.search : "/"), 301);
    }
    if (/^\/(app|api|db)(\/|$)/.test(url.pathname)) {
      return Response.redirect(SITE + "/", 301);
    }
    const old = url.pathname.match(/^\/((?:de|en)\/)?(?:pricing|terms|cookies)(?:\.html)?$/);
    if (old) {
      return Response.redirect(SITE + "/" + (old[1] ?? ""), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
