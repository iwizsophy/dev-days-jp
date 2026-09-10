---
title: "レッスン 1 - GitHub Copilot app のインストール"
description: "GitHub Copilot app をインストールし、テンプレートから作成したリポジトリを接続して、ワークスペースを確認し、クイックチャットを試します。"
authors:
  - geektrainer
lastUpdated: 2026-07-09
---

> **この章の進め方：** App を使える場合は以下の本文を進めます。UI で止まった場合は、[この章の CLI 代替手順](#cli-fallback)を使い、同じ章の合流条件を確認してください。


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
4. **Sign in to GitHub** を選択し、画面の指示に従って認証します。GitHub Enterprise Server を使用している場合は **Use GitHub Enterprise** を選択し、求められたらサーバーアドレスを入力します。
5. 認証後、リポジトリを接続するよう求められます。先ほど作成した `<YOUR_GITHUB_HANDLE>/tailspin-toys` という名前の Tailspin Toys リポジトリを選択します。
6. **Continue** を選択してオンボーディングを続けます。
7. テーマの選択を求められたら、最も好みのものを選び、**Finish** を選択します。

> [!NOTE]
> Tailspin Toys のコピーが一覧に自動的に表示されなかった場合は、アプリのオンボーディングを完了した後に追加できます。完了すると、Copilot app のホーム画面が表示されます。そこで **Choose from GitHub** を選択し、リポジトリ名 (\<YOUR_GITHUB_HANDLE\>/tailspin-toys) で検索して選択します。これでリポジトリが Copilot app に追加されます。

## ワークスペースを確認する

プロジェクトを接続したら、各領域を確認します。アプリのサイドバーは、主に次の領域で構成されています。

- **Sessions** - エージェントが作業する場所です。各セッションは分離された独自のワークスペースで実行されるため、変更が競合することなく複数のセッションを同時に実行できます。次のレッスンで最初のセッションを開始します。
- **Quick chats** - 独自のブランチやワークスペースを必要としない、質問やブレインストーミング向けの簡易的な会話です。このレッスンの最後に試します。
- **My work** - アプリの **GitHub ネイティブ統合**を通じて表示される Issue と pull request です。アプリを離れずに、Issue と pull request の参照や絞り込み、CI ステータスの確認、Issue からのセッション開始、pull request のレビューを行えます。
- **Automations** - スケジュールまたはオンデマンドで実行する、保存済みのエージェントタスクです。ハーネスの終盤で作成します。

### 用意されたバックログを確認する

アプリは GitHub とネイティブに統合されているため、リポジトリで待機中の作業がアプリ内に表示されます。テンプレートからリポジトリを作成したときに、バックログとなる Issue が用意されています。表示されていることを確認します。

1. サイドバーで **My work** を選択します。
2. テンプレートはバックログに 8 件の Issue を用意しています。このハーネスでは次の 3 件に焦点を当てます。表示されていることを確認してください。

   - Allow users to filter games by category and publisher
   - Update our repository coding standards
   - Implement pagination on the game list page

3. Issue を選択して詳細を読みます。各 Issue はエージェントセッションの開始点にもなります。ハーネスの後半では、これらの Issue から作業を開始します。

> [!NOTE]
> My work の項目一覧は自動的に絞り込まれ、Copilot app に追加したリポジトリの項目だけが表示されます。ほかのリポジトリの作業項目を表示するには、そのリポジトリをアプリに追加してください。

## クイックチャットを試す

アプリに慣れるには、アプリ自体について質問するのが効果的です。その用途には **quick chat** が適しています。Quick chats ではブランチや worktree を作成せずに質問やブレインストーミングができるため、セッションを必要としない、その場限りの簡単な質問に最適です。

1. サイドバーで **Quick chats** の横にある **+** を選択し、新しいチャットを開きます。
2. アプリのセッションがどのように動作するかを尋ねます。

   ```plaintext
   GitHub Copilot app は worktree をどのように使いますか？
   ```

3. 会話ビューで回答を読みます。各セッションが分離された独自の git worktree で実行されるため、変更が競合することなく複数のエージェントを並列実行できることがわかります。会話はいつでも継続でき、新しいチャットも開始できます。

<a id="cli-fallback"></a>

## CLI 代替手順：同じプロジェクトについて質問する

[共通の切り替え手順](../material/continuation.md)で作業場所を確認して `copilot` を起動します。求められたら自分の Copilot アカウントで認証し、フォルダーの信頼先が演習コピーであることを確認します。

```text
このリポジトリの構成、ゲームデータの取得方法、開発サーバーの起動方法、
テスト・lint・型チェックの方法を説明してください。ファイルは変更しないでください。
```

**合流条件：** Tailspin Toys の構成について応答し、README と回答が一致すること。App の Run・ターミナル・レビュー画面の説明は本文で読み、画面体験の未実施を記録します。次は同じコピーで演習2へ進みます。

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