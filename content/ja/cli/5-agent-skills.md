---
title: "演習 5 - エージェントスキルを使う"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

ソフトウェア開発においては、ビルドの生成、テストの実行、pull request の起票といった定型的な反復タスクが頻繁に発生します。**エージェントスキル（Agent Skills）**を活用することで、Copilot などの AI エージェントに対して、それらのタスクをどのような規約と手順で実行すべきか明確なガイダンスを提供できます。

スキルは、エージェントが必要に応じてオンデマンドで読み込む指示文、スクリプト、参照リソースをまとめたフォルダーです。[Agent Skills はオープン標準][agent-skills-repo]として策定されており、Copilot Chat（エージェントモード）、Copilot cloud agent、Copilot CLI、GitHub Copilot app の各環境で共通して動作します。

スキルはリポジトリ内の `.github/skills` フォルダー（または端末のグローバル環境 `~/.copilot/skills`）に配置します。各スキルフォルダーは、YAML frontmatter（`name` と `description`）を持つ `SKILL.md` ファイルと、それに続く Markdown 形式の指示文で構成されます。

```yaml
---
name: make-contribution
description: All changes to code must follow the guidance documented in the repository. Before any issue is filed, branch is made, commits generated, or pull request (or PR) created, a search must be done to ensure the right steps are followed. Whenever asked to create an issue, commit messages, to push code, or create a PR, use this skill so everything is done correctly.
---
```

必要に応じて、スクリプトや静的アセットをサブフォルダーに含めることも可能です（完全な構成仕様は [エージェントスキルの仕様書][agent-skills-spec] を参照してください）。

> [!TIP]
> スキルは実行時に動的に読み込まれます。エージェントは各スキルの `description` フィールドの記述を読み取り、現在のタスクに適したスキルを自律的に判断して適用します。そのため、スキルの目的と適用条件を明確に記述しておくことが、スキルが正しく呼び出されるための鍵となります。

[agent-skills-repo]: https://github.com/agentskills/agentskills
[agent-skills-spec]: https://agentskills.io/specification

本演習では、チームの pull request が定められた規約に厳密に従うよう、エージェントスキルを活用して PR を作成します。

## シナリオ

Tailspin Toys の開発チームでは、pull request（PR）の作成に関して以下のような厳格な品質基準を設けています。

- コミットメッセージを明確にし、変更ファイルを論理的な単位でグループ化する
- PR を起票する前に、すべての自動テストが通過していることを確認する
- PR 本文には、以下の必須セクションを必ず含める
  - 変更理由の説明
  - 変更されたファイルの一覧と概要
  - 重要なコードブロックの抜粋
  - 実施した変更の詳細な解説

エージェントに PR 作成を任せる際にも、これらのチーム基準を確実に遵守させたいと考えています。

この演習では、次の内容を学習します。

- pull request 作成用に定義された既存のスキル（`make-contribution`）の構造を確認する
- AI エージェントがどのようにスキルを認識し動的に読み込むかを理解する
- スキルのガイダンスに沿って、チームの基準を満たす PR を作成させる

## PR スキルを確認する

エージェントがチームのガイドラインに適合した PR を生成できるよう、あらかじめ用意されているスキルを確認しましょう。

1. `.github/skills/make-contribution/SKILL.md` を開きます。
2. 先頭の `name` と `description` を確認します。PR 作成、コミット作成、ブランチ作成を指示された際に呼び出すべきシナリオが定義されている点に注目してください。
3. ファイル全体をスクロールして確認します。ブランチの命名規則、コミットの構成方法、および PR 本文に記載すべき必須項目などのルールが体系化されていることを確認します。

## スキルを使って PR を作成する

前述の通り、スキルはプロンプトの意図に応じて Copilot CLI が自動的に判別して読み込みます。したがって、人間側は通常通り PR の作成を指示するだけで構いません。

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

1. Copilot CLI のプロンプトに次の指示を入力して送信します。

   ```plaintext
   この変更の pull request を作成してください。
   ```

2. Copilot がリクエストを受け付け、内部的に **make-contribution** スキルを検出して読み込んだ旨がターミナルに出力されます。
3. エージェントはスキルの指示手順に従い、まずテストを実行して安全性を確認したうえで、ブランチ作成、コミット作成、そして PR の起票を順次実行します。
4. PR が作成されたら、GitHub 上でその PR を開きます。本文の各セクションがスキルの指示通りに構成され、チーム要件を満たしていることを確認してください。
5. 次の演習に進む前に、今回のフィルター機能 PR と次章のアクセシビリティ対応作業を分離するため、ターミナルでローカルブランチを `main` から新しい作業ブランチへ切り替えておきます。

   ```bash
   git checkout main
   git pull
   git checkout -b feature/accessibility-cli
   ```

## まとめと次のステップ

エージェントスキルを活用し、チームの文書化された品質要件を満たす pull request を自律生成しました。本演習で実施した主な内容は次の通りです。

- pull request 作成用スキル（`make-contribution`）の構造と規約定義を確認した
- エージェントがプロンプトの意図に応じてスキルを動的に読み込む仕組みを理解した
- スキルのガイダンスに基づき、テスト実行から構造化された PR 作成までを完走させた

特定の単発タスクにはスキルが最適ですが、より高度で自律的な専門業務には [カスタムエージェント][next-lesson] の活用が適しています。次はカスタムエージェントの作成と利用を体験しましょう。

## リソース

- [Agent Skills について][about-agent-skills]
- [Agent Skills 仕様][agent-skills-spec]
- [Agent Skills リポジトリ][agent-skills-repo]
- [awesome-copilot の Agent Skills][awesome-copilot-skills]

[previous-lesson]: 4-mcp.md
[next-lesson]: 6-custom-agents.md
[about-agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[awesome-copilot-skills]: https://github.com/github/awesome-copilot/tree/main/skills
