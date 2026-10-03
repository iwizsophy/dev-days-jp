---
title: "レッスン 3 - カスタム指示による Copilot のガイド"
description: "GitHub Copilot app を使い、バックログの Issue から始めてカスタム指示の標準をリポジトリに追加し、変更を pull request としてマージします。"
authors:
  - geektrainer
lastUpdated: 2026-10-04
---

> **この章の進め方：** Appで規約更新のIssueを開き、指示ファイルとコード例をレビューしてからマージします。作業対象は画像内のIssueではなく、本文のタイトルと要件を確認して選んでください。ボタンや機能が見つからない場合は、本文の操作対象と項目名を確認し、講師に相談してください。

指示ファイルの仕組みと設計方針は、章末の[補足](#補足)で確認できます。

このレッスンでは、次の内容を学習します。

- リポジトリ全体への指示と、パス固有の指示ファイルがエージェントにどのように渡されるかを理解する
- バックログ内の指示関連 Issue から新しいセッションを開始する
- `.github/copilot-instructions.md` にドキュメント標準を追加するようエージェントに依頼する
- 変更内容をレビューし、pull request としてマージする

<a id="シナリオ"></a>

## 3.1 シナリオ

成熟した開発組織と同様に、Tailspin Toys にも開発プラクティスに関するガイドラインと要件が存在します。具体的には次の2点です。

- コードには TSDoc 形式のドキュメントコメント（doc comment）を付与する
- コードフォーマットのルールを文書化し、ESLint 等の静的検証ツールによって機械的に適用する

<a id="このプロジェクトのカスタム指示ファイルを確認する"></a>

## 3.2 このプロジェクトのカスタム指示ファイルを確認する

本リポジトリに配置されている指示ファイルを確認しましょう。ルートとなる `copilot-instructions.md` と、個別タスクに対応する複数の `*.instructions.md` ファイルで構成されています。App 内のファイルビューアーを使って確認します。

1. 右側のパネルが表示されていない場合は、画面右上の **Toggle panel** を選択して開きます。

   ![右パネルの Add tab メニュー。Files、Browser、Terminal の入口](../../_images/app-1.1.20-20260913-add-tab.png)

2. パネル上部のタブ列にある **+**（Add tab）を選択します。
3. 一覧から **Files** を選択します。
4. <kbd>Ctrl</kbd>+<kbd>P</kbd> を押して **Go to file** を開き、`copilot-instructions.md` を検索します。

   ![App 全体と Go to file。copilot-instructions.md の検索結果](../../_images/app-1.1.20-20260913-file-search.png)

5. 検索結果から `copilot-instructions.md` を選択して開きます。
6. ファイルの内容を確認します。プロジェクト概要に加えて、**Agent notes**、**Code standards**、**Scripts**、**Repository Structure** といったセクションが定義されています。**Code standards** 配下には **GitHub Actions Workflows** の指針もネストされており、これらは Copilot との全対話に共通して適用されます。
7. 右側のファイルツリーを確認します。もしツリー上に `.github` フォルダーが表示されていない場合は、ファイルパネル上部の歯車アイコン **View options** をクリックし、**Show hidden files** を有効にしてください。

   なお、ツリーを展開する代わりに、**Go to file** に直接ファイル名を入力して開くことも可能です。

   ![会話欄と指示ファイルの表示。右上の View options に Show hidden files](../../_images/app-1.1.20-20260913-files-options.png)

8. `.github/instructions` フォルダーを展開し、配置されているファイルを確認します。Astro ファイル、Drizzle データレイヤー、単体テストなどに向けた指示ファイルが並んでいます。
9. `.github/instructions/unit-tests.instructions.md` を開きます。ファイル冒頭の `applyTo` フィールドに注目してください。ここにはリポジトリルートを基準とする glob パターンが記述されており、指示を適用するファイル（例: `**/*.test.ts` に一致する TypeScript テストファイル）が限定されています。

   `applyTo`は指示の対象を表す指定です。たとえば`src/lib/games.test.ts`は上記のパターンに一致し、`src/components/GameCard.astro`は一致しません。対象が狭すぎると必要なファイルが漏れ、広すぎると関係のない規則まで読ませることになります。書式は[公式のパス固有指示の説明][path-instructions]を参照し、対象ファイルを具体的に挙げて適用範囲を確認しましょう。ファイル名だけで判断せず、本文の指示内容も読んでください。

10. このプロジェクトで単体テストを実装する際の個別ルールがどのように定義されているかを確認します。
11. 続けて `.github/instructions/drizzle.instructions.md` を開き、末尾までスクロールします。他の指示ファイル（`unit-tests.instructions.md` 等）やプロジェクト内の既存ファイルへの相対リンクが記載されている点に注目してください。指示セットを小規模かつ再利用可能なファイルへ分割し、コード生成時に参照すべき実例を Copilot に提示する構造になっています（ここに記載された相対パスは、リポジトリルートではなく指示ファイル自身の位置を基準とします）。

> [!NOTE]
> 現在の`copilot-instructions.md`にはコーディング標準が記載されています。次の手順では規約更新のIssueの要件に従い、処理の意図を説明するコメント、データ層のTSDoc/JSDoc、AstroコンポーネントのPropsの説明、ESLintとREADMEへの反映を確認します。全ファイルへのヘッダーコメント追加はIssueの要件に含まれていません。

<a id="指示に関する-issue-から開始する"></a>

## 3.3 指示に関する Issue から開始する

前章では空の会話入力欄から直接プロンプトを入力してセッションを開始しましたが、実際の開発では Issue に起票された課題を起点として作業を進めることが一般的です。指示ファイルの更新用に登録された Issue を選択し、新しいセッションを作成して作業を依頼しましょう。

> [!NOTE]
> 指示ファイルの内容は、以後 Copilot が生成するすべてのコード品質に直接影響を与えます。そのため、指示が Copilot を正しく導く表現になっているかを厳密に確認する必要があります。本レッスンのように、まず Copilot に初期ドラフトを作成させ、それを人間が慎重にレビューして要件適合性を検証するアプローチが極めて有効です。

1. サイドバーの **Projects** で自分の演習用プロジェクトを選択し、**Issues** フィルターでOpen Issueを表示します。課題が見つからない場合は、[レッスン1のバックログ確認](1-install-copilot-app.md#バックログ-issue-の確認)に従って表示条件を見直します。

2. 一覧から**Update our repository coding standards**というタイトルのIssueを選択して開きます。番号だけで選ばず、タイトルと本文を確認してください。
3. 画面右上の **New session** を選択し、この Issue に紐づく新しいセッションを開始します。

> [!NOTE]
> 新しいセッションのworktreeに、前章でmainへマージした星評価の変更が含まれていることを確認してください。設定の承認を求められた場合は、**Review repository content → Repository trust**でセットアップ内容やRunの定義を読み、**Accept for new sessions**を選択します。

   ![Issueの詳細画面と右上のNew sessionボタンの操作例](../../_images/app-1.1.20-20260913-issue-session.png)

4. 次のプロンプトを入力し、Issue の要件に従って指示ファイルを更新するよう Copilot に指示します。

   ```plaintext
   この Issue に記載された要件に従って、プロジェクトの指示ファイルを更新してください。既存の指示、実装、ESLint設定に矛盾がないか確認し、必要なREADMEの説明も更新してください。変更した規則と、その規則を機械検査できる範囲を説明してください。PR はまだ作らないでください。
   ```

Copilot が指示ファイル等の更新作業を実行します。

変更対象には、指示ファイルだけでなくREADMEやESLint設定が含まれる場合があります。ファイル数を正解とせず、それぞれがIssueの要件に必要な変更かを確認してください。

<a id="変更をレビューする"></a>

## 3.4 変更をレビューする

Copilot が実施した更新内容を差分ビューで精査し、さらに更新後の指示に基づいてどのようなコードが生成されるかをシミュレーションさせて確認します。

指示ファイルを活用すると、エージェントへこれらのプラクティスを共有し、方針に沿ったコード生成を促せます。ただし、毎回同じように指示を守ることは保証されません。GitHubの[カスタム指示の説明][instruction-files]でも、AIの応答は非決定的であると説明されています。そのため、本章では指示を書いた後に生成例を読み、機械検査で確認できる規則はESLintなどでも検査します。

指示と機械検査では役割が異なります。「なぜこの処理が必要かをコメントで説明する」という指示は、書く内容の判断を助けます。一方、ESLintは設定した規則への違反を検出します。lintが成功しても、コメントが実装と一致し、その理由を十分に伝えているかは人間が読む必要があります。

1. 会話入力欄の上部にある **Changes**（Open changes）を選択して差分ビューを開きます。変更されたファイルの一覧と、追加・削除された行を確認します。

   ![左の会話欄の Changes と右の差分パネルを同時に表示した App 全体](../../_images/app-1.1.20-20260913-changes.png)

2. 更新された指示ファイル（`copilot-instructions.md` など）の差分をレビューします。コードへのドキュメント付与およびコメント記述に関するガイドラインが適切に追加されていることを確認します。

   規則の対象と理由を説明できるか、既存の説明と矛盾しないかを読みます。たとえば、ディレクトリ構成の説明は実際のファイルと、SQLiteのコード例は実装の使い方と照合します。食い違いがあれば修正を依頼してください。指示を増やすときは、新しい段落だけでなく、同じ内容を説明している既存の段落も確認します。

> [!NOTE]
> AI の出力は確率的に変動するため、生成される文言の細部は上記と異なる場合があります。

3. 次のプロンプトを入力し、新しい指示がコード生成にどう反映されるか、コード例の提示をエージェントに求めます。

   ```plaintext
   ファイルを変更せず、コードの例だけを見せてください。新しい指示に従って、すべての Publishers を返すライブラリコンポーネントを作るよう依頼した場合、どのようなコードになりますか？
   ```

4. Copilotが提示したコード例をレビューします。データを取得する関数の役割、引数、戻り値がTSDoc/JSDocで説明され、コメントがコードと一致しているかを確認します。引数や戻り値がある関数では、`@param`・`@returns`の説明も読みます。Issueにない全ファイルへの一律のヘッダー付与は、成功条件に含めません。

たとえば、テストから渡せる`db`引数があれば、コメントにもその使い方が読み取れるかを確認します。「出版社を返す」とだけ書かれていて、実際の戻り値や引数の意味が不明な場合は、具体的な修正を依頼できます。コード例は指示の伝わり方を観察する小さな試行です。この一例の成功だけで、今後の生成結果がすべて規約に適合すると判断せず、次章の実装でも確認を続けます。

これで、プロジェクトの指示ファイルが更新され、エージェントへの指示伝達が意図通りに機能していることを確認できました。

<a id="pull-request-を作成してマージする"></a>

## 3.5 pull request を作成してマージする

指示ファイルはチーム全体で共有されるリポジトリの重要な構成要素（開発資産）です。他のソースコードと同様に、変更内容を含めた pull request を作成してマージします。

1. 画面右上にある **Create PR** を選択します。

   この操作でコミット作成、リモートへのpush、PR作成へ進みます。対象の差分をレビューしてから実行してください。

2. ブラウザー認証を求められた場合は、**Sign in with your browser** を選択して画面の指示に従い認証します。
3. Copilot が pull request の作成を開始します。
4. PR作成後、CopilotはリポジトリのCIワークフローを監視します。Appのチェック一覧を開き、必要なすべてのジョブが成功したか確認します。
5. **Ready to merge**を選択し、ダイアログ内のチェック状態も確認します。**Checks are running**が残る間は待ちます。ボタンの表示だけでCIの成功を判断せず、GitHub側の実行結果とも照合してください。表示が更新されない場合はダイアログを閉じて開き直します。
6. CIの全成功を確認してから、ダイアログの**Merge pull request**を選択し、mainへ通常マージします。AppとGitHubの両方で**Merged**になったことを確認します。

> [!NOTE]
> デフォルトブランチへマージした指示は、次章で最新のmainから始めるセッションでも参照できます。新しいworktreeに更新した指示が含まれているかを確認し、生成されたTypeScriptコードのTSDocもレビューします。指示を共有することと、生成結果が指示に従ったことの確認を、それぞれ行ってください。

<a id="まとめと次のステップ"></a>

## 3.6 まとめと次のステップ

App が指示ファイルからコンテキストを取得する仕組みを理解し、Issue を起点とするセッションを通じてリポジトリ全体の標準規約を追加・マージしました。

- リポジトリ全体の `copilot-instructions.md` と、特定パス用の `*.instructions.md` ファイルの役割を確認した
- バックログ内の規約更新 Issue から新しいエージェントセッションを開始した
- `.github/copilot-instructions.md` にドキュメント標準を追加するようエージェントへ依頼した
- 変更差分をレビューし、コード生成例によって効果を確認したうえで pull request としてマージした

この章を振り返り、追加した規則のうち「機械検査で確認したもの」と「コードを読んで判断したもの」を一つずつ挙げてみてください。次は新しいセッションでゲームの絞り込み機能を実装し、いま共有した規約が実際のコードにどう反映されるかを確認します。[レッスン 4「Autopilot による機能の構築」][next-lesson]へ進んでください。

<a id="補足"></a>

## 3.7 補足

<a id="コンテキストと指示ファイル"></a>

### 3.7.1 コンテキストと指示ファイル

生成 AI を活用するうえで、コンテキスト（文脈や背景情報）の提供は極めて重要です。特定の設計方針に沿ってタスクを実装させたい場合や、Copilot があらかじめ把握しておくべき前提知識がある場合は、それらをコンテキストとして利用可能な状態にしておく必要があります。

そのための特に強力な手段が[指示ファイル（Instruction files）][instruction-files]です。指示ファイルには、期待するコードの機能要件だけでなく、コードの構成方法や規約も明記できます。本レッスンでは、リポジトリにドキュメント作成の標準規約を追加します。実際の開発現場と同様に、バックログの Issue を起点としてエージェントに変更作業を実行させます。

<a id="指示ファイルの構造と役割"></a>

### 3.7.2 指示ファイルの構造と役割

カスタム指示を定義すると、Copilotにプロジェクト固有の前提知識や設定を提供できます。毎回のプロンプトに同じ背景を繰り返し書く手間を減らし、規約に沿った提案を得やすくする仕組みです。推奨するコーディング規約、採用ライブラリ、コード中に記述すべきコメントの粒度まで指定できます。[GitHub公式の概要][instruction-files]も、継続的に使う背景情報を指示として共有する方法を説明しています。

指示ファイルには、リポジトリ全体に一律適用するものと、特定ファイル種別のタスクに応じて適用するものの2階層があります。

1. **リポジトリ全体の指示（`.github/copilot-instructions.md`）**<br>
   リポジトリに対する**すべての**リクエストで Copilot に送信される単一の指示ファイルです。Copilot に投げるチャットや CLI リクエスト全般に関係するプロジェクトレベルの情報（採用技術スタック、アーキテクチャの概要、全体的なベストプラクティスなど）を記載します。
2. **パス固有の指示ファイル（`.github/instructions/*.instructions.md`）**<br>
   特定のタスクやファイル種類向けに作成する個別指示ファイルです。特定のプログラミング言語（TypeScript や Astro など）のコーディング規約や、UI コンポーネント作成、単体テスト一式の構築といった具体的タスクに応じたガイドラインを定義します。

> [!NOTE]
> `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`などの指示ファイルもありますが、対応する種類はCopilotの利用環境によって異なります。[対応表][custom-instructions-support]を参照し、本演習ではテンプレートにある`.github/copilot-instructions.md`と`.github/instructions/`を確認します。

Appの設定画面にも、全プロジェクト共通のApp instructionsと、プロジェクトごとのInstructionsがあります。これらの設定場所は[Appのカスタマイズ手順][customize-app]で説明されています。本章でリポジトリ内のファイルを編集するのは、チームが同じ指示を読み、ソースコードと同じように差分レビューできる形で共有するためです。

<a id="指示ファイルを管理するためのベストプラクティス"></a>

#### 3.7.2.1 指示ファイルを管理するためのベストプラクティス

指示ファイルの詳細な設計論はこのワークショップの範囲を超えますが、本サンプルプロジェクトに含まれる構成は代表的なアプローチを示しています。基本方針は次の通りです。

- `copilot-instructions.md` には、開発対象の概要、プロジェクト構造、全体的なコーディング規約など、プロジェクト共通のハイレベルなガイダンスを集約する
- `*.instructions.md` ファイルは、ファイル種別（単体テスト、Astro コンポーネント、データアクセス層など）や個別タスクに特化した具体的な指示を記述する
- 明快な自然言語を用い、望ましいコード例（Good）と避けるべきコード例（Bad）を併記する

指示ファイルに単一の絶対的な正解はありません。プロジェクトの成熟度やチームの文化に合わせて反復的にブラッシュアップしていくことが推奨されます。

指示の粒度を決めるときは、その規則を必要とするファイルを先に考えます。たとえば、全体の技術構成は共通指示に置き、テスト用DBの作り方は単体テスト向けの指示へ置くと、用途を読み分けやすくなります。似た規則を複数ファイルへコピーすると、後の変更で食い違うことがあります。同じ対象に適用される指示は一緒に読み、既存コードや検査設定とも照合してください。

> [!TIP]
> GitHub Copilot を導入するすべてのプロジェクトにおいて、体系的な指示ファイル群を整備しておくことを強く推奨します。本プロジェクトでも、多くのコード種別に対応した個別指示ファイルが配置されています。
>
> テンプレートや作成の出発点を探している場合は、指示ファイルやカスタムエージェントの実例が集約されているリポジトリ [awesome-copilot][awesome-copilot] を参考にしてください。

[指示ファイルの確認手順へ戻る](#このプロジェクトのカスタム指示ファイルを確認する)

<a id="リソース"></a>

## 3.8 リソース

- [GitHub Copilot をカスタマイズするための指示ファイル][instruction-files]
- [GitHub Copilot app のカスタマイズ][customize-app]
- [カスタム指示を作成するためのベストプラクティス][instructions-best-practices]
- [Awesome Copilot - 指示ファイルなどのリソース集][awesome-copilot]

[next-lesson]: 4-build-filtering.md
[instruction-files]: https://docs.github.com/en/copilot/concepts/prompting/response-customization
[path-instructions]: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions#creating-path-specific-custom-instructions
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[awesome-copilot]: https://awesome-copilot.github.com/
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support
[ui-instructions]: https://github.com/iwizsophy/dev-days-tailspin-template/blob/v2026.10.03/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/iwizsophy/dev-days-tailspin-template/blob/v2026.10.03/.github/instructions/astro.instructions.md
[managing-issues-prs]: https://docs.github.com/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests
