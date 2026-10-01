---
slug: ja-jp/cli
title: "GitHub Copilot CLI"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

**[GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)** は、ターミナル環境で GitHub Copilot をエージェント型コーディングアシスタントとして活用できるツールです。コードベースの探索、コード生成、コマンド実行、外部ツール連携のすべてをコマンドライン上で行えます。GUI エディターへ作業コンテキストを切り替えることなく、開発の流れをスムーズに維持できます。

本演習コースでは、Copilot CLI のインストールと認証から始めます。カスタム指示によるプロジェクト固有コンテキストの提供や、Plan モードを用いた計画的な機能実装を順次体験します。さらに Playwright MCP サーバーを接続して実際のブラウザー上で機能を検証し、再利用可能なエージェントスキル（Agent Skills）やカスタムエージェントによって Copilot の機能を拡張します。最後に、コンテキスト管理・モデル選択・共有・Cloud agent への委任といったスラッシュコマンドを網羅し、学習内容を総括します。

## 演習一覧

| 演習 | トピック | 説明 |
|---|---|---|
| [0. 前提条件][ex0] | セットアップ | リポジトリと Codespace の準備 |
| [1. Copilot CLI のインストール][ex1] | インストール | Copilot CLI のセットアップと認証 |
| [2. カスタム指示][ex2] | コンテキスト | 指示ファイルの追加とエージェントの挙動確認 |
| [3. コード生成][ex3] | コード生成 | Plan モードを用いた機能の実装 |
| [4. Playwright MCP によるテスト][ex4] | 外部ツール | Playwright MCP サーバーの追加とブラウザー検証 |
| [5. エージェントスキル][ex5] | スキル | 専門タスク用スキルによる機能拡張 |
| [6. カスタムエージェント][ex6] | エージェント | カスタムエージェントの定義と実行 |
| [7. スラッシュコマンド][ex7] | CLI 機能 | コンテキスト、モデル選択、共有、Cloud agent への委任 |
| [8. 振り返り][ex8] | まとめ | 主要概念の総括と次のステップ |

## 前提条件

本ワークショップを開始する前に、以下の準備が完了していることを確認してください。

- [ ] 有効な GitHub Copilot プランが紐づいた GitHub アカウント（Free プランを含む。全演習を完走するのに十分な利用枠があることを事前に確認してください）
- [ ] ターミナルおよびコマンドライン操作に関する基礎知識
- [ ] インストールおよび初期設定が完了している Git 環境

> [!TIP]
> 認証済みの学生は [GitHub Education][callout-student-plan-education] を通じて GitHub Copilot を無償で利用できます。**Copilot Student** プランには、本ワークショップで使用するエージェント、MCP、コードレビュー、Copilot CLI の各機能が含まれています（対応機能および演習完走に必要な枠残量は各自でご確認ください）。

[callout-student-plan-education]: https://github.com/education/students

> [!NOTE]
> Copilot Business または Copilot Enterprise をご利用の組織では、管理者が Copilot CLI の利用ポリシーを有効化している必要があります。

## はじめる

**[演習 0: 前提条件から始める →][ex0]**

[ex0]: 0-prerequisites.md
[ex1]: 1-install-copilot-cli.md
[ex2]: 2-custom-instructions.md
[ex3]: 3-generating-code.md
[ex4]: 4-mcp.md
[ex5]: 5-agent-skills.md
[ex6]: 6-custom-agents.md
[ex7]: 7-slash-commands.md
[ex8]: 8-review.md
