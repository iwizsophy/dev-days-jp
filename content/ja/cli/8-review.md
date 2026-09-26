---
title: "演習 8 - 振り返りと次のステップ"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

本演習コースを通じて、GitHub Copilot CLI を活用したエージェント型開発における中核的なユースケースを実践してきました。これまで習得した主な内容は次の通りです。

- GitHub や Playwright を含む各種 MCP サーバーとの連携
- 指示ファイル（Instruction files）によるプロジェクト規約やアーキテクチャの統制
- エージェントスキル（Agent Skills）の実装による、反復タスクの標準化と自動化
- カスタムエージェント（Custom Agents）の導入による、専門領域（アクセシビリティ等）の自律的課題解決
- スラッシュコマンド（Slash commands）によるコンテキスト管理、モデル切り替え、および Cloud agent への委任

本章では、主要なスラッシュコマンドの総括、エージェント活用のベストプラクティス、および今後の学習ロードマップを確認しましょう。

## 主要なスラッシュコマンド一覧

GitHub Copilot CLI には、エージェントの挙動制御や内部状態の可視化を支援する多彩なスラッシュコマンドが備わっています。これまでに使用した会話リセットの `/clear` や MCP 管理の `/mcp` に加え、日々の開発で役立つ代表的なコマンドは以下の通りです。

| コマンド | 説明 |
|---|---|
| `/add-dir` | Copilot の信頼リストに指定ディレクトリを追加する |
| `/clear`, `/new` | 会話履歴をリセットしてクリーンなセッションを開始する |
| `/compact` | 会話履歴を要約圧縮し、コンテキストウィンドウの消費量を削減する |
| `/context` | 現在のトークン消費状況とコンテキストの内訳を視覚的に表示する |
| `/diff` | 現在の作業ツリーでエージェントが加えたコード差分をレビューする |
| `/model` | セッションで使用する LLM モデル（Claude Sonnet、GPT 等）を選択・切り替える |
| `/plan <prompt>` | コーディング着手前に実装方針と手順を定めた計画を作成する |
| `/review <prompt>` | コードレビュー用エージェントを呼び出し、コード変更の品質を精査する |
| `/delegate` | 時間のかかるタスクを GitHub の Cloud agent へ委任して非同期実行させる |
| `/session` | 現在のセッションメタ情報およびワークスペースの概要を表示する |
| `/share` | セッションの全履歴を Markdown ファイルまたは GitHub gist として出力・共有する |
| `/skills` | エージェントの能力を拡張するスキルの状態を確認・管理する |
| `/usage` | セッション内のトークン消費量メトリクスと統計情報を表示する |

> [!TIP]
> `/help` コマンドを実行すると、利用可能な全スラッシュコマンドおよびキーボードショートカットの一覧を確認できます。

## エージェント活用のベストプラクティス

AI コーディングツールを活用する際、生成されるアウトプットの品質を決定づけるのは、**ツールの周辺に整備されたコンテキスト基盤**です。本ワークショップで体験した通り、指示ファイル、スキル、カスタムエージェントがそれぞれ重要な役割を果たしました。これらの資産を整備し、チーム内で再利用可能な形でリポジトリへ蓄積していくことが極めて重要です。[awesome-copilot][awesome-copilot] はテンプレートの優れた情報源であり、Copilot 自身に指示ファイルやスキルのひな形を生成させるアプローチも有効です。

基盤の整備と並んで重要なのが、**提示するコンテキストの明晰性**です。何を作りたいのか、なぜそれが必要なのか、どのような制約条件や設計方針で進めるべきかを明確に提示することで、エージェントのコード生成精度は劇的に向上します。エージェントの判断材料となる情報は、可能な限り具体的にプロンプトや指示ファイルへ含めてください。

## 次のステップ

AI エージェントを自在に使いこなす最良の道は、日々の開発業務や個人プロジェクトで継続的に使い続けることです。プロダクションコードの改修、趣味のプログラミング、温めていたアイデアのプロトタイプ構築など、多様な場面で活用してください。得られた知見やプロンプトの工夫をチームへ共有し、チーム固有の指示ファイルやスキルを育てていきましょう。

GitHub Copilot エコシステムの全容をさらに深く学ぶには、以下の関連教材も合わせて参照してください。

- [VS Code ハーネス][vscode-harness-link]
- [Cloud agent ハーネス][cloud-harness-link]

## リソース

- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI を使う][using-copilot-cli]
- [Awesome Copilot リポジトリ][awesome-copilot]
- [Custom instructions ガイド][repo-instructions]
- [Agent Skills ドキュメント][agent-skills]
- [カスタム エージェント ドキュメント][custom-agents]
- [MCP 仕様][mcp-spec]

[previous-lesson]: 7-slash-commands.md
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[awesome-copilot]: https://github.com/github/awesome-copilot
[repo-instructions]: https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions
[agent-skills]: https://docs.github.com/copilot/concepts/agents/about-agent-skills
[custom-agents]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents
[mcp-spec]: https://modelcontextprotocol.io/
[vscode-harness-link]: https://github-samples.github.io/copilot-workshops/vscode/
[cloud-harness-link]: https://github-samples.github.io/copilot-workshops/cloud/
