---
title: "演習 1 - GitHub Copilot CLI をインストールする"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

[GitHub Copilot CLI][about-copilot-cli] は、ターミナル環境で自律動作するエージェント型コーディングアシスタントです。コードベースの構造探索、コード生成、シェルコマンドの実行、外部ツール連携まで、すべてコマンドラインから指示できます。GUI エディターとターミナルを行き来することなく、ターミナル作業に集中したままエージェントへタスクを委譲できます。

本演習では、日常的に利用しているパッケージマネージャーを用いて Copilot CLI をインストールし、認証を完了させます。

この演習では、次の内容を学習します。

- npm を使用して GitHub Copilot CLI をグローバルインストールする
- GitHub アカウントで認証を行う
- 作業ディレクトリの信頼設定を行い、正常動作を確認する

## シナリオ

開発チームでは、増え続けるバックログを迅速に消化するため AI エージェントの導入を進めています。Copilot CLI は、多くのエンジニアが日々の作業拠点としているターミナル環境へ直接エージェント機能を提供します。本演習を通じてインストールと認証を済ませ、以降の演習ですぐに活用できる状態を整えます。

## Codespace でターミナルを開く

Copilot CLI をインストールするため、起動した Codespace 上で統合ターミナルを開きます。

1. 前の演習で立ち上げた Codespace のブラウザータブを表示します。
2. キーボードで <kbd>Ctrl</kbd>+<kbd>\`</kbd>（バッククォート）を押してターミナルパネルを開きます。
3. 画面下部に bash ターミナルが表示されたことを確認します。

## Copilot CLI をインストールする

Copilot CLI は [npm][install-npm]、[WinGet][install-winget]、[Homebrew][install-homebrew] など各種パッケージマネージャーから導入可能です。GitHub Codespaces には Node.js があらかじめセットアップされているため、本演習では npm を使用してインストールします。

1. ターミナルで Node.js のバージョンを確認します。

   ```bash
   node --version
   ```

   本演習で使用する Tailspin Toys は **Node.js 22.13 以上** を必須要件としています。出力が `v22.13.0` 以降であることを確認してください（テンプレートの更新等を行った場合は、リポジトリの `package.json` 内 `engines.node` の指定も合わせて確認してください）。

2. npm を使用して、Codespace 環境へ Copilot CLI をグローバルインストールします。

   ```bash
   npm install -g @github/copilot
   ```

3. インストールされたバージョンを確認し、正常に導入されたことを検証します。

   ```bash
   copilot --version
   ```

   ターミナルに `v1.0.XX` のようなバージョン番号が出力されれば成功です。

> [!TIP]
> もしパーミッションエラー（権限不足）が発生した場合は、`sudo npm install -g @github/copilot` のように管理者権限で実行してください（通常の GitHub Codespaces 環境では sudo なしでインストール可能です）。

## GitHub で認証する

> [!NOTE]
> **GitHub CLI（gh）の確認について**  
> 後続の演習で pull request を作成・管理する際に使用する `gh` コマンドは、Copilot CLI とは別の独立したツールです。ターミナルで `gh --version` を実行し、もし `command not found` となる場合は事前にインストールしてください。Debian 系の Codespace 環境であれば、`sudo apt-get update && sudo apt-get install -y gh` で導入できます（ローカル端末の場合は [GitHub CLI 公式サイト](https://cli.github.com/) の手順に従ってください）。導入後は `gh api user --jq .login` を実行し、演習用アカウントでログインされていることを確認してください。

Copilot CLI を初回起動する際、GitHub アカウントとの紐付け認証が求められます。

1. ターミナルで Copilot CLI を起動します。

   ```bash
   copilot
   ```

2. 未ログイン状態の場合、認証を促すプロンプトが表示され、8桁のワンタイムデバイスコード（device code）と認証用 URL が提示されます。
3. 画面の案内に従って認証を行います。
   - 提示された URL をブラウザーで開きます。
   - 表示されたデバイスコードを入力します。
   - GitHub 上で Copilot CLI によるアクセス許可を承認（Authorize）します。
4. 認証が完了すると、質問や指示を受け付ける Copilot CLI の対話プロンプトが表示されます。

> [!NOTE]
> Codespace のセッション情報から自動的に GitHub 認証が引き継がれ、デバイスコードの入力を求められずに直接対話プロンプトが起動する場合があります。その場合は認証がすでに完了していますので、そのまま次へ進んでください。

## ディレクトリを信頼し、動作を確認する

Copilot CLI の対話画面が開いたら、本リポジトリに対するセキュリティ上の信頼設定を行い、基本的な疎通確認を実施します。

1. ワークスペース内のファイルを信頼するかどうかの確認ダイアログが表示されたら、矢印キーで選択肢を確認します。
   - **Yes, proceed**：現在のセッションに限り信頼する
   - **Yes, and remember this folder for future sessions**：このフォルダーを恒久的に信頼する
   - **No, exit (Esc)**：アクセスを拒否して終了する
2. 今後も同じリポジトリで作業を継続するため、**Yes, and remember this folder for future sessions** を選択して <kbd>Enter</kbd> を押します。
3. プロンプトに簡単な質問を入力し、Copilot CLI がコードベースを正しく認識できるか確認します。

   ```plaintext
   このプロジェクトにはどのようなファイルがありますか？
   ```

4. エージェントがリポジトリ内のディレクトリ構造を走査し、プロジェクト概要を回答することを確認します。
5. `/help` コマンドを入力して、利用可能なスラッシュコマンドの一覧を表示させてみます。

   ```plaintext
   /help
   ```

6. 動作確認が完了したら、次のコマンドを入力して一度 Copilot CLI を終了します（後続の演習で再度起動します）。

   ```plaintext
   exit
   ```

## まとめと次のステップ

GitHub Copilot CLI のインストールと GitHub アカウントの認証が完了しました。本演習で実施した主な内容は次の通りです。

- npm を使って Copilot CLI をグローバルインストールした
- GitHub アカウントで CLI のデバイス認証を完了した
- リポジトリフォルダーを信頼済みとして登録した
- 簡単な質問とスラッシュコマンドにより CLI の正常動作を確認した

環境が整いましたので、次は Copilot にプロジェクト固有の規約や背景知識を伝達するカスタム指示を設定します。[演習 2 - カスタム指示][next-lesson] へ進んでください。

## リソース

- [GitHub Copilot CLI のインストール][install-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI を使う][using-copilot-cli]

[previous-lesson]: 0-prerequisites.md
[next-lesson]: 2-custom-instructions.md
[install-copilot-cli]: https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli
[install-npm]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-npm-all-platforms
[install-winget]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-winget-windows
[install-homebrew]: https://docs.github.com/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-homebrew-macos-and-linux
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
