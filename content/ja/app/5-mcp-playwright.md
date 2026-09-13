---
title: "レッスン 5 - Playwright MCP server によるテスト"
description: "Playwright MCP server を GitHub Copilot app に追加し、実際のブラウザーでフィルター機能を手動テストするようエージェントに依頼します。"
authors:
  - geektrainer
lastUpdated: 2026-09-13
---

> **この章の確認範囲：** 2026年9月13日に Windows の App 1.1.20 で、MCP カタログ・Installed・Playwright の登録フォームを確認し、画像を撮影しました。リポジトリ定義は信頼承認と設定形式の修正後、3サーバーが Connected になりました。新規登録の保存とセッションからのツール実行は未確認です。[UI 確認表](../material/ui-check.md)を参照してください。


前のレッスンでは、プロジェクトの自動テストスイートを使ってフィルター機能を作成し、検証しました。テストによってコードの検証を自動化できますが、エージェント自身が動作を確認できるようにすることも効果的です。実際に作成している UI で問題を見つけた場合に、エージェントが対応できるようになります。MCP を使って AI エージェントに外部機能へのアクセスを提供する方法を確認し、Copilot が構築中のサイトを直接操作できるように Playwright MCP server を追加します。

このレッスンでは、次の内容を学習します。

- Model Context Protocol (MCP) の概要と、GitHub Copilot app での使用方法を理解する。
- アプリの設定から Playwright MCP server を追加する。
- エージェントにブラウザーを操作させ、フィルター機能を確認する。

## シナリオ

単体テストとエンドツーエンドテストは重要ですが、UI の更新を検証するには、実際に UI を操作する必要があります。変更作業をさらに自動化し、更新が期待どおりに動作するという確信を高めるために、ユーザーと同じ方法で Copilot が作業中の Web サイトを使用できるようにします。

## Model Context Protocol (MCP) とは

[Model Context Protocol (MCP)][mcp-blog-post] は、AI エージェントが外部のツールやサービスと通信するための手段を提供します。MCP を使うと、AI エージェントは外部のツールやサービスとリアルタイムで通信できます。その結果、最新情報へのアクセス (resources を使用) や、ユーザーに代わる操作 (tools を使用) が可能になります。

これらの tools と resources には、AI エージェントと外部のツールやサービスをつなぐ MCP server を通じてアクセスします。MCP server は、AI エージェントと外部ツール (既存の API や NPM パッケージなどのローカルツール) 間の通信を管理します。各 MCP server は、AI エージェントがアクセスできる異なる tools と resources のセットを表します。

よく使われる既存の MCP server には、次のものがあります。

