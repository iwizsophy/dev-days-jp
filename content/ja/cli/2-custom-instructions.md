---
title: "演習 2 - カスタム指示 (Copilot CLI)"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[← 前のレッスン: Copilot CLI のインストール][previous-lesson] · [次のレッスン: CLI でコードを生成する →][next-lesson]

生成 AI を活用するにあたり、コンテキスト（文脈や設計意図）の提供は極めて重要です。特定の設計方針に沿ってタスクを実装させたい場合や、事前に知っておくべき前提知識がある場合は、それらを正確に伝達する必要があります。Copilot を補助するツールのうち、本演習ではまず[指示ファイル（Instruction files）][instruction-files]を取り上げます。指示ファイルは、コードに求める機能だけでなく、コードの構成方法や規約をエージェントに遵守させるための強力な手段です。

この演習では、次の内容を学習します。

- リポジトリ全体へのカスタム指示とパス単位の指示ファイルを通じて、プロジェクト固有の規約やドキュメント標準がどのように Copilot へ伝達されるかを理解する
- *既存の* 指示に従って、フィルター機能の第一歩となるデータアクセス関数（publishers helper）を生成する
- `.github/copilot-instructions.md` を編集し、リポジトリ全体に適用される新しいドキュメント標準を追加する
- 再度プロンプトを実行し、再生成されたコードが新しい標準（TSDoc やファイルヘッダー）を取り入れる様子を確認する
- 指示ファイルの更新と生成コードをコミットし、次章の実装準備を整える

> [!CAUTION]
> AI の出力は確率的に変動するため、指示を更新する前であってもドキュメントコメントが含まれる場合があります。本演習の目的は出力を一字一句一致させることではなく、指示ファイルを更新した後にエージェントの振る舞いの傾向がどう変化するかを体感することです。

## 指示ファイル（Instruction files）

### シナリオ

成熟した開発組織と同様に、Tailspin Toys にも開発プラクティスに関するガイドラインと要件が存在します。たとえば次のような項目です。

- データアクセス層には必ず単体テストを用意する
- UI はモダンなダークモードを採用する
- コード内ドキュメントは TSDoc 形式のドキュメントコメント（doc comment）として記述する
- 各ファイルの先頭には、モジュールの役割を説明するコメントブロックを配置する

指示ファイルを活用することで、これらのプラクティスに沿ってタスクを実行するために必要な情報を Copilot へ確実に提供できます。

### カスタム指示の構造

カスタム指示を使うと、Copilot にプロジェクト固有の前提や要件を正確に理解させることができます。希望するコーディング規約、採用ライブラリ、記述すべきコメントの粒度に至るまで指定でき、リポジトリ全体に一律適用するものと、特定ファイル種別のタスクに応じて適用するものの2階層で管理できます。

1. **リポジトリ全体の指示（`.github/copilot-instructions.md`）**  
   リポジトリに対する**すべての**リクエストで Copilot に送信される単一の指示ファイルです。採用技術スタック、アーキテクチャの概要、全体的なコーディング規約など、プロジェクト全体に関係するグローバルなガイダンスを記載します。
2. **パス固有の指示ファイル（`.github/instructions/*.instructions.md`）**  
   特定のタスクやファイル種類向けに作成する個別指示ファイルです。TypeScript や Astro などの特定言語向け規約、UI コンポーネント作成、単体テスト実装といった具体的タスクに応じたガイドラインを定義します。

> [!NOTE]
> IDE 上で作業する場合、指示ファイルはチャット（Copilot Chat）でのコード生成時にのみ参照され、インライン補完や次編集候補（next-edit suggestion）には使用されません。  
> 一方、Copilot Chat、Copilot CLI、Copilot cloud agent は、コード生成時にリポジトリ全体の指示ファイルと `*.instructions.md` ファイル（`applyTo` frontmatter 付き）の両方を自動参照します。  
> また、Copilot は AGENTS.md や CLAUDE.md といった他ツールの標準指示ファイルの取り込みにも対応しています。

### 指示ファイルを管理するためのベストプラクティス

本サンプルプロジェクトに含まれている構成は、代表的なベストプラクティスを示しています。

- `copilot-instructions.md` には、開発対象の概要、プロジェクト構造、全体的なコーディング規約など、プロジェクト共通のハイレベルなガイダンスを集約する
- `*.instructions.md` ファイルは、ファイル種別（単体テスト、Astro コンポーネント、データアクセス層）や個別タスクに特化した具体的な指示を記述する
- 明快な自然言語を用い、望ましいコード例（Good）と避けるべきコード例（Bad）を併記する

