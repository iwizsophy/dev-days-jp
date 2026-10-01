---
title: "レッスン 1 - GitHub Copilot app のインストール"
description: "GitHub Copilot app をインストールし、テンプレートから作成したリポジトリを接続して、ワークスペースを確認し、クイックチャットを試します。"
authors:
  - geektrainer
lastUpdated: 2026-09-13
---

> **この章の確認範囲：**
> 2026年9月13日に Windows の App 1.1.20 で、インストール、サインイン後の初期設定、プロジェクト追加入口、Chats の応答、および Open folder で追加した演習用コピーの読み取り応答を確認しました。さらに、GitHub 連携プロジェクトの追加により、My work で8件のバックログ Issue が表示されることも確認済みです（詳細は [実走記録](../material/verification.md) および [UI 確認表](../material/ui-check.md) を参照）。

[**GitHub Copilot app**][about-copilot-app] は、エージェント主導の開発に特化したデスクトップアプリケーションです。GitHub Copilot CLI を基盤とし、GitHub のリポジトリ、ブランチ、CI パイプラインとネイティブに統合されています。すべての作業を開発者自身が手動で行うのではなく、それぞれ独立して分離されたワークスペース（worktree）上で複数のエージェントを並列に動作させ、日常の開発タスクを自動化できるよう設計されています。

Node.js の準備と演習用リポジトリの作成が完了したため、本レッスンではアプリをインストールし、リポジトリを接続してワークスペースの構造を確認します。

本レッスンでの到達目標は次の4点です。
- GitHub Copilot app をインストールし、GitHub アカウントでサインインする。
- GitHub リポジトリから演習プロジェクトをアプリに追加する。
- テンプレートによって自動生成されたバックログ Issue を含め、ワークスペースの各領域を確認する。
- クイックチャットを試し、アプリ自体の仕組みについて質問する。

## シナリオと利用条件

開発チームは、増え続けるバックログを効率的に消化するため AI エージェントの導入を進めています。Copilot app を利用することで、Issue の選定、エージェントへの実装指示、変更差分のレビュー、Pull Request の作成とマージまでを一元的に管理できます。本レッスンでは、アプリのセットアップを行い、プロジェクトについての対話を開始できる状態を整えます。

> [!NOTE]
> アプリの利用には有効な Copilot プランが必要です（公式ドキュメントでは Free を含む全プランが対象です。演習の完走に必要な利用枠は事前に確認してください）。また、Copilot Business または Copilot Enterprise を利用している組織では、管理者が **GitHub Copilot app** ポリシー（CLI 用ポリシーとは別個）を有効化している必要があります。

## GitHub Copilot app をインストールして構成する

Windows、macOS、Linux 向けにインストーラーが提供されています。アプリを導入・認証し、演習用リポジトリを追加します。

1. ブラウザーで [GitHub Copilot app のダウンロードページ][download-app] を開きます。
2. 使用している OS 向けのインストーラーをダウンロードし、画面の指示に従ってインストールします。
3. インストール完了後、Copilot app を起動します。
4. **Sign in to GitHub** を選択し、ブラウザーが開いたら認証を完了させます（※Windows App 1.1.20 では別の選択肢として **Sign in to GitHub Enterprise Cloud (*.ghe.com)** も表示されましたが、これは GitHub Enterprise Server への接続を保証するものではありません）。
5. 認証完了後、リポジトリの接続画面（**Connect your repositories**）が表示されます。候補一覧に演習コピーが表示されていない場合は **Add from GitHub** から検索できますが、本教材の実機検証では、ここでは選択せずオンボーディング完了後にサイドバーから追加する手順で動作を確認しています。
6. **Continue** を選択して進みます。
7. テーマ（外観）の選択画面が表示されたら、好みのテーマを選んで **Finish** を押します。

### プロジェクト接続における重要事項（Open folder と GitHub 連携の回避策）

初期設定完了後のプロジェクト追加入口は、サイドバーの **Projects** 横にある **`+`**（New project or session）です。ここから **Add GitHub repository**、**Clone repository**、および **Open folder** を選択できます。

> [!WARNING]
> **Open folder 経路における停滞と回避手順**：
> ローカルに既存のフォルダーを直接開く **Open folder** 経路では、Windows App 1.1.20 の実機確認において次の問題が確認されています。
> - 設定レビュー画面で **Accept and apply** を押した後も画面が停滞し、プロンプト入力欄が表示されない
> - エージェントによる Pull Request 作成ツールがアカウント連携エラーで失敗する
>
> このため、本教材では次の手順を標準とします。
> 1. **Projects の `+` → Add GitHub repository** から自身の演習コピーを追加する
> 2. **GitHub 連携プロジェクト** としてセッションを開始する
>
> この経路であれば、設定承認後に入力欄へ正常に遷移し、専用 worktree の作成後に依存関係が導入され、**Run options → Build static site** での 24 ページ静的生成（Complete!）が確認できています。
> ※設定画面を通過しただけで準備完了と判断せず、実際のビルド成否まで確認してください。なお、これは教材を進めるための「操作的回避策」であり、App 本体の不具合修復を意味するものではありません。

> [!IMPORTANT]
> **途中から切り替える場合の注意**：
> ローカルフォルダー（Open folder）側で加えた未コミットの変更は、GitHub 連携の新しい worktree へ自動的には移行されません。もし切り替えが必要になった場合は、変更を確実に保存・コミットした上で講師と引き継ぎを行ってください。最初から GitHub 連携側を使用していれば、この作業ツリー間の移動を避けられます。

