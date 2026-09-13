"""Build Web pages and standalone PDF books from content/ja (never edit PDFs by hand)."""
from pathlib import Path
import argparse
import base64
import hashlib
import html
import json
import mimetypes
import re
import subprocess
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit

import build_workshops as web
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

ROOT = web.ROOT
CONFIG = ROOT / 'content/ja/distribution.json'


def anchor(path):
    return '-'.join(path.relative_to(web.SOURCE).with_suffix('').parts).lower()


def source_url(path, ref):
    return f'https://github.com/iwizsophy/dev-days-jp/blob/{quote(ref, safe="/")}/{path.relative_to(ROOT).as_posix()}'


def book_html(paths, label, config, ref, digest, web_base=None):
    sections, titles, expected_images = [], [], 0
    selected = {p.resolve() for p in paths}
    for path in paths:
        title, body = web.title_body(path)
        titles.append(title)
        renderer = web.markdown.Markdown(extensions=['tables', 'toc', 'sane_lists', 'pymdownx.superfences', 'pymdownx.tasklist'],
            extension_configs={'toc': {'slugify': web.slugify_unicode}})
        soup = BeautifulSoup(renderer.convert(body), 'html.parser')
        if '\u2027' in soup.get_text() or re.search('[\u2f00-\u2fdf]', soup.get_text()):
            raise ValueError('Source uses characters reserved by the Japanese PDF copy correction')
        # The overview's final Web navigation duplicates the PDF contents page.
        if path.name == 'README.md':
            for heading in list(soup.select('h2')):
                if heading.get_text() == 'はじめる':
                    sibling = heading.find_next_sibling('p')
                    if sibling: sibling.decompose()
                    heading.decompose()
        prefix = anchor(path)
        for node in soup.select('[id]'):
            node['id'] = prefix + '--' + node['id']
        for link in soup.select('a[href]'):
            url = urlsplit(link['href'])
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if target in selected:
                link['href'] = '#' + anchor(target) + ('--' + unquote(url.fragment) if url.fragment else '')
            elif target in web.TARGETS:
                if web_base:
                    link['href'] = web_base.rstrip('/') + '/' + web.TARGETS[target].relative_to(web.OUTPUT).as_posix()
                else:
                    link['href'] = source_url(target, ref)
                if url.fragment:
                    link['href'] += '#' + quote(unquote(url.fragment))
            elif target.is_file() and target.is_relative_to(ROOT):
                link['href'] = source_url(target, ref)
            else:
                raise ValueError(f'Unresolved PDF link: {path}: {link["href"]}')
        for img in list(soup.select('img')):
            image = (path.parent / unquote(img['src'])).resolve()
            if not image.is_file() or not image.is_relative_to(ROOT / 'content/_images'):
                raise ValueError(f'Missing or external image: {image}')
            data = base64.b64encode(image.read_bytes()).decode('ascii')
            img['src'] = f'data:{mimetypes.guess_type(image.name)[0]};base64,{data}'
            figure = soup.new_tag('figure')
            img.replace_with(figure)
            figure.append(img)
            caption = soup.new_tag('figcaption')
            caption.string = img.get('alt', '') + ' / ' + web.META.get('ui_captures', {}).get(image.name, '参照元の画面例。現行 UI は本文の注記を参照。')
            figure.append(caption)
            expected_images += 1
        # Figures must not stay inside paragraphs; HTML parsing would otherwise relocate them.
        for para in list(soup.select('p')):
            if para.find('figure'):
                para.name = 'div'
        sections.append(f'<section class="chapter"><h1 id="{prefix}">{html.escape(title)}</h1>{soup}</section>')
    toc = ''.join(f'<li><a href="#{anchor(p)}">{html.escape(t)}</a></li>' for p, t in zip(paths, titles))
    cfg = {k: html.escape(str(v)) for k, v in config.items()}
    web_link = (f'<a href="{html.escape(web_base.rstrip("/") + "/app/index.html", quote=True)}">Web 版を開く</a>' if web_base
        else f'<a href="{source_url(web.SOURCE / "app/README.md", ref)}">オンライン原稿（リポジトリの閲覧権限が必要）</a>。Web 版は講師が案内するローカル環境で閲覧します。')
    cover = f'''<section class="cover"><p class="eyebrow">DEV DAYS · JAPANESE WORKSHOP</p>
<h1>GitHub Copilot App</h1><p class="subtitle">{label}</p><p>操作を確かめながら、Tailspin Toys の開発を進める</p>
<div class="meta">教材版：{cfg['edition']}<br>対応テンプレート：{cfg['template_tag']}<br>原稿コミット：{html.escape(ref)}<br>原稿識別子：{digest[:12]}</div>
<p>{web_link}</p><p><a href="{cfg['template_url']}">演習コードの取得先（非公開テンプレート）</a></p>
<p class="source">非公式の独立教材です。画像は操作位置の例を含みます。確認済みの範囲は各章の注記を参照してください。プロンプトは選択・コピーできる文字で収録しています。</p></section>'''
    license_text = html.escape((web.SOURCE / 'licenses/copilot-workshops.txt').read_text(encoding='utf-8'))
    credits = f'<section class="credits"><h1 id="credits">出典とライセンス</h1><p>日本語原稿：iwizsophy/dev-days-jp / content/ja。演習本文の参照元：{html.escape(web.META["courses"]["app"]["repository"])}、固定コミット {web.META["courses"]["app"]["commit"]}。画像の出典・確認範囲は各画像の注記を参照してください。</p><pre>{license_text}</pre></section>'
    css = (ROOT / 'scripts/pdf/print.css').read_text(encoding='utf-8')
    result = f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{label} | Dev Days</title><style>{css}</style></head><body>{cover}<section class="contents"><h1 id="contents">目次</h1><p>章名を選択すると本文へ移動します。PDF のしおりから各節も開けます。</p><ol>{toc}<li><a href="#credits">出典とライセンス</a></li></ol></section>{"".join(sections)}{credits}</body></html>'
    parsed = BeautifulSoup(result, 'html.parser')
    ids = [n['id'] for n in parsed.select('[id]')]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate PDF anchor')
    for link in parsed.select('a[href^="#"]'):
        if unquote(link['href'][1:]) not in ids:
            raise ValueError(f'Broken PDF anchor: {link["href"]}')
    return result, titles, expected_images


