# PDF 教材の作成と配布

教材の正本（更新元）は `content/ja/` 配下の Markdown です。PDF を手作業で直接修正することはせず、Web サイトと PDF の双方を同一の原稿から自動生成します。

## 配布物の構成と対象者

- **参加者向け (`dev-days-app-participant.pdf`)**：演習0〜8の本文、概要、画像、出典・ライセンス表記を収録した本編です。参加者にはこの PDF のみを配布します（画像フォルダーの個別配布は不要です）。
- **講師向け別冊 (`dev-days-app-instructor.pdf`)**：当日の運営ガイド、UI 確認表、検証記録、緊急対応手順を収録した講師専用の資料です。
- **配布管理マニフェスト (`manifest.json`)**：配布管理者が使用する記録ファイルです。原稿のコミット SHA、入力ハッシュ、PDF のハッシュ値、および各自動検査の結果が記録されます。

生成された PDF には、目次リンク、章・節のしおり（アウトライン）、ページ番号が付与されます。画面キャプチャ画像は全体を保って埋め込まれ、コードやプロンプトはテキストとしてコピー可能です（画面の細部は PDF ビューアー側で拡大して確認します）。

## 環境準備（初回のみ）

Python 3.12 以降、Node.js 24、および Git がインストールされている環境を用意し、リポジトリのルートで次のコマンドを実行します。

```sh
python -m pip install --target .workshop-tools -r scripts/requirements-pdf.txt
npm ci --prefix scripts/pdf --ignore-scripts
node scripts/pdf/node_modules/playwright/cli.js install chromium
```

### フォント要件
- **Windows**：Noto Sans JP または メイリオ
- **Linux / Ubuntu**：Noto Sans CJK JP（`sudo apt-get install fonts-noto-cjk` で導入）
- **CI 環境**：Chromium の OS 依存ライブラリおよびフォントも自動導入されます。
初回の依存ツール取得が完了した後は、PDF 生成処理中に外部ネットワークリソースを読み込むことはありません。

## PDF の通常生成

Web サイトの生成・内部リンク検査、および2冊の PDF の生成・自動検査をまとめて行うには、次の1コマンドを実行します。

```sh
python scripts/build_distribution.py
```

- 生成された PDF は `output/pdf/` に、作業用の一時 HTML は `tmp/pdfs/` に出力されます（いずれのフォルダーも Git 管理対象外です）。
- 個別生成を行う場合は、参加者用のみであれば `--audience participant`、講師用のみであれば `--audience instructor` を指定できます。ただし、個別指定した場合はもう一方の既存 PDF が更新されないため、通常の教材配布時は引数を省略して2冊同時に生成してください。
- 実行環境の調整として、ローカルの Chrome を使用する場合は `--chromium` に実行ファイルパスを指定でき、Node.js が PATH に通っていない場合は `--node` で指定可能です。特定の個人のローカル環境パスを原稿や設定ファイルへ直接書き込まないようにしてください。

## バージョン管理と Web リンクの案内方針

教材のバージョン、テンプレートのタグ・コミット、各冊への収録順は `content/ja/distribution.json` で一元管理しています。本文と表紙にはタグ名を表示し、コミットSHAは管理用の記録に保持します。`template_ref` が演習0にない場合や、タグ・コミットが `sources.json` と一致しない場合は生成を停止します。教材を配布する際は、原稿の変更をGitにコミットしてから最終生成を行い、そのコミットSHAとハッシュ値をマニフェストに記録します。

未コミットの原稿から作るPDFはローカル確認用です。表紙の「原稿の基準コミット」はHEADを示し、今回読み込んだ原稿は「原稿識別子」とマニフェストの `source_sha256` で識別します。この状態では冊外のGitHubリンクは改訂前の基準コミットを参照するため、最新の補助資料は同時生成した講師用PDFまたはローカルWebで確認してください。

### リンク先の解決
PDF内のリンクは次のように解決されます。

- **冊内リンク**：PDF 内の該当章・節へジャンプします。
- **冊外リンク（補助資料等）**：同じ原稿コミットに基づくGitHub上のページへリンクします。

Webサイトへリンクする場合は、次のようにworkshopsディレクトリのURLを指定してビルドします。

```sh
python scripts/build_distribution.py --web-base-url https://example.com/ja/workshops
```
※このオプションは PDF 内のリンク先 URL を切り替えるだけであり、Web サイト自体の公開・デプロイを行うものではありません。

## 品質検査と目視確認の義務

PDF 生成後は、次のスクリプトを用いて機械検査と目視確認を実施します。

```sh
python scripts/test_distribution.py
python scripts/render_pdf_review.py output/pdf/dev-days-app-participant.pdf
python scripts/render_pdf_review.py output/pdf/dev-days-app-instructor.pdf
```

### 機械検査の仕様
生成処理では、全章からのテキスト抽出、各コード・プロンプトブロックの原稿との一致（改行・空白を除く）、しおり、リンク、画像読み込み、および冊内アンカーの整合性を機械的に検査します。
特に、Chromium の日本語共有字形に起因する康熙部首や中黒（U+2027）の文字マッピングを自動補正し、PDF からコピーした文字が原稿と一致することを照合します。原稿内で補正対象の部首文字や U+2027 を意図的に使用している場合は、意図しない変換を防ぐためエラーとして検出されます。

### 目視確認の義務
`scripts/render_pdf_review.py` を実行すると、`tmp/pdfs/review/` 配下に全ページの PNG 画像および一覧画像が出力されます。配布前には、次の点を必ず人間の目で目視確認してください。
- キャプチャ画像内の文字が判読できる大きさになっているか
- 表が不自然な位置で改ページ分割されていないか
- 章の開始位置やページ末尾に崩れがないか
- プロンプトの枠囲みが途中で改ページによって分断されていないか

**機械検査がパスしたことだけをもって、組版が完了したとは判定しません。**

## GitHub Actions による取得

リポジトリで GitHub Actions が有効化されている場合（有効化はリポジトリ管理者が設定を確認して実施）、クラウド上でビルド成果物を取得できます（無効な環境でもローカル生成は利用可能です）。

1. ワークフローが既定ブランチに入っている場合は、GitHub 上の **Actions → Build workshop distribution → Run workflow** から対象ブランチを指定して手動実行します（既定ブランチに未反映の間は、対象ブランチへの push または Pull Request によって実行させます）。
2. 実行成功後、**workshop-pdf** artifact に2冊の PDF と `manifest.json` が格納されます。また、**workshop-pdf-visual-review** には目視確認用の全ページ画像が出力されます。
3. 管理者がartifactを取得し、参加者には参加者用PDFを配布します。
   - artifact の保存期間：PDF は30日間、確認用画像は7日間です。

ワークフローは対象パスの Pull Request や教材ブランチへの push でも動作します。外部への無断公開や GitHub Releases の作成は行いません。なお、原稿・生成スクリプトの修正と、生成された Web ページの差分がある場合は、必ず別コミットに分離してください。
