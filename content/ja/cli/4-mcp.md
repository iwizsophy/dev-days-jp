---
title: "演習 4 - Playwright MCP サーバーで機能をテストする"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Copilot CLI を使ってフィルター機能を実装しました。pull request を起票する前に、実際のブラウザー上で期待通りに動作するかを検証する必要があります。人間が手動で画面操作を行う代わりに、**Playwright MCP server** を Copilot CLI に接続し、エージェント自身にブラウザーを操作させて機能を検証させましょう。

この演習では、次の内容を学習します。

- Model Context Protocol (MCP) の概要と、MCP サーバーが Copilot CLI を拡張する仕組みを理解する
- `/mcp add` コマンドを用いて Playwright MCP server を Copilot CLI に登録する
- エージェントにブラウザーを自律操作させ、フィルター機能の動的検証を実施する

## Model Context Protocol (MCP) とは

[Model Context Protocol (MCP)](https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/) は、AI エージェントが外部のツールやサービスと安全に双方向通信するための標準プロトコルです。MCP を導入することで、AI エージェントはリアルタイムに外部システムへアクセスし、**リソース（resources）**を通じて最新情報を取得したり、**ツール（tools）**を通じてユーザーに代わる操作を実行したりできるようになります。

エージェントは、対象ツールとの通信を仲介する **MCP server** を経由してこれらの機能を利用します。MCP server はローカルプロセス（CLI や NPM パッケージ）やリモート API とエージェント間の接続を管理し、それぞれ固有のツールセットとリソース群を提供します。

