---
title: "演習 6 - GitHub Copilot CLI のカスタムエージェント"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

## カスタムエージェントとは

GitHub Copilot の[カスタムエージェント（Custom Agents）][custom-agents-concept]を使用すると、開発ワークフロー内の特定のタスクや専門領域に特化した AI アシスタントを構築できます。リポジトリ内の `.github/agents` フォルダーに Markdown ファイルを配置することで、焦点を絞った指示（focused instructions）、ベストプラクティス、コーディングパターン、およびドメイン固有の知見をエージェントに与え、特定分野の作業を極めて高い精度で遂行させることができます。

開発チームは、自チームの専門知識を再利用可能なエージェントとして標準化できます。たとえば、[WCAG][wcag] への適合を徹底するアクセシビリティエージェント、セキュアコーディング規約を監査するセキュリティエージェント、厳格なテストカバレッジを維持するテスティングエージェントなどが典型例です。

カスタムエージェントは、リポジトリの `.github/agents` フォルダー（または端末のグローバル環境 `~/.copilot/agents`）にある Markdown ファイルで定義します。各ファイルには、少なくとも `name` と `description` を含む YAML frontmatter が必須であり、それに続いてエージェントのペルソナ、専門知識、指示文を Markdown で記述します。

### カスタムエージェントとエージェントスキルの違い

カスタムエージェントと[エージェントスキル][agent-skills-concept]は、どちらも主に Markdown ファイルで定義されるため概念的な近しさがありますが、その役割分担は明確です。**カスタムエージェントが「作業者（専門家）」**であるのに対し、**エージェントスキルは作業者が手に取る「道具（ツール）」**にあたります。

カスタムエージェントは独自の独立したコンテキストウィンドウを保持し、作業プロセスの中で複数のスキル（場合によっては他のエージェント）をオーケストレーション（統合管理）して課題を解決します。本演習で扱うアクセシビリティエージェントは、ガイドラインに照らしてサイトをレビュー・改修する過程で、単体テスト実行スキルや pull request 作成用スキルを自律的に呼び出して作業を完走させます。

> [!NOTE]
> カスタムエージェントのプロンプト構成に単一の絶対解はありません。実際の開発シナリオに合わせてテストと反復を行い、最適な指示をブラッシュアップしてください。

[custom-agents-concept]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[agent-skills-concept]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[wcag]: https://www.w3.org/WAI/standards-guidelines/wcag/

## シナリオ

多くの Web アプリケーションでは、アクセシビリティへの配慮が不足しがちです。Tailspin Toys のクラウドファンディングサイトも例外ではありません。視覚特性や好みの異なるすべてのユーザーにとって利用しやすいプラットフォームを目指すため、アクセシビリティ専用のカスタムエージェントを投入して改修を行います。

ユーザーからのフィードバックにより、現在のダークテーマは文字と背景色のコントラスト比が不十分で視認性が低いという課題が判明しました。この問題に対処するため、デザインチームはユーザーが手動でオン／オフを切り替えられるハイコントラストモードの実装を求めています。

この演習では、次の内容を学習します。

- リポジトリに定義されたアクセシビリティカスタムエージェントの構成を確認する
- Copilot CLI からカスタムエージェントを呼び出し、タスクを委譲して自律実装させる

## アクセシビリティカスタムエージェントを確認する

> [!NOTE]
> **付属エージェントの YAML 構文エラーに関する注意**  
> 2026年9月8日時点のテンプレート環境において、`/agent` コマンドを実行した際に `.github/agents/pr-readiness.md` の YAML 解析で `unknown escape character` エラーが発生する事例がありました。もしこのエラーが表示された場合は、該当ファイルの `tools` セクションにある `"playwright/\*"` を `"playwright/*"` へ修正してください（YAML のダブルクォート文字列内では `\*` は無効なエスケープシーケンスです）。修正後に CLI を再起動することでエラーが解消します。なお、本演習で使用する Accessibility agent 自体は正常に選択可能です。

リポジトリにあらかじめ用意されているアクセシビリティエージェントの定義を確認します。

1. `.github/agents/accessibility.md` を開きます。
2. 先頭の `name` および `description` を含む YAML frontmatter を確認します（これらはエージェント定義において必須の項目です）。
3. 続く Markdown 本文の各セクションを読み込みます。
   - アクセシブルな Web サイトを構築する際の中核的責務
   - WCAG に準拠したコントラスト比やセマンティック HTML のベストプラクティス
   - HTML、CSS、JavaScript の具体的実装パターン
   - アクセシビリティ対応で陥りがちな典型的なアンチパターン

