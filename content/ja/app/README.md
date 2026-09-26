---
slug: ja-jp/app
title: "GitHub Copilot app"
authors:
  - geektrainer
lastUpdated: 2026-09-13
---

## この教材セットの進め方

本教材は、**GitHub Copilot App を用いた開発プロセスと操作体験を一連の流れとして学ぶ本編コース** です。演習0〜8を順番に進める構成となっており、単にコードを完成させることだけを目的とせず、エージェントセッションの管理、差分レビュー、MCP の連携、Agent Merge による自動マージ、キャンバスでの共同作業、および Automation による自動化まで、App の各機能を実際に体験して確認します。

### 画面画像と操作経路の留意点
- **掲載画像**：App 本編に掲載している画面画像は、2026年9月13日時点の Windows App 1.1.20 および GitHub Web の実機画面に基づいています。操作位置を示す例として後続章（検索機能や並べ替え Issue）の画面を用いている箇所がありますが、その場合は画像注記で区別しています。追加された13点の実機画像は画面全体を保持し、個人アカウントやリポジトリ名等の識別情報のみを灰色でマスクしています。
- **UI の相違への対応**：操作が見当たらない場合は、自己判断や推測で進めず、講師による現行 App の操作案内、ペア操作、または講師デモの順で対応してください。
- **緊急対応の位置づけ**：CLI 手順は作業を保全するための講師専用緊急対応であり、本編 App 演習を完了した代替経路とはみなしません。
- **リポジトリの分離**：演習の対象は各自の Tailspin Toys コピー環境です。参照元リポジトリへの push、Pull Request、Issue 作成は固く禁止されています。

### 関連リソースへのリンク
- [UI が異なるときの確認](../material/ui-check.md)
- [講師ガイド](../material/instructor.md)
- [章別の実走検証状況](../material/verification.md)

## GitHub Copilot App の概要

[**GitHub Copilot app**](https://docs.github.com/copilot/concepts/agents/github-copilot-app) は、Copilot CLI を基盤とするデスクトップアプリケーションであり、エージェント主導の開発環境を単一のワークスペースに統合します。
並列エージェントセッション、切り替え可能なセッションモード（Plan / Autopilot 等）、共有キャンバス、および GitHub Issue / Pull Request のネイティブ管理機能を備えています。さらに、リベース、レビュー指摘への対応、CI 失敗の修正から最終マージまでを自動で導く **Agent Merge** を利用できます。

本コースでは、アプリの導入と演習用プロジェクトの接続から始め、バックログに用意された Issue に沿って開発を進めます。
1. **星評価の追加**：小さな機能改修を通じて、セッションの開始から PR 作成・マージまでの基本サイクルを体験します。
2. **カスタム指示の標準化**：コーディング規約やドキュメント標準を指示ファイルに定義し、プロジェクトへ反映します。
3. **フィルター機能の自律実装**：独立したエージェントセッションで Plan モードと Autopilot モードを使い分け、スキルを活用して品質を検証します。
4. **外部ツール連携（MCP）**：Playwright MCP server を追加し、エージェント自身が実際のブラウザーを操作して動作を検証する手法を学びます。
5. **段階的マージの自動化**：最終段階として **Agent Merge** に PR の修正とマージを一任します。
6. **協調作業と自動化**：共有キャンバスでタスクを整理し、繰り返し発生する作業を Automation で自動化します。

アイデアの具体化から機能のマージに至る、AI 支援開発の包括的なライフサイクルを体験できます。

## レッスン一覧

| レッスン | トピック | 学習内容 |
| :--- | :--- | :--- |
| [0. 前提条件][ex0] | セットアップ | Node.js の準備と Tailspin Toys 演習用コピーの作成 |
| [1. Copilot app のインストール][ex1] | セットアップ | アプリの導入、リポジトリの接続、ワークスペースの確認 |
| [2. 最初のエージェントセッションの実行][ex2] | 最初の変更 | セッション開始、星評価の実装、最初の PR 作成と通常マージ |
| [3. カスタム指示による Copilot のガイド][ex3] | コンテキスト | Issue に基づくドキュメント標準（TSDoc）の追加とマージ |
| [4. Autopilot による機能の構築][ex4] | コア機能 | Plan / Autopilot モードによるフィルター実装とスキル検証 |
| [5. Playwright MCP によるテスト][ex5] | 外部ツール | Playwright MCP server を追加し、ブラウザーでの手動検証を実行 |
| [6. Agent Merge によるマージ][ex6] | マージ | Agent Merge による PR 修正と CI 連携自動マージ |
| [7. キャンバスを使った計画][ex7] | コラボレーション | 共有キャンバスを作成し、Issue の計画・追跡と実装連携を実行 |
| [8. 振り返りと次のステップ][ex8] | まとめ | 開発プロセスの振り返り、手動 Automation による要約実行 |

## 前提条件

このワークショップに参加する前に、次の環境を用意してください。

- [ ] 有効な Copilot プランが設定された GitHub アカウント（Free を含む。全演習を完走するのに十分な利用枠があるか事前確認）
- [ ] **macOS、Linux、Windows** のいずれかが動作する PC
- [ ] PC に[インストールされた Git][install-git]

> [!TIP]
> 有料プランを利用していない場合でも、認証済みの学生は [GitHub Education][callout-student-plan-education] を通じて GitHub Copilot を無料で利用できます。**Copilot Student** プランには、本ワークショップで使用するエージェント、MCP、コードレビュー、Copilot CLI の各機能が含まれています（演習の完走に必要な利用枠は別途確認してください）。

> [!NOTE]
> Copilot app はクラウド上の codespace ではなくローカル PC 上で直接実行するため、[レッスン 0][ex0] ではアプリをインストールする前に Node.js をインストールし、プロジェクトの演習用コピーを準備します。

> [!NOTE]
> Copilot Business または Copilot Enterprise を利用している組織では、アプリを使用するために組織管理者が **GitHub Copilot app** ポリシー（CLI のポリシーとは別個）を有効化している必要があります。

## はじめる

[**レッスン 0「前提条件」から始める →**][ex0]

[ex0]: 0-prerequisites.md
[ex1]: 1-install-copilot-app.md
[ex2]: 2-add-star-rating.md
[ex3]: 3-custom-instructions.md
[ex4]: 4-build-filtering.md
[ex5]: 5-mcp-playwright.md
[ex6]: 6-agent-merge.md
[ex7]: 7-canvases.md
[ex8]: 8-review.md
[install-git]: https://github.com/git-guides/install-git
[callout-student-plan-education]: https://github.com/education/students