- [**GitHub MCP Server**](https://github.com/github/github-mcp-server): GitHub リポジトリを管理するための API セットにアクセスできます。AI エージェントは、新しいリポジトリの作成、既存のリポジトリの更新、Issue と pull request の管理などを行えます。
- [**Playwright MCP Server**][playwright-mcp-server]: Playwright を使ったブラウザー自動化機能を提供します。AI エージェントは、Web ページへの移動、フォームへの入力、ボタンの選択などを行えます。

さまざまな tools と resources にアクセスできる MCP server がほかにも多数あります。GitHub は、エコシステム内での発見と貢献を促進するために [MCP registry](https://github.com/mcp) をホストしています。

> [!CAUTION]
> MCP server は、プロジェクト内のほかの依存関係と同様に扱ってください。使用する前にソースコードを慎重に確認し、発行元を検証して、セキュリティ上の影響を考慮します。信頼できる MCP server だけを使用し、機密性の高いリソースや操作へのアクセスを許可するときは注意してください。

## Playwright MCP server を追加する

2026年9月10日の [公式文書との照合](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app#configuring-mcp-servers)に加え、9月13日に Windows の App 1.1.20 で以下の表示を確認しました。プロジェクト未接続でも登録フォームまで開けます。

> **リポジトリ定義がある場合：** 検証コピーには `.mcp.json` に Playwright などが定義されていました。GitHub 連携プロジェクトを右クリック → Settings → MCP servers で確認します。Trust repository が表示された場合は、定義内容を確認して利用者が信頼を承認します。Repository configuration の Trusted 表示とは別です。重複登録せず、既存定義を確認してから以下の新規登録手順を使ってください。

### 既存の設定を読み込めない場合

実走では、本人による信頼承認後に **No MCP servers loaded** と表示されました。固定コミットから作ったコピーの `.mcp.json` は、ルートが `"servers"` でした。[公式のリポジトリ別設定形式](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers#adding-per-repository-mcp-servers)に合わせ、自分の演習コピーでこのキーを `"mcpServers"` に変更します。既存のサーバー定義・接続先はそのままにします。参照元リポジトリは変更しません。

Settings の **Refresh** で再確認します。今回の修正後は GitHub・Playwright・astro-docs の3件が **Connected** になりました。ただし、既存のフィルターセッションは Playwright のブラウザー操作ツールが利用できないと報告して停止しました。Connected の表示だけで章を完了にせず、セッションから実際にツールを呼べるか確認してください。セッションへの再読み込み方法と MCP によるブラウザー検証は未確認です。

### 新規登録の手順

1. サイドバーの **Customize** を開きます。
2. **Installed** タブの **MCP Servers** で既存の登録を確認します。登録済みなら重複して追加しません。実走時は未登録と表示されました。
3. 未登録なら **MCP** タブを開きます。実走時は **Featured** に **Playwright** が表示されました。見つからなければ **Search MCP servers** で検索します（検索操作は未検証）。
4. **Playwright** カードを選択し、登録フォームを開きます。実走時の初期値は **Server name** が `playwright`、種類が **Local**、**Command** が `npx`、**Arguments** が `-y @playwright/mcp@latest` でした。
5. 内容を確認して **Add server** で保存します。この保存操作以降は未検証です。導入後に **Installed** の登録状態とセッションからの利用可否を確認します。登録しただけで成功とはせず、次の節で実際のツール実行を確認します。

![App 1.1.20 の Customize の MCP タブ。Featured に Playwright と Add server が表示されている](../../_images/app-1.1.20-20260913-mcp-catalog.jpg)

![Playwright 登録フォーム。Local、npx、-y @playwright/mcp@latest が表示されている。保存前の画面](../../_images/app-1.1.20-20260913-mcp-config.jpg)

画像は2026年9月13日に撮影した Windows の App 1.1.20 です。アカウント情報を写さないためサイドバーを閉じています。サイドバーは左上の切り替えボタン、または `Ctrl+B` で表示します。

Customize・MCP の項目がない場合は、App のバージョン・組織ポリシー・画面の状態を記録して講師と確認してください。ここで右クリックへ移ったと断定できる根拠はありません。

## Playwright で機能を確認するよう Copilot に依頼する

Playwright MCP server を使って機能を手動テストするよう Copilot に依頼します。

1. 次のプロンプトを使い、新しい機能を検証するよう Copilot に依頼します。

   ```plaintext
   開発サーバーを起動し、Playwright MCP server で追加した機能を検証してください。Issue の詳細を使って、新しい動作が仕様に一致することを確認してください。
   ```

Copilot は Playwright MCP server を通じてブラウザーを起動し、各手順を実行して、確認結果を報告します。タスクの実行中、システム上で実際にブラウザーが開く様子を確認できます。

2. Issue の受け入れ条件と照らし合わせて概要を読みます。問題がある場合は、pull request を作成する前に追加の質問をするか、コードを修正するよう依頼します。
3. 次のレッスンでこの作業を完了するため、セッションを開いたままにします。

これで Copilot は、ユーザーと同じように機能を確認し、ブラウザーでも動作を検証しました。

<a id="cli-fallback"></a>

> **講師向け：** 緊急の作業保全が必要な場合だけ [対応手順](../material/emergency-cli.md#chapter-5) を参照してください。CLI の実装成功は、この章の App 操作の完了には数えません。

## まとめと次のステップ

GitHub Copilot app から Playwright MCP server を使い、実際のブラウザーで機能を確認しました。学習した内容は次のとおりです。

- Model Context Protocol (MCP) の概要と、アプリで MCP tools を利用する仕組みを学習した。
- アプリの設定から Playwright MCP server を追加した。
- エージェントにブラウザーを操作させ、フィルター機能を確認した。

機能の構築と検証が完了し、動作することも確認できました。次は、**Agent Merge** を使って pull request の作成とマージをエージェントに任せ、機能をリリースします。[レッスン 6「Agent Merge によるマージ」][next-lesson]に進んでください。

## リソース

- [MCP とは何か、なぜ注目されているのか][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [GitHub Copilot app での MCP server の構成][customize-app]

[next-lesson]: 6-agent-merge.md
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp
[customize-app]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