def normalize_cmap(data):
    """Chromium can map shared Japanese glyphs to Kangxi radicals when copying text."""
    def unicode_value(value):
        text = bytes.fromhex(value).decode('utf-16-be')
        return ''.join(unicodedata.normalize('NFKC', c) if '\u2f00' <= c <= '\u2fdf' else '\u30fb' if c == '\u2027' else c for c in text).encode('utf-16-be').hex().upper()

    def chars(match):
        return re.sub(r'(<[0-9A-Fa-f]+>\s*)<([0-9A-Fa-f]+)>',
            lambda m: m[1] + '<' + unicode_value(m[2]) + '>', match[0])

    text = data.decode('ascii')
    text = re.sub(r'\d+ beginbfchar\s+.*?endbfchar', chars, text, flags=re.S)
    # Expand range mappings, because normalized radicals need not remain consecutive.
    def ranges(match):
        rows = []
        for start, end, value, array in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*(?:<([0-9A-Fa-f]+)>|\[([^\]]*)\])', match[0]):
            values = re.findall(r'<([0-9A-Fa-f]+)>', array) if array else []
            for offset, cid in enumerate(range(int(start, 16), int(end, 16) + 1)):
                dest = values[offset] if values else f'{int(value, 16) + offset:0{len(value)}X}'
                rows.append(f'<{cid:0{len(start)}X}> <{unicode_value(dest)}>')
        return '\n'.join(f'{len(rows[i:i+100])} beginbfchar\n' + '\n'.join(rows[i:i+100]) + '\nendbfchar' for i in range(0, len(rows), 100))
    return re.sub(r'\d+ beginbfrange\s+.*?endbfrange', ranges, text, flags=re.S).encode('ascii')


def fix_copy_text(path):
    writer = PdfWriter(clone_from=path)
    seen = set()
    def visit(resources):
        for font in resources.get('/Font', {}).values():
            font = font.get_object()
            cmap = font.get('/ToUnicode')
            if cmap and id(font) not in seen:
                seen.add(id(font))
                stream = DecodedStreamObject()
                stream.set_data(normalize_cmap(cmap.get_object().get_data()))
                font[NameObject('/ToUnicode')] = writer._add_object(stream)
        for obj in resources.get('/XObject', {}).values():
            obj = obj.get_object()
            if '/Resources' in obj: visit(obj['/Resources'])
    for page in writer.pages: visit(page['/Resources'])
    fixed = path.with_suffix('.fixed.pdf')
    writer.write(fixed)
    writer.close()
    fixed.replace(path)


