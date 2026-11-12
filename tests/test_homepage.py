"""Dependency-free checks for the static homepage; does not access the network."""
from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Homepage(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.links = []
        self.anchor_depth = 0
        self.nested_anchors = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == "a":
            self.nested_anchors |= self.anchor_depth > 0
            self.anchor_depth += 1
            self.links.append(attrs)

    def handle_endtag(self, tag):
        if tag == "a":
            self.anchor_depth -= 1


class HomepageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.page = Homepage(cls.html)

    def test_document_has_one_main_heading_and_unique_ids(self):
        self.assertEqual(sum(tag == "h1" for tag, _ in self.page.elements), 1)
        ids = [attrs["id"] for _, attrs in self.page.elements if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)))

    def test_fragment_links_and_accessible_labels_resolve(self):
        ids = {attrs["id"] for _, attrs in self.page.elements if "id" in attrs}
        for link in self.page.links:
            if link.get("href", "").startswith("#"):
                self.assertIn(link["href"][1:], ids)
        for _, attrs in self.page.elements:
            for target in attrs.get("aria-labelledby", "").split():
                self.assertIn(target, ids)

    def test_external_links_have_safe_new_tab_behavior(self):
        for link in self.page.links:
            if link.get("target") == "_blank":
                self.assertTrue({"noopener", "noreferrer"} & set(link.get("rel", "").split()))

    def test_no_nested_links(self):
        self.assertFalse(self.page.nested_anchors)
        self.assertEqual(self.page.anchor_depth, 0)

    def test_existing_projects_are_preserved(self):
        urls = {link.get("href") for link in self.page.links}
        for repo in ["HarnessX", "Mi-Memory", "Car-bench-TRACE",
                     "topological-collapse-agent-societies", "awesome-world-models-for-digital-agents"]:
            self.assertIn("https://github.com/Darwin-Agent/" + repo, urls)
        cards = [attrs for _, attrs in self.page.elements
                 if "project-card" in attrs.get("class", "").split()]
        self.assertEqual(len(cards), 6)

    def test_new_projects_have_verified_resource_destinations(self):
        urls = {link.get("href") for link in self.page.links}
        expected = ["https://darwin-agent.github.io/HarnessPAI/",
                    "https://arxiv.org/abs/2609.29166",
                    "https://github.com/Darwin-Agent/HarnessPAI",
                    "https://darwin-agent.github.io/WIA/",
                    "https://github.com/Darwin-Agent/WIA",
                    "https://darwin-agent.github.io/WIA/demos.html"]
        for url in expected:
            self.assertIn(url, urls)
        self.assertNotIn("https://github.com/Darwin-Agent/WIA/tree/main/paper/Tech_Report__WAM", urls)

    def test_six_research_directions_and_local_work_entry(self):
        rows = [attrs for _, attrs in self.page.elements
                if "research-row" in attrs.get("class", "").split()]
        self.assertEqual(len(rows), 6)
        hero_buttons = [link for link in self.page.links if "button-dark" in link.get("class", "").split()]
        self.assertEqual(hero_buttons[0]["href"], "#work")

    def test_local_resources_exist(self):
        for tag, attrs in self.page.elements:
            path = attrs.get("src") if tag == "script" else attrs.get("href") if tag == "link" else None
            if path and path.startswith("./"):
                self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
