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


def heading_label(text):
    """Ignore chapter.section numbering when recognizing special sections."""
    return re.sub(r'^\d+(?:\.\d+)+\.?\s+', '', text.strip())


def keep_explanations_with_examples(soup, path, prefix, figures):
    """Keep three reviewed examples with their short interpretation in the PDF."""
    def example_after(heading, name):
        if heading:
            for node in heading.next_siblings:
                if getattr(node, 'name', None) in ('h2', 'h3', 'h4'):
                    break
                if getattr(node, 'name', None) == name:
                    return node
                if getattr(node, 'name', None):
                    example = node.find(name)
                    if example:
                        return example

    def block(node):
        while node.parent is not soup:
            node = node.parent
        return node

    def group(nodes):
        if not nodes or any(node.parent is not nodes[0].parent for node in nodes):
            return
        container = soup.new_tag('div', attrs={'class': 'reading-group'})
        nodes[0].insert_before(container)
        for node in nodes:
            container.append(node.extract())

    if path.name == '4-custom-instructions.md':
        target = soup.find(id=prefix + '--指示に関する-issue-から開始する')
        heading = target.find_parent(['h2', 'h3', 'h4']) if target else None
        prompt = example_after(heading, 'pre')
        if prompt:
            start = block(prompt)
            nodes = [start]
            following = start.find_next_sibling()
            while following and following.name == 'p' and len(nodes) < 3:
                nodes.append(following)
                following = following.find_next_sibling()
            if len(nodes) == 3:
                group(nodes)
    elif path.name == '5-build-filtering.md':
        target = soup.find(id=prefix + '--quality-checks-スキルを確認する')
        heading = target.find_parent(['h2', 'h3', 'h4']) if target else None
        table = example_after(heading, 'table')
        if table:
            start = block(table)
            following = start.find_next_sibling()
            if following and following.name == 'p':
                group([start, following])
    elif path.name == '8-canvases.md':
        figure = figures.get('app-20261004-07-search-plan-review.jpg')
        if figure:
            start = block(figure)
            following = start.find_next_sibling()
            if following and following.name == 'p':
                group([start, following])


