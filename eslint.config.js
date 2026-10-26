// ESLint flat config: recommended rules for the Worker (src/) and the tests (test/).
import js from "@eslint/js";
import globals from "globals";

export default [
  { ignores: ["node_modules/", "dist/"] },
  js.configs.recommended,
  { files: ["src/**/*.js"], languageOptions: { globals: globals.serviceworker } },
  { files: ["test/**/*.js", "eslint.config.js"], languageOptions: { globals: globals.node } },
];
