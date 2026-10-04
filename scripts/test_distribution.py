"""Regression checks for distribution links and Japanese prompt copy fidelity."""
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch
import build_distribution as pdf
from bs4 import BeautifulSoup


class DistributionTests(unittest.TestCase):
    def test_numbered_table_keeps_cell_markup_and_allocates_space_to_explanations(self):
        body = ('<p>Before</p><table><thead><tr><th>項番</th><th>Key</th>'
                '<th>Explanation</th></tr></thead><tbody><tr><td>1</td>'
                '<td><code>Node.js</code></td><td><strong>Read</strong> '
                '<a href="https://example.com">the official explanation</a> '
                'and compare the environment requirements before continuing.</td>'
                '</tr></tbody></table><p>After</p>')
        source = BeautifulSoup(body, 'html.parser')
        rendered = BeautifulSoup(pdf.web.format_tables(body), 'html.parser')
        self.assertEqual([c.decode_contents() for c in source.select('th,td')],
                         [c.decode_contents() for c in rendered.select('th,td')])
        self.assertEqual([p.get_text() for p in rendered.select('p')], ['Before', 'After'])
        widths = [float(c['style'][6:-1]) for c in rendered.select('col')]
        self.assertAlmostEqual(sum(widths), 100)
        self.assertLess(widths[0], widths[1])
        self.assertLess(widths[1], widths[2])
        self.assertTrue(rendered.select_one('.table-scroll[tabindex="0"]'))
        self.assertEqual(len(rendered.select('.table-number')), 2)
        pdf.web.layout_table(rendered.table, rendered)
        self.assertEqual(len(rendered.select('colgroup')), 1)

    def test_web_and_pdf_use_the_same_numbering_and_widths(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        paths = [pdf.web.SOURCE / 'app/6-mcp-playwright.md',
                 pdf.web.SOURCE / 'app/8-canvases.md']
        markup, _, _ = pdf.book_html(paths, 'test', config, 'test-ref', 'a' * 64)
        printed = BeautifulSoup(markup, 'html.parser').select('.chapter table')
        web_tables = []
        for path in paths:
            _, body = pdf.web.title_body(path)
            html = pdf.web.format_tables(pdf.web.markdown_renderer().convert(body))
            web_tables.extend(BeautifulSoup(html, 'html.parser').select('table'))
        self.assertEqual(len(web_tables), len(printed))
        for web_table, pdf_table in zip(web_tables, printed):
            self.assertEqual([c.get_text() for c in web_table.select('th,td')],
                             [c.get_text() for c in pdf_table.select('th,td')])
            self.assertEqual([c['style'] for c in web_table.select('col')],
                             [c['style'] for c in pdf_table.select('col')])
            numbers = [row.find_all('td', recursive=False)[0].get_text()
                       for row in pdf_table.select('tbody tr')]
            self.assertEqual(numbers, [str(i + 1) for i in range(len(numbers))])

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

    def test_latin_ligatures_preserve_copyable_prompt_identifiers(self):
        result = pdf.normalize_cmap(b'2 beginbfchar\n<01> <FB01>\n<02> <00660069>\nendbfchar')
        self.assertIn(b'<01> <00660069>', result)
        self.assertIn(b'<02> <00660069>', result)

    def test_renamed_chapters_link_to_original_upstream_filenames(self):
        self.assertTrue(pdf.web.reference_url('app', Path('1-prerequisites.md')).endswith('/0-prerequisites.md'))
        self.assertTrue(pdf.web.reference_url('app', Path('9-review.md')).endswith('/8-review.md'))
        self.assertTrue(pdf.web.reference_url('app', Path('README.md')).endswith('/README.md'))

    def test_books_have_embedded_images_and_resolved_links(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        for book in config['books'].values():
            paths = [pdf.web.SOURCE / p for p in book['chapters']]
            markup, titles, images = pdf.book_html(paths, book['title'], config, 'test-ref', 'a' * 64)
            soup = BeautifulSoup(markup, 'html.parser')
            self.assertEqual(len(soup.select('.chapter')), len(titles))
            self.assertEqual(len(soup.select('img')), images)
            self.assertFalse(soup.select('.chapter > a[id]:not([href])'))
            self.assertFalse(soup.select('.chapter p > a[id]:not([href])'))
            for heading in soup.select('.chapter h2, .chapter h3'):
                following = heading.find_next_sibling()
                if following and following.name in ('h3', 'h4'):
                    self.assertIn('section-lead', heading.parent.get('class', []))
            self.assertTrue(all(i['src'].startswith('data:image/') for i in soup.select('img')))
            self.assertTrue(all(a['href'].startswith(('#', 'https:', 'http:', 'mailto:')) for a in soup.select('a[href]')))
            self.assertNotIn('file://', markup)
            contents = soup.select_one('.contents')
            self.assertFalse(contents.select('ol'))
            expected_contents = [
                ('#' + heading['id'], heading.get_text(' ', strip=True))
                for chapter in soup.select('.chapter')
                for heading in chapter.select('h1[id], h2[id]')]
            credits = soup.select_one('.credits h1')
            expected_contents.append(('#' + credits['id'], credits.get_text(' ', strip=True)))
            self.assertEqual(
                [(link['href'], link.get_text(' ', strip=True)) for link in contents.select('a[href]')],
                expected_contents)
            contents_targets = {link['href'] for link in contents.select('a[href]')}
            self.assertTrue(all('#' + heading['id'] not in contents_targets for heading in soup.select('.chapter h3[id]')))
            cited = {a['href'] for a in soup.select('a[href]')}
            for path in paths:
                _, body = pdf.web.title_body(path)
                source = BeautifulSoup(pdf.web.markdown.markdown(body, extensions=['tables', 'sane_lists', 'pymdownx.superfences']), 'html.parser')
                self.assertTrue(all(a['href'] in cited for a in source.select('a[href]') if a['href'].startswith(('https:', 'http:'))))

    def test_web_index_has_separate_overview_and_matching_h2_links(self):
        destination = pdf.web.OUTPUT / 'index.html'
        soup = BeautifulSoup(pdf.web.course_index('app', destination), 'html.parser')
        self.assertFalse(soup.select('ol'))
        overview = pdf.web.SOURCE / 'app/README.md'
        self.assertEqual(soup.select_one('.course-overview a')['href'],
            pdf.web.relative(pdf.web.TARGETS[overview.resolve()], destination))
        chapters = [path for path in pdf.web.FILES['app'] if path.name != 'README.md']
        entries = soup.select('.course-chapters > li')
        self.assertEqual(len(entries), len(chapters))
        for path, entry in zip(chapters, entries):
            with self.subTest(chapter=path.name):
                title, body = pdf.web.title_body(path)
                renderer = pdf.web.markdown_renderer()
                lesson = BeautifulSoup(renderer.convert(body), 'html.parser')
                href = pdf.web.relative(pdf.web.TARGETS[path.resolve()], destination)
                self.assertEqual(entry.find('a', recursive=False)['href'], href)
                self.assertEqual(entry.find('a', recursive=False).get_text(), title)
                self.assertEqual(
                    [(a['href'], a.get_text()) for a in entry.select('.course-sections a')],
                    [(href + '#' + h['id'], h.get_text()) for h in lesson.select('h2[id]')])

    def test_app_section_numbers_are_continuous_within_each_chapter(self):
        for path in pdf.web.FILES['app']:
            _, body = pdf.web.title_body(path)
            renderer = pdf.web.markdown_renderer()
            soup = BeautifulSoup(renderer.convert(body), 'html.parser')
            if path.name == 'README.md':
                self.assertTrue(all(not re.match(r'^\d+(?:\.\d+)+\s', h.get_text()) for h in soup.select('h2, h3')))
                continue
            chapter = int(path.name.split('-', 1)[0])
            section = subsection = 0
            for heading in soup.select('h2, h3'):
                if heading.name == 'h2':
                    section += 1
                    subsection = 0
                    expected = f'{chapter}.{section}'
                else:
                    self.assertGreater(section, 0, f'{path.name}: H3 before H2')
                    subsection += 1
                    expected = f'{chapter}.{section}.{subsection}'
                with self.subTest(chapter=path.name, heading=heading.get_text()):
                    self.assertRegex(heading.get_text(), '^' + re.escape(expected) + r'\s+')
            self.assertEqual(section, 5, f'{path.name}: expected five sections with objectives in the overview')

    def test_numbered_navigation_and_resource_headings_keep_pdf_cleanup(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        path = pdf.web.SOURCE / 'app/README.md'
        title_body = pdf.web.title_body
        for cited_in_prose in [False, True]:
            with self.subTest(cited_in_prose=cited_in_prose):
                citation = '[Reference](https://example.com/reference)' if cited_in_prose else 'Main text.'
                body = ('## 0.1 はじめる\n\n[Start](https://example.com/start)\n\n'
                    '## 0.2 Main\n\n' + citation + '\n\n'
                    '## 0.3 リソース\n\n- [Reference](https://example.com/reference)\n')
                with patch.object(pdf.web, 'title_body', side_effect=lambda source:
                        ('Overview', body) if source == path else title_body(source)):
                    markup, _, _ = pdf.book_html([path], 'test', config, 'test-ref', 'a' * 64)
                soup = BeautifulSoup(markup, 'html.parser')
                chapter = soup.select_one('.chapter')
                headings = [h.get_text() for h in chapter.select('h2')]
                self.assertNotIn('0.1 はじめる', headings)
                self.assertNotIn('https://example.com/start', [a['href'] for a in chapter.select('a[href]')])
                self.assertEqual('0.3 リソース' in headings, not cited_in_prose)
                self.assertEqual(bool(chapter.select('.resource-links .resources')), not cited_in_prose)
                self.assertIn('https://example.com/reference', [a['href'] for a in chapter.select('a[href]')])

    def test_web_links_use_explicit_host_only_when_supplied(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        path = pdf.web.SOURCE / 'app/1-prerequisites.md'
        markup, _, _ = pdf.book_html([path], 'test', config, 'test-ref', 'a' * 64, 'https://example.com/workshops/')
        self.assertIn('https://example.com/workshops/app/2-install-copilot-app.html', markup)

    def test_participant_book_keeps_attribution_without_instructor_material(self):
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        rendered = {}
        for audience, book in config['books'].items():
            paths = [pdf.web.SOURCE / p for p in book['chapters']]
            markup, _, _ = pdf.book_html(paths, book['title'], config, 'test-ref', 'a' * 64)
            rendered[audience] = BeautifulSoup(markup, 'html.parser')
        participant = rendered['participant']
        cover = participant.select_one('.cover').get_text()
        self.assertIn(config['edition'], cover)
        self.assertIn(config['template_ref'], cover)
        self.assertNotIn('test-ref', cover)
        self.assertNotIn('a' * 12, cover)
        self.assertFalse(any('/material/' in a['href'] for a in participant.select('a[href]')))
        self.assertNotIn('講師向け緊急対応', participant.get_text())
        credits = participant.select_one('.credits')
        self.assertIn('https://github.com/github-samples/copilot-workshops', [a['href'] for a in credits.select('a[href]')])
        self.assertIn('Copyright', credits.get_text())
        self.assertIn('test-ref', rendered['instructor'].select_one('.cover').get_text())
        self.assertIn('a' * 12, rendered['instructor'].select_one('.cover').get_text())

    def test_shared_credits_preserve_all_sources_and_complete_mit_terms(self):
        repositories = [
            ('https://github.com/iwizsophy/dev-days-jp',
             'https://github.com/iwizsophy/dev-days-jp/blob/main/LICENSE'),
            ('https://github.com/github/dev-days',
             'https://github.com/github/dev-days/blob/84b1e89aefcc23368b2ab44fd5c133ecd9572dfc/LICENSE'),
            ('https://github.com/github-samples/copilot-workshops',
             'https://github.com/github-samples/copilot-workshops/blob/7ddcf241c1cd10b8e90c0df96f6bef81e710392a/LICENSE'),
            ('https://github.com/iwizsophy/dev-days-tailspin-template',
             'https://github.com/iwizsophy/dev-days-tailspin-template/blob/v2026.10.03/LICENSE'),
            ('https://github.com/github-samples/tailspin-toys',
             'https://github.com/github-samples/tailspin-toys/blob/bae003609c8cff0c51d92658b8d3bd89450464f1/LICENSE'),
        ]
        expected_license = '''MIT License
Copyright GitHub, Inc.
Copyright (c) 2023 GitHub
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
        source = pdf.web.SOURCE / 'credits.md'
        destination = pdf.web.OUTPUT / 'credits.html'
        self.assertEqual(pdf.web.SITE_PAGES[source], destination)
        self.assertEqual(pdf.web.TARGETS[source.resolve()], destination)
        title, body = pdf.web.title_body(source)
        web_body = pdf.web.markdown.markdown(body,
            extensions=['tables', 'sane_lists', 'pymdownx.superfences'])
        web_body = pdf.web.format_tables(pdf.web.transform_links(web_body, source, destination))
        standalone = BeautifulSoup(pdf.web.shell(title, '<article>' + web_body + '</article>', destination), 'html.parser')
        rendered = {'web': standalone.select_one('main')}
        config = json.loads(pdf.CONFIG.read_text(encoding='utf-8'))
        for audience, book in config['books'].items():
            paths = [pdf.web.SOURCE / p for p in book['chapters']]
            markup, _, _ = pdf.book_html(paths, book['title'], config, 'test-ref', 'a' * 64)
            soup = BeautifulSoup(markup, 'html.parser')
            credits = soup.select_one('.credits')
            self.assertNotIn('chapter', credits.get('class', []))
            self.assertEqual(credits.h1['id'], 'credits')
            self.assertEqual(soup.select_one('.contents a[href="#credits"]').get_text(), title)
            rendered[audience] = credits
        for audience, credits in rendered.items():
            with self.subTest(audience=audience):
                self.assertEqual(credits.h1.get_text(), title)
                rows = credits.select('table tbody tr')
                self.assertEqual(len(rows), len(repositories))
                for number, (row, expected_links) in enumerate(zip(rows, repositories), 1):
                    cells = row.find_all('td', recursive=False)
                    self.assertEqual(len(cells), 4)
                    self.assertEqual(cells[0].get_text(), str(number))
                    self.assertEqual([a['href'] for a in row.select('a[href]')], list(expected_links))
                    self.assertEqual(cells[3].get_text(), 'MIT')
                widths = [float(c['style'][6:-1]) for c in credits.select('table col')]
                self.assertAlmostEqual(sum(widths), 100)
                self.assertLess(widths[0], min(widths[1:]))
                self.assertTrue(all(a['href'].startswith('https://') for a in credits.select('a[href]')))
                licenses = credits.select('pre')
                self.assertEqual(len(licenses), 1)
                self.assertEqual(' '.join(licenses[0].get_text().split()),
                                 ' '.join(expected_license.split()))
        self.assertEqual(
            [c['style'] for c in rendered['web'].select('table col')],
            [c['style'] for c in rendered['participant'].select('table col')])
        self.assertEqual(
            [c['style'] for c in rendered['participant'].select('table col')],
            [c['style'] for c in rendered['instructor'].select('table col')])


if __name__ == '__main__':
    unittest.main()
