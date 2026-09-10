"""Render checked-in Japanese workshop sources; no network access required."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import os
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.workshop-tools'))
import markdown
from markdown.extensions.toc import slugify_unicode

SOURCE = ROOT / 'content/ja'
OUTPUT = ROOT / 'website/ja/workshops'
META = json.loads((SOURCE / 'sources.json').read_text(encoding='utf-8'))
LABELS = {'app': 'Copilot App', 'cli': 'Tailspin Toys CLI', 'mona-mayhem': 'Mona Mayhem'}
FILES = {key: sorted((SOURCE / key).glob('*.md'), key=lambda p: (p.name != 'README.md', p.name)) for key in LABELS}
TARGETS = {p.resolve(): OUTPUT / key / ('index.html' if p.name == 'README.md' else p.stem + '.html') for key, files in FILES.items() for p in files}
SUPPORT = sorted((SOURCE / 'material').glob('*.md'))
TARGETS.update({p.resolve(): OUTPUT / 'material' / (p.stem + '.html') for p in SUPPORT})


def relative(target, origin):
    return os.path.relpath(target, origin.parent).replace(os.sep, '/')


def title_body(path):
    text = path.read_text(encoding='utf-8')
    if text.startswith('---\n'):
        front, text = text[4:].split('\n---\n', 1)
        title = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', front, re.M)[1]
    else:
        title = re.search(r'^# (.+)$', text, re.M)[1]
        text = re.sub(r'^# .+\n', '', text, count=1)
    # GitHub admonitions: render recognizable Japanese labels in normal blockquotes.
    for key, label in {'NOTE': '補足', 'TIP': 'ヒント', 'IMPORTANT': '重要', 'WARNING': '注意', 'CAUTION': '注意'}.items():
        text = text.replace(f'[!{key}]', f'**{label}**')
    return title, text


def transform_links(body, source, destination):
    def replace(match):
        attr, value = match[1], match[2]
        url = urlsplit(value)
        if url.scheme or url.netloc or not url.path:
            return match[0]
        candidate = (source.parent / unquote(url.path)).resolve()
        if candidate in TARGETS:
            target = TARGETS[candidate]
        elif candidate.is_file() and candidate.is_relative_to(ROOT / 'content/_images'):
            target = OUTPUT / 'assets' / candidate.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(candidate, target)
        else:
            raise ValueError(f'Unresolved source link: {source}: {value}')
        suffix = ('?' + url.query if url.query else '') + ('#' + url.fragment if url.fragment else '')
        return f'{attr}="{escape(relative(target, destination) + suffix, quote=True)}"'
    return re.sub(r'(href|src)="([^"]+)"', replace, body)


def shell(title, body, destination, extra=''):
    css = relative(OUTPUT / 'workshops.css', destination)
    theme = relative(ROOT / 'website/theme-toggle.js', destination)
    site = relative(ROOT / 'website/ja/index.html', destination)
    guide = relative(ROOT / 'website/ja/handson-guide.html', destination)
    index = relative(OUTPUT / 'index.html', destination)
    return f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>{escape(title)} | Dev Days 日本語版</title>
<link rel="stylesheet" href="{css}"><script src="{theme}"></script></head><body>
<a class="skip" href="#lesson">本文へ移動</a><header><nav aria-label="資料のナビゲーション">
<a href="{site}">教材セットの入口</a><a href="{index}">App シナリオの目次</a>
<a href="{guide}#switch">UI が違うときは CLI へ</a></nav>
<button class="theme-toggle" type="button" onclick="toggleTheme()">☀️ ライト</button></header>
<main id="lesson"><h1>{escape(title)}</h1>{extra}{body}</main></body></html>\n'''


def build():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / 'licenses').mkdir(exist_ok=True)
    for p in (SOURCE / 'licenses').glob('*.txt'):
        shutil.copyfile(p, OUTPUT / 'licenses' / p.name)
    for course, files in FILES.items():
        meta = META['courses'][course]
        for i, source in enumerate(files):
            destination = TARGETS[source.resolve()]
            destination.parent.mkdir(exist_ok=True)
            title, text = title_body(source)
            renderer = markdown.Markdown(extensions=['tables', 'toc', 'sane_lists', 'pymdownx.superfences', 'pymdownx.tasklist'], extension_configs={'toc': {'slugify': slugify_unicode}, 'pymdownx.superfences': {'disable_indented_code_blocks': False}})
            body = transform_links(renderer.convert(text), source, destination)
            prevnext = []
            for n, label in [(i - 1, '← 前の章'), (i + 1, '次の章 →')]:
                if 0 <= n < len(files):
                    prevnext.append(f'<a href="{relative(TARGETS[files[n].resolve()], destination)}">{label}：{escape(title_body(files[n])[0])}</a>')
            nav = '<nav class="chapter-nav" aria-label="章の移動">' + ''.join(prevnext) + '</nav>'
            upstream = f"https://github.com/{meta['repository']}/blob/{meta['commit']}/{meta['source']}/{source.name}"
            source_link = f'<a href="{upstream}">参照原文</a>'
            license_link = relative(OUTPUT / 'licenses' / meta['license'], destination)
            notice = f'<p class="source">非公式の日本語版 · {source_link} · <a href="{license_link}">MIT ライセンス</a><br>参照コミット：<code>{meta["commit"][:12]}</code> ／ 確認日：{META["checked"]}</p>'
            guide = relative(ROOT / 'website/ja/handson-guide.html', destination)
            notice += f'<aside>UI の名前・位置は参照原文のものです。利用条件は <a href="{guide}#plans">事前確認</a>を参照してください。</aside>'
            if course == 'app':
                status = relative(OUTPUT / 'material/verification.html', destination)
                notice += f'<aside>本編：App シナリオ。各章の CLI 代替手順はこの教材独自の補足です。App と代替経路の実走は未検証です。<a href="{status}">章別の検証状況</a></aside>'
            else:
                notice += '<aside>参考資料：本編の続きではありません。App の途中で切り替える場合は App の同じ章の CLI 代替手順に戻ってください。</aside>'
            if course == 'cli':
                notice += '<aside>このコースの <code>--yolo</code> を含む手順は、演習専用 Codespace / dev container を前提とする原文の手順です。App の途中からローカルで切り替える場合は、上の「CLI の横道」の通常対話手順を使ってください。</aside>'
            toc = '<details><summary>この章の目次</summary>' + renderer.toc + '</details>'
            destination.write_text(shell(title, nav + toc + '<article>' + body + '</article>' + nav, destination, notice), encoding='utf-8')
    for source in SUPPORT:
        destination = TARGETS[source.resolve()]
        destination.parent.mkdir(exist_ok=True)
        title, text = title_body(source)
        body = markdown.markdown(text, extensions=['tables', 'sane_lists', 'pymdownx.superfences'])
        body = transform_links(body, source, destination)
        destination.write_text(shell(title, '<article>' + body + '</article>', destination,
                                    '<aside>この教材セット独自の運営・補助手順です。</aside>'), encoding='utf-8')
    index = OUTPUT / 'index.html'
    body = '<p>App 版の順序・課題・到達目標に沿って Tailspin Toys を改修します。UI で止まった場合は各章の CLI 代替手順で同じ作業を続け、同じ章の完了条件へ合流します。</p>'
    body += '<p><a href="app/0-prerequisites.html">演習0から始める</a> · <a href="material/continuation.html">切り替え・PR・合流の共通手順</a> · <a href="material/instructor.html">講師ガイド</a> · <a href="material/verification.html">検証状況</a></p>'
    for course in ['app']:
        files = FILES[course]
        body += f'<section><h2>{LABELS[course]}</h2><ol>'
        for source in files:
            body += f'<li><a href="{relative(TARGETS[source.resolve()], index)}">{escape(title_body(source)[0])}</a></li>'
        body += '</ol></section>'
    body += '<p><a href="references.html">参考資料：独立した CLI コース・Mona Mayhem・運営原本</a></p>'
    index.write_text(shell('App シナリオの演習目次', body, index), encoding='utf-8')
    reference = OUTPUT / 'references.html'
    body = '<p>以下は別シナリオの参考資料です。本編の CLI 代替経路は、App の各章にあります。</p>'
    for course in ['cli', 'mona-mayhem']:
        body += f'<section><h2>{LABELS[course]}（参考）</h2><ul>'
        for source in FILES[course]:
            body += f'<li><a href="{relative(TARGETS[source.resolve()], reference)}">{escape(title_body(source)[0])}</a></li>'
        body += '</ul></section>'
    body += '<p><a href="https://github.com/github/dev-days">イベント資料の参照元</a> · <a href="https://github.com/github-samples/copilot-workshops">演習本文の参照元</a>（どちらも閲覧用）</p>'
    reference.write_text(shell('参考資料', body, reference), encoding='utf-8')
    verify()
    print(f'Built {sum(map(len, FILES.values()))} lesson/overview pages, {len(SUPPORT)} support pages, and two indexes.')


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links = []; self.ids = []; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        self.links.extend(attrs[k] for k in ('href', 'src') if k in attrs)


def verify():
    web = ROOT / 'website'
    pages = {p.resolve(): Links(p.read_text(encoding='utf-8')) for p in web.rglob('*.html')}
    errors = []; checked = 0
    for path, page in pages.items():
        if len(page.ids) != len(set(page.ids)): errors.append(f'Duplicate IDs: {path}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc: continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir(): target = target / 'index.html'
            checked += 1
            if not target.is_relative_to(web) or not target.exists(): errors.append(f'Missing: {path}: {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'Missing anchor: {path}: {link}')
    if errors: raise ValueError('\n'.join(errors))
    print(f'Checked {len(pages)} pages and {checked} local links/assets/anchors.')


if __name__ == '__main__':
    build()