def validate_pdf(path, titles, markup=None):
    reader = PdfReader(path)
    text = '\n'.join(p.extract_text() or '' for p in reader.pages)
    compact = re.sub(r'\s+', '', text)
    for title in titles:
        if re.sub(r'\s+', '', title) not in compact:
            raise ValueError(f'Text not selectable or missing chapter: {title}')
    if not reader.outline:
        raise ValueError('PDF bookmarks are missing')
    if '\ufffd' in text or re.search(r'file:///|[CD]:[/\\]Users[/\\]', text):
        raise ValueError('PDF contains replacement glyphs or local paths')
    links = 0
    for page in reader.pages:
        for annot in page.get('/Annots', []):
            item = annot.get_object()
            uri = str(item.get('/A', {}).get('/URI', ''))
            if uri.startswith('file:'):
                raise ValueError(f'Local filesystem link leaked into PDF: {uri}')
            links += item.get('/Subtype') == '/Link'
    if not links:
        raise ValueError('PDF links are missing')
    prompts = BeautifulSoup(markup, 'html.parser').select('.chapter pre') if markup else []
    for code in prompts:
        if re.sub(r'\s+', '', code.get_text()) not in compact:
            raise ValueError('A code/prompt block differs from the selectable PDF text')
    return {'pages': len(reader.pages), 'links': links, 'bookmarks': True, 'selectable_chapter_text': True, 'verified_code_blocks': len(prompts)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audience', choices=['participant', 'instructor', 'all'], default='all')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'output/pdf')
    parser.add_argument('--web-base-url', help='Published workshops directory URL; omit for local-only Web use')
    parser.add_argument('--node', default='node')
    parser.add_argument('--chromium', help='Optional installed Chromium/Chrome executable')
    args = parser.parse_args()
    if args.web_base_url and urlsplit(args.web_base_url).scheme not in {'https', 'http'}:
        parser.error('--web-base-url must be an http(s) URL')
    web.build()
    config = json.loads(CONFIG.read_text(encoding='utf-8'))
    # Detect a stale cover version instead of silently publishing conflicting versions.
    prerequisite = (web.SOURCE / 'app/0-prerequisites.md').read_text(encoding='utf-8')
    if config['template_tag'] not in prerequisite:
        raise ValueError('distribution.json template_tag does not match prerequisites')
    ref = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    inputs = sorted(list(web.SOURCE.rglob('*.md')) + list((ROOT / 'content/_images').glob('*')) + [CONFIG, web.SOURCE / 'sources.json', web.SOURCE / 'licenses/copilot-workshops.txt', ROOT / 'scripts/pdf/print.css', ROOT / 'scripts/pdf/print.cjs', ROOT / 'scripts/build_workshops.py', Path(__file__)])
    digest = hashlib.sha256()
    for p in inputs:
        if p.is_file():
            digest.update(p.relative_to(ROOT).as_posix().encode()); digest.update(b'\0'); digest.update(p.read_bytes())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    temp = ROOT / 'tmp/pdfs'; temp.mkdir(parents=True, exist_ok=True)
    manifest = {'edition': config['edition'], 'template_tag': config['template_tag'], 'source_commit': ref,
        'source_sha256': digest.hexdigest(), 'books': {}}
    for audience in ['participant', 'instructor']:
        if args.audience not in {'all', audience}:
            continue
        paths = [web.SOURCE / p for p in config['books'][audience]['chapters']]
        markup, titles, images = book_html(paths, config['books'][audience]['title'], config, ref, digest.hexdigest(), args.web_base_url)
        intermediate = temp / f'{audience}.html'; intermediate.write_text(markup, encoding='utf-8')
        final = args.output_dir.resolve() / f'dev-days-app-{audience}.pdf'
        staging = temp / f'{audience}.pdf'
        command = [args.node, str(ROOT / 'scripts/pdf/print.cjs'), str(intermediate), str(staging)]
        if args.chromium: command.append(args.chromium)
        subprocess.run(command, cwd=ROOT, check=True)
        fix_copy_text(staging)
        checks = validate_pdf(staging, titles, markup)
        rendered = json.loads(Path(str(staging) + '.render.json').read_text(encoding='utf-8'))
        if rendered['images'] != images: raise ValueError('Image count mismatch')
        final.write_bytes(staging.read_bytes())
        manifest['books'][audience] = {**checks, 'images': images, 'file': final.name,
            'sha256': hashlib.sha256(final.read_bytes()).hexdigest()}
        print(f'{final.name}: {checks["pages"]} pages, {images} images, {checks["links"]} links')
    (args.output_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
