"""Translation parity for build.py: RO, DE and EN must have the same texts, none empty or left untranslated.

Run: python3 -m unittest discover -s test -p "test_*.py"
"""

import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("ro", "de", "en")


def build_constants():
    """Reads T, LANGS and PHONE from build.py without running it (running it writes the pages)."""
    tree = ast.parse((ROOT / "build.py").read_text())
    found = {}
    for node in tree.body:
        target = node.targets[0] if isinstance(node, ast.Assign) else None
        if isinstance(target, ast.Name) and target.id in ("T", "LANGS", "PHONE"):
            found[target.id] = ast.literal_eval(node.value)
    return found


def shape(value):
    """The structure of a text tree: dict keys, list lengths, '' for every string."""
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [shape(item) for item in value]
    return ""


def strings(value, path=""):
    """Every (path, string) in a text tree."""
    if isinstance(value, dict):
        for key, item in value.items():
            yield from strings(item, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for i, item in enumerate(value):
            yield from strings(item, f"{path}[{i}]")
    else:
        yield path, value


class TranslationParity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = build_constants()
        cls.T = cls.c["T"]

    def test_every_language_is_defined_everywhere(self):
        for name in ("T", "LANGS", "PHONE"):
            self.assertEqual(sorted(self.c[name]), sorted(LANGS), name)

    def test_languages_have_the_same_texts(self):
        for lang in ("de", "en"):
            self.assertEqual(shape(self.T[lang]), shape(self.T["ro"]), f"{lang} differs from ro")

    def test_no_empty_texts(self):
        for lang in LANGS:
            for path, text in strings(self.T[lang]):
                self.assertTrue(str(text).strip(), f"{lang}{path} is empty")

    def test_long_texts_are_translated(self):
        # A sentence that is identical in two languages was almost certainly copied, not translated.
        for lang in ("de", "en"):
            ro = dict(strings(self.T["ro"]))
            for path, text in strings(self.T[lang]):
                if isinstance(text, str) and len(text) > 40:
                    self.assertNotEqual(text, ro[path], f"{lang}{path} is the Romanian text")

    def test_html_lang_matches_the_language(self):
        for lang in LANGS:
            self.assertEqual(self.T[lang]["html_lang"], lang)


if __name__ == "__main__":
    unittest.main()
