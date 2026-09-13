# PDF 教材の作成と配布

更新元は `content/ja/` の Markdown です。PDF を手修正せず、Web と PDF を同じ原稿から生成します。

## 何を配るか

- 参加者へは `dev-days-app-participant.pdf` だけを配布します。演習0～8と概要、画像、出典・ライセンスを含みます。画像フォルダーは不要です。
- 講師は別冊の `dev-days-app-instructor.pdf` を使用します。運営、UI 確認、検証記録、緊急対応を収録しています。
- 演習コードは非公開テンプレートから取得します。PDF の配布だけではリポジトリのアクセス権は付与されません。
- `manifest.json` は配布管理者用です。原稿コミット・入力ハッシュ・PDF ハッシュ・検査結果を記録します。

PDF には目次リンク、章・節のしおり、ページ番号が付きます。画像は全体を保持して埋め込み、プロンプトは文字としてコピーできます。画面の細部は PDF ビューアーで拡大してください。

## 初回の準備

Python 3.12 以降、Node.js 24、Git を用意し、リポジトリのルートで実行します。

```sh
python -m pip install --target .workshop-tools -r scripts/requirements-pdf.txt
npm ci --prefix scripts/pdf --ignore-scripts
node scripts/pdf/node_modules/playwright/cli.js install chromium
```

日本語フォントは Windows では Noto Sans JP またはメイリオ、Linux では Noto Sans CJK JP を使用します。Ubuntu は `sudo apt-get install fonts-noto-cjk` で用意します。CI は Chromium の OS 依存とフォントも導入します。初回の依存ダウンロード後は、PDF 生成時に外部リソースを読み込みません。

## 通常の生成

```sh
python scripts/build_distribution.py
```

この1コマンドで Web の生成・リンク検査、2冊の PDF の生成・検査を行います。成果物は `output/pdf/`、作業用 HTML は `tmp/pdfs/` に出力します。両フォルダーは Git 管理しません。

参加者用だけの場合は `--audience participant`、講師用だけなら `--audience instructor` を指定します。同じ出力先の他方の既存 PDF は更新されないため、通常の配布は省略時の2冊同時生成を使ってください。

ローカルの Chrome を使う場合は `--chromium` に実行ファイルを指定できます。Node が PATH にない場合は `--node` を指定します。特定の利用者のローカルパスを原稿や配布設定へ書き込みません。

## 版と Web の案内先

`content/ja/distribution.json` で教材の版、テンプレートのタグ、各冊の収録順を管理します。テンプレートのタグが演習0の原稿に存在しない場合は生成を止めます。配布時は原稿をコミットしてから最終生成し、そのコミットとハッシュを記録します。

現在の Web 版はローカル閲覧が前提です。PDF の冊内リンクは該当章へ移動し、冊外の補助資料は同じ原稿コミットの GitHub ページへリンクします。閲覧権限が必要です。公開サイトがあるとは案内しません。

将来、利用者がアクセスできる Web 版を配置したら、次のように workshops ディレクトリの URL を指定します。

```sh
python scripts/build_distribution.py --web-base-url https://example.com/ja/workshops
```

このオプションはリンク先を変更するだけで、Web サイトの公開・デプロイは行いません。

## 検査と目視確認

```sh
python scripts/test_distribution.py
python scripts/render_pdf_review.py output/pdf/dev-days-app-participant.pdf
python scripts/render_pdf_review.py output/pdf/dev-days-app-instructor.pdf
```

生成処理では全章の文字抽出、各コード・プロンプトブロックの原稿との一致（改行・空白を除く）、しおり、リンク、画像読込、冊内アンカーを検査します。Chromium の日本語共有字形に起因する康熙部首・中黒の文字マッピングを補正し、コピー時の文字を原稿と照合します。原稿で補正対象の部首文字・U+2027 を意図的に使う場合は、そのまま処理せずエラーになります。

`tmp/pdfs/review/` に全ページ PNG と一覧画像を出力します。配布前には画像の読める大きさ、表の分割、章の先頭、ページ末尾、プロンプトの改ページを目視確認してください。機械検査の成功だけを組版の確認とは扱いません。

## GitHub Actions から取得

このコピーの **Actions → Build workshop distribution → Run workflow** で対象ブランチを指定します。成功した実行の **workshop-pdf** artifact に2冊と manifest が入っています。**workshop-pdf-visual-review** は目視確認用です。非公開リポジトリのアクセス権を持つ管理者が取得し、参加者には参加者用 PDF を配布します。artifact の保存期間は PDF が30日、確認画像が7日です。

ワークフローは対象パスの PR と教材ブランチへの push でも動作します。外部への公開や Release 作成は行いません。原稿・生成機構と、生成 Web ページに差分がある場合は別コミットにします。