## 2. ワークスペースの構造を確認する

プロジェクトを接続したら、アプリの主要な作業領域を確認します。サイドバーは次のセクションで構成されています。

- **Projects**：プロジェクトとエージェントセッションを管理する領域（上流原本の英語表記「Sessions」から変更）。実装用セッションおよび独立した worktree の実走は次章以降で体験します。
- **Chats**：リポジトリの作業ツリーやブランチを作成せず、単発の質問や相談を行える会話領域（上流原本の「Quick chats」に対応）。
- **My work**：**GitHub ネイティブ統合** により、リポジトリに紐づく Issue や Pull Request を直接一覧表示・操作する領域。Issue の検索・絞り込み、CI ステータスの確認、Issue を起点としたセッション開始、PR の差分レビューが可能です。
- **Automations**：スケジュール実行やオンデマンド実行を行う、保存済みのエージェント自動化タスクを管理する領域（演習8で作成します）。
- **Customize**：MCP サーバー、Plugins、Skills、Extensions、Canvas、および Installed の各設定・管理画面を開く入口。

### バックログ Issue の確認

GitHub との連携により、リポジトリ内の待機中タスクがアプリ内に直接同期されます。

1. サイドバーで **My work** を選択します。
2. テンプレート作成時に自動生成された 8 件のバックログ Issue が表示されていることを確認します。本ワークショップでは、特に次の 3 件を中心に開発を進めます。
   - `Allow users to filter games by category and publisher`（フィルター機能の実装）
   - `Update our repository coding standards`（コーディング規約・ドキュメント標準の追加）
   - `Implement pagination on the game list page`（ページネーション機能の実装）
3. 任意の Issue を選択して詳細を確認します。各 Issue は、後続のレッスンでエージェントセッションを開始する起点となります。

> [!NOTE]
> `Open folder` のみで追加した状態では、実走時に **My work** に「No GitHub repositories yet」と表示されました。その場合は **Add GitHub repository** から自身の `owner/repo` を検索・追加してください。GitHub 連携プロジェクトが追加されると、8 件の Issue が正しく表示されます（ローカルプロジェクトとは別枠で管理されるため、画面上部の **All repositories** 等で現在の操作対象リポジトリを確認してください）。

## 3. クイックチャット（Quick Chat）を試す

ブランチや worktree を作成せず、その場限りの質問やアイデア出しを行いたい場合は **Chats** が適しています。アプリ自身の仕組みについて質問してみましょう。

1. サイドバーの **Chats** の横にある **`+`**（New chat）を選択します（入力欄の下部のモードが **Chat** になっていることを確認します）。
2. プロンプト入力欄に次のテキストを入力し、送信します。

    ```plaintext
    GitHub Copilot app は worktree をどのように使いますか？
    日本語で簡潔に説明してください。説明だけを行い、ファイル変更、
    リポジトリ操作、コマンド実行はしないでください。
    ```

3. 送信後、会話ビューに日本語での解説が返答され、処理完了後にステータスが **Idle** に戻ることを確認します（※この回答はエージェント自身による解説であり、worktree の実動作の証明ではありません。実際の実装セッションにおける worktree 分離は次章以降で確認します）。

### チャット一覧のコンテキストメニュー確認
完了したチャット項目を **Chats 一覧で右クリック** すると、次の項目が表示されることを実機確認しました。
- `Rename`、`Pin`、`Mark as unread`、`Show in Explorer`、`Share as secret gist`、`Copy`、`Archive`、`Delete`

※今回の実機検証ではメニュー項目の表示確認のみを行っており、共有、削除、アーカイブ等の実行は行っていません。また、これらの項目が過去の常設メニューから移行したものなのか、あるいは実装用セッションにも同様の項目が存在するのかは未特定の状態です。

<a id="cli-fallback"></a>

> [!WARNING]
> **講師向け緊急対応**：
> 受講者の環境トラブル等により作業保全が緊急に必要な場合のみ、[講師専用 CLI 対応手順](../material/emergency-cli.md#chapter-1) を参照してください。CLI で質問・確認を代替した場合、この章の App 操作体験は「未完了」として記録します。

## まとめと次のステップ

GitHub Copilot app をインストールし、プロジェクトを接続してワークスペースを確認しました。
- アプリをインストールして GitHub アカウントでサインインした
- GitHub リポジトリから演習プロジェクトを追加した
- ワークスペースの構造を確認し、**My work** で用意されたバックログ Issue を確認した
- クイックチャットを使って、その場限りの質問を試した

次は最初のエージェントセッションを開始し、ゲームカードに星評価を表示する最初の変更をプロジェクトに加えます。[レッスン 2「最初のエージェントセッションの実行」][next-lesson] に進んでください。

## リソース

- [GitHub Copilot app について][about-copilot-app]
- [GitHub Copilot app の概要][getting-started]
- [GitHub Copilot app でのエージェントセッションの操作][agent-sessions]

[ex0]: 0-prerequisites.md
[next-lesson]: 2-add-star-rating.md
[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[agent-sessions]: https://docs.github.com/copilot/how-tos/github-copilot-app/agent-sessions
[download-app]: https://gh.io/app
