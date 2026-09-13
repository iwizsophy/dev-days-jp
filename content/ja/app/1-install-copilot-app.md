---
title: "レッスン 1 - GitHub Copilot app のインストール"
description: "GitHub Copilot app をインストールし、テンプレートから作成したリポジトリを接続して、ワークスペースを確認し、クイックチャットを試します。"
authors:
  - geektrainer
lastUpdated: 2026-09-13
---

> **この章の確認範囲：** 2026年9月13日に Windows の App 1.1.20 で、インストール、サインイン後の初期設定、プロジェクト追加メニュー、Chats の応答、Open folder で追加した演習用コピーの読み取り応答を確認しました。GitHub 連携プロジェクトの追加後、My work で8件のバックログ Issue の表示も確認しました。[実走記録](../material/verification.md)と [UI 確認表](../material/ui-check.md)を参照してください。


[**GitHub Copilot app**][about-copilot-app] は、エージェント主導の開発に使用するデスクトップアプリケーションです。GitHub Copilot CLI を基盤とし、GitHub とネイティブに統合されているため、リポジトリ、ブランチ、CI パイプラインをすぐに利用できます。すべての作業を自分で行うのではなく、複数のエージェントをそれぞれ分離されたワークスペースで並列に指示し、繰り返し発生するタスクを自動化するワークフロー向けに設計されています。Node.js のインストールとプロジェクトのコピーが完了したので、次はアプリをインストールして、そのリポジトリを接続します。

このレッスンでは、次の内容を学習します。

- GitHub Copilot app をインストールしてサインインする。
- GitHub リポジトリからプロジェクトをアプリに追加する。
- テンプレートによって用意されたバックログを含め、ワークスペースを確認する。
- クイックチャットを試して、アプリ自体について学ぶ。

## シナリオ

チームは、増え続けるバックログに対応するために AI エージェントを導入しています。Copilot app では、Issue の選択、エージェントの実行、変更のレビュー、pull request のマージを一か所から指示できます。このレッスンでは、アプリをインストールして接続し、プロジェクトについての会話を始められるようにします。

> [!NOTE]
> 有効な Copilot プランが必要です。公式情報では Free を含む全プランが対象です。必要な利用枠は事前に確認してください。Copilot Business または Copilot Enterprise を使用している場合、アプリを動作させるには管理者が **GitHub Copilot app** ポリシー（CLI のポリシーとは別）を有効にする必要があります。

## GitHub Copilot app をインストールして構成する

GitHub Copilot app を使用するには、まずアプリをインストールします。Windows、macOS、Linux 向けのバージョンが用意されています。アプリをインストールして認証し、Tailspin Toys リポジトリを追加します。

1. ブラウザーで [GitHub Copilot app のランディングページ][download-app]を開きます。
2. 使用しているプラットフォーム向けのアプリをダウンロードし、ランディングページの手順に従ってインストールします。
3. インストールが完了したら、アプリを開きます。
4. **Sign in to GitHub** を選択し、画面の指示に従って認証します。Windows の App 1.1.20 では、別の入口として **Sign in to GitHub Enterprise Cloud (*.ghe.com)** が表示されました。これは GitHub Enterprise Server の接続確認を意味しません。
5. 認証後、**Connect your repositories** が表示されます。演習用コピーが候補になければ **Add from GitHub** で探します。この実走では何も選択せず、後から追加する流れで確認しました。
6. **Continue** を選択してオンボーディングを続けます。
7. テーマの選択を求められたら、最も好みのものを選び、**Finish** を選択します。

> [!NOTE]
> 初期設定後の追加入口は、サイドバーの **Projects** の **+**（New project or session）→ **Add GitHub repository** です。同じメニューに **Clone repository** と **Open folder** も表示されます。ローカルに取得済みの自分用コピーを使う場合は、**Open folder** → コピーのフォルダーを選択します。この経路では既存の checkout を直接使うセッションを確認しました。設定確認が出たら **Review configuration** で内容を読み、自分の判断で **Accept and apply** を選択してください。

> [!NOTE]
> Windows App 1.1.20 の **Open folder** では、**Accept and apply** 後も確認画面が残りました。教材では **Add GitHub repository** から演習コピーを追加し、その GitHub 連携プロジェクトで進めます。この経路では設定承認後に入力欄が表示され、新しい worktree の最初のセッション開始後に依存が導入されました。**Run options → Build static site** で24ページ生成と **Complete!** を確認しています。設定画面を通過しただけで準備完了とせず、ビルド結果まで確認してください。これは操作経路による回避であり、App 本体の不具合修正ではありません。