def book_html(paths, label, config, ref, digest, web_base=None):
    sections, titles, contents, expected_images = [], [], [], 0
    selected = {p.resolve() for p in paths}
    for path in paths:
        title, body = web.title_body(path)
        titles.append(title)
        renderer = web.markdown_renderer()
        soup = BeautifulSoup(renderer.convert(body), 'html.parser')
        for para in list(soup.select('p')):
            children = para.find_all(recursive=False)
            if not para.get_text(strip=True) and len(children) == 1 and children[0].name == 'a' and children[0].has_attr('id') and not children[0].has_attr('href'):
                para.unwrap()
        # Keep legacy link destinations without inserting boxes between headings.
        # A separate empty anchor can defeat Chromium's heading keep-with-next.
        for legacy in list(soup.select('a[id]:not([href])')):
            heading = legacy.find_next_sibling(['h2', 'h3', 'h4', 'p', 'ul', 'ol', 'div'])
            if not heading and legacy.parent.name == 'p':
                heading = legacy.parent.find_next_sibling()
            if not legacy.get_text(strip=True) and heading:
                legacy.name = 'span'
                heading.insert(0, legacy.extract())
        for para in list(soup.select('p')):
            if not para.get_text(strip=True) and not para.find(True):
                para.decompose()
        if '\u2027' in soup.get_text() or re.search('[\u2f00-\u2fdf]', soup.get_text()):
            raise ValueError('Source uses characters reserved by the Japanese PDF copy correction')
        # The overview's final Web navigation duplicates the PDF contents page.
        if path.name == 'README.md':
            for heading in list(soup.select('h2')):
                if heading_label(heading.get_text()) == 'はじめる':
                    sibling = heading.find_next_sibling('p')
                    if sibling: sibling.decompose()
                    heading.decompose()
        for heading in soup.select('h2'):
            if heading_label(heading.get_text()) == 'リソース':
                resources = heading.find_next_sibling('ul')
                if resources:
                    links = resources.select('a[href]')
                    cited = {a['href'] for a in soup.select('a[href]') if resources not in a.parents}
                    if links and all(a['href'] in cited for a in links):
                        resources.decompose()
                        heading.decompose()
                        continue
                    resources['class'] = resources.get('class', []) + ['resources']
                    block = soup.new_tag('div', attrs={'class': 'resource-links'})
                    heading.insert_before(block)
                    block.append(heading)
                    block.append(resources)
        for table in soup.select('table'):
            headers = [th.get_text() for th in table.select('thead th')]
            if len(headers) == 4 and 'App 実走' in headers:
                group = soup.new_tag('colgroup')
                for width in [14, 24, 48, 14]:
                    col = soup.new_tag('col'); col['style'] = f'width:{width}%'; group.append(col)
                table.insert(0, group)
        for summary in soup.select('ul'):
            if len(summary.find_all('li', recursive=False)) <= 5 and len(summary.get_text()) < 500 and not summary.select('ul, ol, img, pre, table'):
                summary['class'] = summary.get('class', []) + ['compact-list']
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
        figures = {}
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
            notice = web.image_caption(image.name)
            caption.string = img.get('alt', '') + (' / ' + notice if notice else '')
            figure.append(caption)
            figures[image.name] = figure
            expected_images += 1
        # Figures must not stay inside paragraphs; HTML parsing would otherwise relocate them.
        for para in list(soup.select('p')):
            if para.find('figure'):
                para.name = 'div'
        keep_explanations_with_examples(soup, path, prefix, figures)
        # Chromium can ignore keep-with-next across consecutive headings.
        for heading in list(soup.select('h2, h3')):
            if 'section-lead' in heading.parent.get('class', []):
                continue
            subsection = heading.find_next_sibling()
            if subsection and subsection.name in ('h3', 'h4') and int(subsection.name[1]) == int(heading.name[1]) + 1:
                nodes = [heading, subsection]
                first_text = subsection.find_next_sibling()
                if first_text and first_text.name == 'h4' and subsection.name == 'h3':
                    nodes.append(first_text)
                    first_text = first_text.find_next_sibling()
                if first_text and first_text.name == 'p' and len(first_text.get_text()) < 800:
                    nodes.append(first_text)
                lead = soup.new_tag('div', attrs={'class': 'section-lead'})
                heading.insert_before(lead)
                for node in nodes:
                    lead.append(node.extract())
        section_links = ''.join(
            f'<li><a href="#{html.escape(heading["id"], quote=True)}">{html.escape(heading.get_text(" ", strip=True))}</a></li>'
            for heading in soup.select('h2[id]'))
        contents.append(f'<li><a class="contents-chapter" href="#{prefix}">{html.escape(title)}</a>'
            + (f'<ul class="contents-sections">{section_links}</ul>' if section_links else '') + '</li>')
        sections.append(f'<section class="chapter"><h1 id="{prefix}">{html.escape(title)}</h1>{soup}</section>')
    toc = ''.join(contents)
    cfg = {k: html.escape(str(v)) for k, v in config.items()}
    web_link = (f'<a href="{html.escape(web_base.rstrip("/") + "/app/index.html", quote=True)}">Web 版を開く</a>' if web_base
        else f'<a href="{source_url(web.SOURCE / "app/README.md", ref)}">オンライン原稿</a>')
    participant = paths[0].parent == web.SOURCE / 'app'
    provenance = '' if participant else f'<br>原稿の基準コミット：{html.escape(ref)}<br>原稿識別子：{digest[:12]}'
    cover = f'''<section class="cover"><p class="eyebrow">DEV DAYS · JAPANESE WORKSHOP</p>
<h1>GitHub Copilot App</h1><p class="subtitle">{label}</p><p>操作を確かめながら、Tailspin Toys の開発を進める</p>
<div class="meta">教材版：{cfg['edition']}<br>演習用テンプレート：{cfg['template_ref']}{provenance}</div>
<p>{web_link}</p><p><a href="{cfg['template_url']}">演習用テンプレート</a></p>
<p class="source">非公式の独立教材です。画像は操作位置の参考です。操作は本文の項目名と手順を確認してください。プロンプトは選択・コピーできる文字で収録しています。</p></section>'''
    license_text = html.escape((web.SOURCE / 'licenses/copilot-workshops.txt').read_text(encoding='utf-8'))
    if participant:
        attribution = '<a href="https://github.com/iwizsophy/dev-days-jp">日本語教材：iwizsophy/dev-days-jp</a>。<a href="https://github.com/github-samples/copilot-workshops">演習本文の参照元：github-samples/copilot-workshops</a>。'
    else:
        attribution = f'日本語原稿：iwizsophy/dev-days-jp / content/ja。演習本文の参照元：{html.escape(web.META["courses"]["app"]["repository"])}、固定コミット {web.META["courses"]["app"]["commit"]}。画像の撮影条件は content/ja/sources.json の ui_captures に記録しています。'
    credits = f'<section class="credits"><h1 id="credits">出典とライセンス</h1><p>{attribution}</p><pre>{license_text}</pre></section>'
    css = (ROOT / 'scripts/pdf/print.css').read_text(encoding='utf-8')
    result = f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{label} | Dev Days</title><style>{css}</style></head><body>{cover}<section class="contents"><h1 id="contents">目次</h1><p>章名や節名を選択すると本文へ移動します。PDFのしおりからは小節も開けます。</p><ul class="contents-chapters">{toc}<li><a class="contents-chapter" href="#credits">出典とライセンス</a></li></ul></section>{"".join(sections)}{credits}</body></html>'
    parsed = BeautifulSoup(result, 'html.parser')
    ids = [n['id'] for n in parsed.select('[id]')]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate PDF anchor')
    for link in parsed.select('a[href^="#"]'):
        if unquote(link['href'][1:]) not in ids:
            raise ValueError(f'Broken PDF anchor: {link["href"]}')
    return result, titles, expected_images


