---
title: "演習 0: 前提条件"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

Copilot CLI の演習を始める前に、開発環境の準備を整えます。Tailspin Toys リポジトリの個人用コピーを作成し、[Codespaces][codespaces] 環境を起動します。後続の演習では、その統合ターミナルを使って Copilot CLI のインストールやコマンド実行を行います。

## ラボ用リポジトリを準備する

本演習でコードを変更するためのリポジトリとして、[テンプレートリポジトリ][template-repository]から新しいリポジトリを作成します。このテンプレートにはハンズオンに必要なすべてのソースコードが含まれており、以降の演習はこのリポジトリ上で進めます。

1. Web ブラウザーで、本ラボのテンプレートリポジトリ `https://github.com/github-samples/tailspin-toys` にアクセスします。
2. 画面右上にある **Use this template** ボタンをクリックし、**Create a new repository** を選択して自分用リポジトリの作成画面を開きます。

    ![「Use this template」ボタン](../../_images/ex0-use-template.png)

3. GitHub または Microsoft 主催のハンズオンイベントとして参加している場合は、講師の案内に従って作成先（Owner）を指定してください。個人で受講している場合は、GitHub Copilot の利用権限を持つ自身のアカウントまたは Organization を選択して作成します。

    ![リポジトリ テンプレートの設定を入力する画面](../../_images/ex0-repository-settings.png)

4. 後続の演習で参照するため、作成したリポジトリのパス（**organization-or-user-name/repository-name**）を記録しておきます。

> [!NOTE]
> **バックログ（Issue）は自動で準備されます**  
> テンプレートからリポジトリを生成すると、ワークフローによって演習用の GitHub Issue 群が自動的に起票されます。ワークショップ全体を通じてこれらの既存 Issue を使って開発を進めるため、自分で手動起票する必要はありません。

## Codespace を起動する

続いて、演習の実行基盤となるクラウド開発環境（Codespace）を立ち上げます。

[GitHub Codespaces][codespaces] は、ブラウザーから直接コードの編集、コマンド実行、デバッグを行えるクラウド開発環境です。Node.js、拡張機能、CLI ツールなど、本演習に必要なすべての依存関係があらかじめプリインストールされた統合開発環境（IDE）が提供されます。

1. 新しく作成した自分用のリポジトリページを開きます。
2. 緑色の **Code** ボタンをクリックします。

    ![「Code」ボタンを選択する](../../_images/ex0-code-button.png)

3. **Codespaces** タブを選択し、**Create codespace on main**（または **+** アイコン）をクリックして新しい Codespace を作成します（すでに稼働中の Codespace が存在する場合は、その一覧から選択して再接続することも可能です）。

    ![新しい codespace を作成する](../../_images/ex0-create-codespace.png)

Codespace のコンテナ構築には数分かかりますが、手元のマシンに個別に依存ツールを手動セットアップするよりも確実かつ高速に環境が整います。

> [!CAUTION]
> 後続の演習ではこの Codespace の画面に戻って作業を行います。ブラウザーのタブを閉じずに開いたままにしておいてください。

> [!NOTE]
> 本ワークショップは、Codespace またはローカル端末の [Dev Containers][dev-containers] 上で実行することを前提に設計されています。どちらの方式でも、共通のコンテナ定義によって必要なツール群が完全にセットアップされた同一環境が再現されます。ローカル端末で進めたい場合は、リポジトリをローカルにクローンして VS Code で開き、プロンプトが表示されたら **Reopen in Container** を選択してください。Codespace と全く同じ Dev Container 環境がローカル上に構築されます。

[codespaces]: https://github.com/features/codespaces
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers

## まとめと次のステップ

自分用の演習リポジトリを作成し、Copilot CLI を実行するためのクラウド開発環境（Codespace）の起動を開始しました。

次は、立ち上がった環境のターミナルで Copilot CLI をインストールし、GitHub アカウントで認証を行います。[演習 1 - GitHub Copilot CLI のインストール][next-lesson] へ進んでください。

## リソース

- [GitHub Codespaces の概要][codespaces]
- [テンプレートからリポジトリを作成する][template-repository]
- [Codespaces クイックスタート][codespaces-quickstart]

[template-repository]: https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository
[codespaces-quickstart]: https://docs.github.com/codespaces/getting-started/quickstart
[next-lesson]: 1-install-copilot-cli.md