> **途中から切り替える場合：** ローカル側の未コミット変更が、新しい GitHub 連携 worktree に自動移動することはありません。変更を保存・確認してから講師と引き継ぎます。開始時点から GitHub 連携側を使用すれば、この移動を避けられます。Open folder 側の PR 作成時のアカウントエラーも、GitHub 連携側を使うことで回避します。GitHub 連携側では App の **Create PR** による作成・マージを実走済みです。

## ワークスペースを確認する

プロジェクトを接続したら、各領域を確認します。アプリのサイドバーは、主に次の領域で構成されています。

- **Projects** - プロジェクトとセッションを扱う領域です。参照原文の **Sessions** と表示名が異なります。実装用セッションと worktree の実走は次のレッスン以降で確認します。
- **Chats** - リポジトリを接続せずに質問できる会話です。参照原文の **Quick chats** に対応する入口として確認しました。このレッスンの最後に試します。
- **My work** - アプリの **GitHub ネイティブ統合**を通じて表示される Issue と pull request です。アプリを離れずに、Issue と pull request の参照や絞り込み、CI ステータスの確認、Issue からのセッション開始、pull request のレビューを行えます。
- **Automations** - スケジュールまたはオンデマンドで実行する、保存済みのエージェントタスクです。ハーネスの終盤で作成します。
- **Customize** - MCP、Plugins、Skills、Extensions、Canvas と Installed の各タブを開く入口です。

### 用意されたバックログを確認する

アプリは GitHub とネイティブに統合されているため、リポジトリで待機中の作業がアプリ内に表示されます。テンプレートからリポジトリを作成したときに、バックログとなる Issue が用意されています。表示されていることを確認します。

1. サイドバーで **My work** を選択します。
2. テンプレートはバックログに 8 件の Issue を用意しています。このハーネスでは次の 3 件に焦点を当てます。表示されていることを確認してください。

   - Allow users to filter games by category and publisher
   - Update our repository coding standards
   - Implement pagination on the game list page

3. Issue を選択して詳細を読みます。各 Issue はエージェントセッションの開始点にもなります。ハーネスの後半では、これらの Issue から作業を開始します。

> [!NOTE]
> **Open folder** だけで追加した状態では、実走時の **My work** は **No GitHub repositories yet** と表示されました。その場合は **Add GitHub repository** → 自分の `owner/repo` を検索 → 対象を選択します。GitHub 連携プロジェクトが追加され、演習コピーの8件の Issue が表示されることを確認しました。ローカルプロジェクトとは別項目になるため、以後は操作対象を確認してください。一覧上部の **All repositories** で対象を確認できます。

## クイックチャットを試す

アプリに慣れるには、アプリ自体について質問するのが効果的です。その用途には **quick chat** が適しています。Quick chats ではブランチや worktree を作成せずに質問やブレインストーミングができるため、セッションを必要としない、その場限りの簡単な質問に最適です。

1. サイドバーで **Chats** の横にある **+**（New chat）を選択します。入力欄の下が **Chat** であることを確認します。
2. アプリのセッションがどのように動作するかを尋ねます。

   ```plaintext
   GitHub Copilot app は worktree をどのように使いますか？
   日本語で簡潔に説明してください。説明だけを行い、ファイル変更、
   リポジトリ操作、コマンド実行はしないでください。
   ```

3. 送信ボタンを選択し、会話ビューで回答を読みます。2026年9月13日の実走では日本語の応答が返り、チャットが Idle になりました。回答は worktree の実動作の証拠ではありません。実装セッションでの分離は別途確認します。

完了したチャットを **Chats の一覧で右クリック**すると、**Rename**、**Pin**、**Mark as unread**、**Show in Explorer**、**Share as secret gist**、**Copy**、**Archive**、**Delete** が表示されました。この確認ではメニューを開いただけで、共有・削除・アーカイブは実行していません。これらの項目が過去の常設メニューから移動したか、実装用セッションにも同じ項目があるかは未確認です。

<a id="cli-fallback"></a>

> **講師向け：** 緊急の作業保全が必要な場合だけ [対応手順](../material/emergency-cli.md#chapter-1) を参照してください。CLI の実装成功は、この章の App 操作の完了には数えません。

## まとめと次のステップ

GitHub Copilot app をインストールし、プロジェクトを接続して、ワークスペースを確認しました。学習した内容は次のとおりです。

- アプリをインストールして GitHub にサインインする。
- GitHub リポジトリからプロジェクトを追加する。
- ワークスペースを確認し、**My work** で用意されたバックログを見つける。
- クイックチャットを使って、その場限りの簡単な質問をする。

次は、最初のエージェントセッションを開始し、ゲームカードに星評価を表示する最初の変更をプロジェクトに加えます。[レッスン 2「最初のエージェントセッションの実行」][next-lesson]に進んでください。

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