指示ファイルの記述に単一の絶対的な正解はありません。チームの文化や開発の進展に合わせて反復的に改善していくことが推奨されます。

> [!TIP]
> テンプレートや作成の出発点を探している場合は、指示ファイルやカスタムエージェントの実例が集約されているリポジトリ [awesome-copilot][awesome-copilot] を参考にしてください。

[ui-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/ui.instructions.md
[astro-instructions]: https://github.com/github-samples/tailspin-toys/blob/main/.github/instructions/astro.instructions.md
[awesome-copilot]: https://github.com/github/awesome-copilot
[custom-instructions-support]: https://docs.github.com/copilot/reference/custom-instructions-support

## このプロジェクトのカスタム指示ファイルを確認する

本リポジトリに配置されている指示ファイルを確認してみましょう。

1. `.github/copilot-instructions.md` を開きます。
2. プロジェクト概要に加えて、**Agent notes**、**Code standards**、**Scripts**、**Repository Structure** などのセクションが定義されていることを確認します。**Code standards** 配下には **GitHub Actions Workflows** の指針もネストされており、これらは Copilot との全対話に共通して適用されます。
3. `.github/instructions` フォルダーを展開し、配置されているファイルを確認します。Astro、Drizzle データレイヤー、単体テストなどに向けた指示ファイルが並んでいます。
4. `.github/instructions/unit-tests.instructions.md` を開きます。先頭の `applyTo` フィールドに注目してください。ここにはリポジトリルートを基準とする glob パターンが記述されており、指示を適用するファイル（例: `**/*.test.ts` に一致する TypeScript テストファイル）が限定されています。
5. 続けて `.github/instructions/drizzle.instructions.md` を開き、末尾までスクロールします。他の指示ファイル（`unit-tests.instructions.md` 等）やプロジェクト内の既存ファイルへの相対リンクが記載されている点に注目してください。指示セットを小規模かつ再利用可能なファイルへ分割し、コード生成時に参照すべき実例を Copilot に提示する構造になっています（ここに記載された相対パスは、リポジトリルートではなく指示ファイル自身の位置を基準とします）。

> [!NOTE]
> 現在の `copilot-instructions.md` の **Code formatting requirements** セクションにはコーディング標準が記載されていますが、コード内のドキュメントコメントに関する規則はまだ含まれていません。後続の手順で、TSDoc ドキュメントコメントおよびファイルヘッダーコメントの規約を追加します。

## ブランチを作成する

コードの変更作業を進めるため、専用の作業ブランチを作成します。

1. Codespace のターミナルで、新しいブランチを作成して切り替えます。

   ```bash
   git checkout -b feature/update-custom-instructions
   ```

2. Copilot CLI がインストールされ、認証済みであることを確認します。

   ```bash
   copilot --version
   ```

## 指示を更新する*前に* Copilot CLI を使う

カスタム指示の効果を比較検証するため、まずは現在の指示のままコードを生成させます。

> [!TIP]
> **Copilot CLI セッションの開始方法**  
> Codespace のターミナルで、次のオプションを指定して Copilot CLI を起動します。
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 既存のセッションを引き継ぐ場合は `copilot --yolo --enable-all-github-mcp-tools --continue` を実行します。すでに起動中の場合は `/clear` を送信して新しい会話を開始してください。  
> `--enable-all-github-mcp-tools` を指定すると、GitHub MCP の読み取り／書き込みツールが有効化され、エージェントがバックログの Issue を参照したり pull request を作成したりできるようになります。

> [!CAUTION]
> `--yolo` オプションは、ツール実行やファイル変更時の確認ダイアログをすべて省略する完全自動化フラグ（`--allow-all-tools`、`--allow-all-paths`、`--allow-all-urls`）を有効にします。Codespace や仮想マシンのような分離された安全な環境でのみ使用し、日常的なローカル開発の既定エイリアスとして設定しないよう注意してください。詳しくは [ツールの許可と拒否に関するドキュメント][allow-all-warning] を参照してください。

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. `.github/copilot-instructions.md` を自動認識させるため、Copilot CLI が**リポジトリのルートディレクトリ**で実行されていることを確認します。
2. Copilot CLI のプロンプトで、フィルター機能で使用する publishers helper の作成を指示します。

   ```plaintext
   すべての publisher の name と id の一覧を返すデータアクセス用 helper を、src/lib/publishers.ts に作成してください。まだテストは実行しないでください。
   ```

3. Copilot CLI はコードベースを探索し、計画を提示したうえでファイルを生成します。
4. 生成された `src/lib/publishers.ts` をエディターで開きます。
5. 第一引数に `db` クライアントを受け取り、publishers の型付き配列を返す関数が生成されていることを確認します（これは `.github/instructions/drizzle.instructions.md` に定義された規約が自動適用された結果です）。
6. この段階では、生成されたコードに TSDoc ドキュメントコメントやファイルヘッダーコメントが**含まれていない**ことを確認します。

## 新しいリポジトリ標準を追加する

`.github/copilot-instructions.md` を更新し、プロジェクト全体のコーディング規約にドキュメント作成ルールを追加します。

1. `.github/copilot-instructions.md` を開きます。
2. **Code formatting requirements** セクション（27行目付近）を探します。コード内ドキュメントに関するルールがまだ存在しないことを確認します。
3. 既存の規約リストの直下に、次の Markdown 行を追記します。

   ```markdown
   - export するすべての関数に、目的、引数、戻り値を説明する TSDoc コメントを付けてください。
   - import やコードの前に、そのファイルの目的を説明するコメントブロックを追加してください。
   ```

4. `copilot-instructions.md` を保存します。

## プロンプトを再実行して変化を確認する

指示ファイルにドキュメント規約を追加したので、先ほど生成したファイルを更新させます。

1. Copilot CLI のプロンプトで `/clear` を送信し、会話履歴をリセットします。
2. 次のプロンプトを送信します。

   ```plaintext
   src/lib/publishers.ts を、.github/copilot-instructions.md にある最新のドキュメント規約に従って更新してください。
   ```

3. 更新完了後、`src/lib/publishers.ts` をエディターで再確認します。
4. ファイルの先頭に、モジュールの役割を説明するファイルヘッダーコメントが追加されたことを確認します。

   ```typescript
   /**
    * Publisher data-access helpers for the Tailspin Toys Crowd Funding platform.
    * Provides functions to retrieve publisher information from the database.
    */
   ```

5. 生成された関数に、次のような TSDoc ドキュメントコメントが付与されていることを確認します。

   ```typescript
   /**
    * Returns a list of all publishers with their id and name.
    *
    * @param db - The Drizzle database client.
    * @returns A promise that resolves to an array of publisher objects.
    */
   ```

6. この更新されたファイルは、次章の実装の土台として使用するためそのまま保持します。

## 変更を検証してコミット・push する

> [!IMPORTANT]
> コミットを作成する前に、リポジトリの `.github/skills/quality-checks/SKILL.md` に従ってコードを検証します。Copilot CLI に「quality-checks スキルを使い、追加した helper の単体テストを用意して、既存のテスト、lint、型チェックを実行してください。失敗した場合は修正し、まだ commit はしないでください」と依頼してください。テストが成功することを確認したうえで、追加されたテストコードもコミット対象に含めます。

1. ターミナルで変更ステータスを確認します。

   ```bash
   git status
   ```

2. 更新した指示ファイル、ヘルパー関数、およびテストファイルをステージングします。

   ```bash
   git add .github/copilot-instructions.md src/lib/publishers.ts
   ```

3. 変更をコミットします。

   ```bash
   git commit -m "Add doc comment standards and publishers helper foundation"
   ```

4. ブランチをリモートリポジトリへ push します。

   ```bash
   git push -u origin feature/update-custom-instructions
   ```

## まとめと次のステップ

指示ファイルから Copilot がコンテキストを取得する仕組みを理解し、CLI を通じて以下の作業を完了しました。

- 既存の指示に従って、フィルター機能の土台となる publishers ヘルパー関数を生成した
- `.github/copilot-instructions.md` にリポジトリ共通のドキュメント規約を追加した
- プロンプトを再実行し、更新された指示に基づいて TSDoc やファイルヘッダーが正しく付与されることを確認した
- 変更内容を検証したうえでコミットし、リモートへ push した

次は、これらの指示を土台として、バックログの Issue に基づく本格的な機能実装を Plan モードで進めます。[演習 3 - コード生成][next-lesson] へ進んでください。

## リソース

- [GitHub Copilot のカスタマイズ用 instruction file][instruction-files]
- [custom instruction 作成のベスト プラクティス][instructions-best-practices]
- [Copilot 向けの custom instruction をより良く書くための 5 つのヒント][copilot-instructions-five-tips]
- [Awesome Copilot — instruction file などのリソース集][awesome-copilot]

[previous-lesson]: 1-install-copilot-cli.md
[next-lesson]: 3-generating-code.md
[instruction-files]: https://docs.github.com/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
[instructions-best-practices]: https://docs.github.com/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository
[copilot-instructions-five-tips]: https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/