## Copilot CLI でカスタムエージェントを使う

> [!NOTE]
> **対応する Issue が存在しない場合の対処**  
> 2026年9月8日時点のテンプレートでは、高コントラストモードに関する Issue があらかじめ起票されていない場合があります。演習リポジトリの Issue 一覧を確認し、該当 Issue が見当たらない場合は、後述のプロンプト内にある「詳細はリポジトリの関連 Issue を取得して確認してください。」の部分を、次のように置き換えて送信してください。  
> 「関連 Issue はありません。以下を今回の要件として、この演習リポジトリ内に Issue を作成してから実装してください。」（リポジトリの `CONTRIBUTING.md` では PR に紐づく Issue の存在が求められているためです）。

Copilot CLI で `/agent` コマンドを実行し、アクセシビリティエージェントを起動してタスクを依頼しましょう。

> [!TIP]
> **Copilot CLI セッションの開始方法**  
> Codespace のターミナルで、次のオプションを指定して Copilot CLI を起動します。
>
> ```bash
> copilot --yolo --enable-all-github-mcp-tools
> ```
>
> 既存のセッションを引き継ぐ場合は `copilot --yolo --enable-all-github-mcp-tools --continue` を実行します。すでに起動中の場合は `/clear` を送信して新しい会話を開始してください。

> [!CAUTION]
> `--yolo` オプションは、ツール実行やファイル変更時の確認ダイアログをすべて省略する完全自動化フラグ（`--allow-all-tools`、`--allow-all-paths`、`--allow-all-urls`）を有効にします。Codespace や仮想マシンのような分離された安全な環境でのみ使用し、日常的なローカル開発の既定エイリアスとして設定しないよう注意してください。詳しくは [ツールの許可と拒否に関するドキュメント][allow-all-warning] を参照してください。

[allow-all-warning]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools

1. Copilot CLI の対話プロンプトで `/agent` と入力し、<kbd>Enter</kbd> を押します。
2. 表示されたエージェント一覧から **Accessibility agent** を選択します。
3. 次のプロンプトを入力し、アクセシビリティのレビューと高コントラストモードの実装を指示します。

   ```plaintext
   サイトのアクセシビリティをレビューしてください。詳細はリポジトリの関連 Issue を取得して確認してください。ページを再読み込みしても設定が維持される高コントラストモードの切り替えを実装し、変更に対する e2e テストを用意してください。その後、変更を含む PR を作成してください。
   ```

4. エージェントがタスクの自律処理を開始します。Issue の要件を分析し、コードの改修と E2E テストの追加を行い、最後に前章で確認した `make-contribution` スキルを自動的に呼び出して pull request を起票する一連の流れを確認してください。

> [!NOTE]
> この処理の完了には数分かかる場合があります。エージェントがテストを実行し、自己修正を繰り返しながら PR を仕上げていくログを眺めて待ちましょう。

## まとめと次のステップ

特定領域の専門知識をカプセル化した [カスタムエージェント][custom-agents] を活用しました。本演習で実施した主な内容は次の通りです。

- カスタムエージェントの構造（YAML frontmatter と指示本文）およびスキルとの役割分担を理解した
- `/agent` コマンドを用いて Accessibility agent を呼び出し、高コントラスト機能の実装からテスト・PR 作成までを自律実行させた

次は、Copilot CLI をより柔軟に制御するための各種スラッシュコマンドを網羅し、コンテキスト管理やモデル選択のテクニックを学習します。[演習 7 - スラッシュコマンド][next-lesson] へ進んでください。

## リソース

- [カスタム エージェント][custom-agents]
- [リポジトリ用カスタム エージェントの作成][creating-custom-agents]
- [awesome-copilot のカスタム エージェント][awesome-copilot-agents]
- [organization で custom agent を使う準備][org-custom-agents]
- [enterprise で custom agent を使う準備][enterprise-custom-agents]

[previous-lesson]: 5-agent-skills.md
[next-lesson]: 7-slash-commands.md
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[creating-custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
[awesome-copilot-agents]: https://github.com/github/awesome-copilot/tree/main/agents
[org-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents
[enterprise-custom-agents]: https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents
