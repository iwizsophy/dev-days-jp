"""Regression checks for distribution links and Japanese prompt copy fidelity."""
import json
import unittest
import build_distribution as pdf
from bs4 import BeautifulSoup


class DistributionTests(unittest.TestCase):
    def test_shared_glyph_mapping_does_not_change_ascii_or_fullwidth(self):
        cmap = b'3 beginbfchar\n<01> <2F8F>\n<02> <2027>\n<03> <FF1A>\nendbfchar\n1 beginbfrange\n<04> <06> <0041>\nendbfrange'
        result = pdf.normalize_cmap(cmap)
        self.assertIn(b'<01> <884C>', result)  # 行 rather than the Kangxi radical
        self.assertIn(b'<02> <30FB>', result)
        self.assertIn(b'<03> <FF1A>', result)  # Preserve intentional fullwidth punctuation
        for i, c in [(4, '0041'), (5, '0042'), (6, '0043')]:
            self.assertIn(f'<{i:02X}> <{c}>'.encode(), result)

    def test_range_arrays_and_radicals(self):
        result = pdf.normalize_cmap(b'1 beginbfrange\n<01> <02> [<2F00> <65E5>]\nendbfrange')
        self.assertIn(b'<01> <4E00>', result)
        self.assertIn(b'<02> <65E5>', result)

    def test_books_have_embedded_images_and_resolved_links(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        for book in config['books'].values():
            paths = [pdf.web.SOURCE / p for p in book['chapters']]
            markup, titles, images = pdf.book_html(paths, book['title'], config, 'test-ref', 'a' * 64)
            soup = BeautifulSoup(markup, 'html.parser')
            self.assertEqual(len(soup.select('.chapter')), len(titles))
            self.assertEqual(len(soup.select('img')), images)
            self.assertTrue(all(i['src'].startswith('data:image/') for i in soup.select('img')))
            self.assertTrue(all(a['href'].startswith(('#', 'https:', 'http:', 'mailto:')) for a in soup.select('a[href]')))
            self.assertNotIn('file://', markup)

    def test_web_links_use_explicit_host_only_when_supplied(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        path = pdf.web.SOURCE / 'app/0-prerequisites.md'
        markup, _, _ = pdf.book_html([path], 'test', config, 'test-ref', 'a' * 64, 'https://example.com/workshops/')
        self.assertIn('https://example.com/workshops/app/1-install-copilot-app.html', markup)


if __name__ == '__main__':
    unittest.main()
