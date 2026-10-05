"""Check generated asset cleanup without touching the checked-in website."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_workshops as web


class WorkshopAssetTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.source = self.root / 'content/ja'
        self.output = self.root / 'website/ja/workshops'
        self.assets = self.output / 'assets'
        self.assets.mkdir(parents=True)
        self.image_source = self.root / 'content/_images'
        self.image_source.mkdir(parents=True)
        self.lesson = self.source / 'app/1-prerequisites.md'
        self.lesson.parent.mkdir(parents=True)
        self.lesson.write_text('# Start\n\n![Used](../../_images/used%20image.png)\n', encoding='utf-8')
        (self.image_source / 'used image.png').write_bytes(b'used')
        licenses = self.source / 'licenses'
        licenses.mkdir()
        (licenses / 'test.txt').write_text('Test license', encoding='utf-8')
        (self.output / 'workshops.css').write_text('body {}', encoding='utf-8')
        (self.root / 'website/theme-toggle.js').write_text('function toggleTheme() {}', encoding='utf-8')
        (self.root / 'website/ja/index.html').write_text('<h1>Home</h1>', encoding='utf-8')
        (self.root / 'website/ja/handson-guide.html').write_text(
            '<h1 id="switch">Guide</h1><h2 id="plans">Plans</h2>', encoding='utf-8')
        self.manual = self.root / 'website/manual.html'
        self.manual.write_text('<img src="ja/workshops/assets/manual.png?cache=1#example">', encoding='utf-8')
        (self.assets / 'manual.png').write_bytes(b'manual')
        (self.assets / 'obsolete.png').write_bytes(b'obsolete')
        (self.assets / 'obsolete.json').write_bytes(b'{}')
        self.outside = self.root / 'outside.png'
        self.outside.write_bytes(b'outside')
        files = {'app': [self.lesson], 'cli': [], 'mona-mayhem': []}
        meta = {'courses': {course: {'repository': 'example/workshop', 'commit': 'fixed',
                'source': 'content', 'license': 'test.txt', 'files': [p.name for p in lessons]}
                for course, lessons in files.items()}}
        targets = {self.lesson.resolve(): self.output / 'app/1-prerequisites.html'}
        for name, value in {'ROOT': self.root, 'SOURCE': self.source, 'OUTPUT': self.output,
                            'FILES': files, 'META': meta, 'TARGETS': targets,
                            'SUPPORT': [], 'SITE_PAGES': {}}.items():
            override = patch.object(web, name, value)
            override.start()
            self.addCleanup(override.stop)

    def build(self):
        with redirect_stdout(io.StringIO()):
            web.build()

    def website_snapshot(self):
        return {p.relative_to(self.root / 'website'): p.read_bytes()
                for p in (self.root / 'website').rglob('*') if p.is_file()}

    def test_success_prunes_only_unused_direct_assets_and_rebuild_is_deterministic(self):
        nested = self.assets / 'nested'
        nested.mkdir()
        (nested / 'untouched.png').write_bytes(b'nested')
        self.build()
        self.assertTrue((self.assets / 'used image.png').is_file())
        self.assertTrue((self.assets / 'manual.png').is_file())
        self.assertFalse((self.assets / 'obsolete.png').exists())
        self.assertFalse((self.assets / 'obsolete.json').exists())
        self.assertEqual((nested / 'untouched.png').read_bytes(), b'nested')
        self.assertEqual(self.outside.read_bytes(), b'outside')
        first = self.website_snapshot()
        self.build()
        self.assertEqual(self.website_snapshot(), first)

    def test_failed_link_verification_preserves_all_existing_assets(self):
        self.manual.write_text('<img src="missing.png">', encoding='utf-8')
        with patch.object(web, 'prune_assets') as prune:
            with self.assertRaisesRegex(ValueError, 'Missing:'):
                self.build()
            prune.assert_not_called()
        self.assertTrue((self.assets / 'obsolete.png').is_file())
        self.assertTrue((self.assets / 'obsolete.json').is_file())

    def test_render_failure_does_not_prune_assets(self):
        with patch.object(web, 'title_body', side_effect=ValueError('Invalid source')):
            with patch.object(web, 'prune_assets') as prune:
                with self.assertRaisesRegex(ValueError, 'Invalid source'):
                    self.build()
                prune.assert_not_called()
        self.assertTrue((self.assets / 'obsolete.png').is_file())

    def test_distinct_sources_with_the_same_basename_fail_before_overwrite(self):
        alternative = self.image_source / 'alternative'
        alternative.mkdir()
        (alternative / 'used image.png').write_bytes(b'different')
        self.lesson.write_text(
            '# Start\n\n![First](../../_images/used%20image.png)\n'
            '![Second](../../_images/alternative/used%20image.png)\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Conflicting asset filename:'):
            self.build()
        self.assertEqual((self.assets / 'used image.png').read_bytes(), b'used')
        self.assertTrue((self.assets / 'obsolete.png').is_file())

    def test_prune_skips_symlink_files_and_outside_resolutions(self):
        protected = self.assets / 'obsolete.png'
        redirected = self.assets / 'obsolete.json'
        original_is_symlink = Path.is_symlink
        original_resolve = Path.resolve

        def is_symlink(path):
            return path == protected or original_is_symlink(path)

        def resolve(path, *args, **kwargs):
            return self.outside if path == redirected else original_resolve(path, *args, **kwargs)

        with patch.object(Path, 'is_symlink', is_symlink), patch.object(Path, 'resolve', resolve):
            web.prune_assets({self.assets / 'manual.png'})
        self.assertTrue(protected.is_file())
        self.assertTrue(redirected.is_file())
        self.assertEqual(self.outside.read_bytes(), b'outside')

    def test_prune_skips_an_asset_directory_that_resolves_elsewhere(self):
        original_resolve = Path.resolve

        def resolve(path, *args, **kwargs):
            return self.root if path == self.assets else original_resolve(path, *args, **kwargs)

        with patch.object(Path, 'resolve', resolve):
            web.prune_assets(set())
        self.assertTrue((self.assets / 'obsolete.png').is_file())
        self.assertTrue((self.assets / 'manual.png').is_file())


if __name__ == '__main__':
    unittest.main()