def normalize_cmap(data):
    """Restore Japanese shared glyphs and Latin ligatures in copied PDF text."""
    def unicode_value(value):
        text = bytes.fromhex(value).decode('utf-16-be')
        return ''.join(unicodedata.normalize('NFKC', c) if '\u2f00' <= c <= '\u2fdf' or '\ufb00' <= c <= '\ufb06' else '\u30fb' if c == '\u2027' else c for c in text).encode('utf-16-be').hex().upper()

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
    import pymupdf
    with pymupdf.open(path) as document:
        for number, page in enumerate(document, 1):
            for block in page.get_text('blocks'):
                if len(block) > 4 and 'Dev Days / Copilot App' in str(block[4]):
                    continue
                if block[0] < 40 or block[2] > page.rect.width - 40 or block[1] < 42 or block[3] > page.rect.height - 45:
                    raise ValueError(f'Content outside printable area on page {number}')
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
    prerequisite = (web.SOURCE / 'app/1-prerequisites.md').read_text(encoding='utf-8')
    if config['template_ref'] not in prerequisite:
        raise ValueError('distribution.json template_ref does not match prerequisites')
    template = web.META['material']['exercise_template']
    if any(config[f'template_{key}'] != template[key] for key in ('ref', 'commit')):
        raise ValueError('distribution.json template reference does not match sources.json')
    ref = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    inputs = sorted(list(web.SOURCE.rglob('*.md')) + list((ROOT / 'content/_images').rglob('*')) + [CONFIG, web.SOURCE / 'sources.json', web.SOURCE / 'licenses/copilot-workshops.txt', ROOT / 'scripts/pdf/print.css', ROOT / 'scripts/pdf/print.cjs', ROOT / 'scripts/build_workshops.py', Path(__file__)])
    digest = hashlib.sha256()
    for p in inputs:
        if p.is_file():
            digest.update(p.relative_to(ROOT).as_posix().encode()); digest.update(b'\0'); digest.update(p.read_bytes())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    temp = ROOT / 'tmp/pdfs'; temp.mkdir(parents=True, exist_ok=True)
    manifest = {'edition': config['edition'], 'template_ref': config['template_ref'], 'template_commit': config['template_commit'], 'source_commit': ref,
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