広く利用されている MCP server の例は次の通りです。

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)**：GitHub リポジトリの管理 API を提供します。リポジトリの作成・更新、Issue や pull request の管理などをエージェントが実行できます。
- **[Playwright MCP Server](https://github.com/microsoft/playwright-mcp)**：Playwright によるブラウザー自動化機能を提供します。ページ遷移、フォーム入力、ボタンのクリック、DOM 操作などをエージェントが実行できます。

GitHub は、エコシステムの発展を促進するため [MCP registry](https://github.com/mcp) を公開しており、多種多様なサーバーが登録されています。

> [!CAUTION]
> セキュリティの観点から、MCP server はプロジェクトに導入する外部ライブラリと同様に慎重に取り扱ってください。利用前にソースコードや発行元を検証し、セキュリティ上の影響を検討してください。信頼できる MCP server のみを利用し、機密性の高いリソースや特権的な操作へのアクセス権限を安易に付与しないよう注意してください。

> [!NOTE]
> [GitHub MCP server][github-mcp-server] は Copilot CLI に**あらかじめ組み込まれています**。そのため追加設定なしで利用可能であり、これまでの演習でエージェントが Issue を読み書きできていたのはこの組み込みサーバーの働きによるものです。本演習では、エージェントにブラウザー操作能力を与えるため、2つ目のサーバーとして Playwright MCP server を追加します。

## Playwright MCP server を追加する

サーバーを追加する最も容易な方法は、対話式コマンド `/mcp add` を使用することです。エージェントがブラウザーを制御できるように [Playwright MCP server][playwright-mcp-server] を登録します。

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

1. Copilot CLI セッションで次のコマンドを入力します。

   ```text
   /mcp add
   ```

2. ターミナルに対話式の設定フォームが表示されます。<kbd>Tab</kbd> キーで各入力フィールド間を移動し、次のように設定します。

   - **Server Name**: `playwright`
   - **Server Type**: **Local**（または **STDIO**）を選択
   - **Command**: `npx @playwright/mcp@latest --headless`
   - **Tools**: すべてのツールを許可するため `*` のままにする

3. キーボードで <kbd>Ctrl</kbd>+<kbd>S</kbd> を押して設定を保存します。サーバーが登録され、CLI プロセスを再起動することなく即座に利用可能になります。

`--headless` フラグを指定することで、Playwright は GUI ウィンドウを表示せずにバックグラウンドでブラウザーを起動します（デスクトップ画面を持たない Codespace 環境ではこの設定が必須です）。内部的には、設定内容が `~/.copilot/mcp-config.json` に書き込まれます。

```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"],
      "tools": ["*"]
    }
  }
}
```

4. 登録されている MCP サーバーの一覧を表示し、正常にアクティブ化されていることを確認します。

   ```text
   /mcp show
   ```

5. 組み込みの `github` サーバーと並んで `playwright` が表示されていれば登録完了です。

> [!NOTE]
> **E2E テスト用ブラウザーと MCP 用ブラウザーの違いについて**  
> Tailspin Toys の E2E テスト用 Chromium が導入済みであっても、MCP が既定で使用する Chrome バイナリがインストールされていない場合があります。実機検証時、`Chromium distribution 'chrome' is not found` というエラーが発生した事例がありました。このエラーが発生した場合は、Codespace のシェルで `npx playwright install chrome` を実行してから MCP の操作を再試行してください（`npx playwright install chromium` を再実行しても Chrome 不足は解消しません）。

## Web サイトを起動する

> [!NOTE]
> **Codespace 環境で Chrome の sandbox / namespace エラーが発生する場合の対処**  
> 分離された演習用 Codespace 内でローカルサイトのみを検証する場合、Playwright の起動コマンドを `npx @playwright/mcp@latest --headless --no-sandbox --isolated` に変更して Copilot CLI を再起動することで復旧できる場合があります（2026年9月8日の実機検証において、この設定で MCP 接続が安定することを確認済みです）。  
> なお、`--no-sandbox` はブラウザーのセキュリティサンドボックスを無効化するため、日常的に使用する開発 PC や外部サイトを閲覧する環境の既定設定としては決して使用しないでください。

Playwright MCP server がブラウザー検証を行うには、対象となる Web アプリケーションが起動している必要があります。Copilot CLI を起動したまま並行して稼働させるため、**別のターミナルタブ**で開発サーバーを立ち上げます。

1. Codespace のターミナルパネル右上にある **+**（新しいターミナル）をクリックします（<kbd>Ctrl</kbd>+<kbd>\`</kbd> はパネルの表示／非表示切り替えですので、必ず **+** で新規ターミナルを作成してください。Copilot CLI を実行中のターミナルはそのまま保持します）。
2. Web サイトの開発サーバーを起動します。

   ```bash
   npm run dev
   ```

3. ターミナル上に `Astro server: http://localhost:4321` と表示されたら、サーバーの準備は完了です。このターミナルは閉じずに起動したままにしておきます。

## フィルタリング機能をテストする

Copilot CLI を実行しているターミナルタブに戻り、エージェントにブラウザー経由での機能テストを指示します。

[Playwright MCP server][playwright-mcp-server] を利用することで、エージェントは自律的にブラウザーを操作できます。人間がいちいちブラウザーを開いて手作業で確認することなく、エージェント自身がページにアクセスし、画面内を遷移し、フィルターを操作して、その結果を要約レポートとして出力してくれます。

Playwright MCP server は、画面のスクリーンショット画像ではなく、ページの[アクセシビリティツリー（accessibility tree）][playwright-mcp-server]を解析して動作します。エージェントは支援技術（スクリーンリーダー等）と同様に、構造化され適切にラベル付けされたボタンやリスト要素を認識して操作します。そのため、この検証プロセスは機能テストであると同時に、基本的なアクセシビリティ適合性の確認も兼ねています。

プロンプト入力欄に次の指示を入力し、実装したフィルター機能の検証を依頼します。

```text
Playwright MCP server を使い、http://localhost:4321 で動作中のアプリをブラウザーで開いて、新しいゲームのフィルタリングを検証してください。

1. ゲームページを開き、表示件数を記録する。
2. カテゴリで絞り込み、そのカテゴリのゲームだけに一覧が更新されることを確認する。
3. 条件を解除して publisher で絞り込み、その publisher の一覧に更新されることを確認する。
4. カテゴリと publisher を組み合わせ、両方の条件に合う結果になることを確認する。

各手順で観察した結果と、期待どおりに動かなかった点を報告してください。
```

Copilot は Playwright MCP server 経由でブラウザーを自律起動し、各手順を順次実行して検証結果を報告します。報告された要約を Issue の受け入れ条件と照合し、挙動に違和感があれば追加の指示を出してコードを修正させてください。

> [!NOTE]
> この検証を行うには、アプリが `http://localhost:4321` で稼働している必要があります。もし開発サーバーが停止していた場合は、プロンプトを送信する前に再起動してください。また、初回実行時にブラウザーバイナリのダウンロードが必要になる場合があります。ブラウザーが見つからない旨のエラーが返された場合は、`npx playwright install chromium` を実行して再試行してください。

[playwright-mcp-server]: https://github.com/microsoft/playwright-mcp

## まとめと次のステップ

Playwright MCP server を活用し、Copilot CLI から実際のブラウザーを自律操作させて機能テストを実施しました。本演習で実施した主な内容は次の通りです。

- Model Context Protocol (MCP) の基本構造と、エージェントが外部ツールを利用する仕組みを理解した
- `/mcp add` コマンドを用いて Playwright MCP server を登録した
- エージェントにブラウザー操作を委譲し、リリース前にフィルター機能の挙動を動的に検証した

機能が正常に動作することを確認できました。次は、再利用可能なエージェントスキル（Agent Skills）を活用して pull request を作成・管理します。[演習 5 - エージェントスキル][next-lesson] へ進んでください。

## リソース

- [MCP とは何か、なぜいま注目されているのか][mcp-blog-post]
- [Microsoft Playwright MCP Server][playwright-mcp-server]
- [Copilot CLI に MCP server を追加する][cli-add-mcp]
- [GitHub MCP Server][github-mcp-server]

[previous-lesson]: 3-generating-code.md
[next-lesson]: 5-agent-skills.md
[mcp-blog-post]: https://github.blog/ai-and-ml/llms/what-the-heck-is-mcp-and-why-is-everyone-talking-about-it/
[github-mcp-server]: https://github.com/github/github-mcp-server
[cli-add-mcp]: https://docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers
