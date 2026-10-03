---
title: "レッスン 0 - 前提条件"
description: "GitHub Copilot app のレッスンに向けて、Tailspin Toys プロジェクト用の Node.js をインストールし、テンプレートからリポジトリの自分用コピーを作成します。"
authors:
  - geektrainer
lastUpdated: 2026-10-04
---

> **この章の進め方**
> Node.jsと各自の演習用リポジトリを準備します。GitHub Webでテンプレートからコピーを作り、次章でCopilot Appに接続します。

GitHub Copilot appは、Copilotのエージェント機能とGitHubのリポジトリ管理を一元的に扱うデスクトップアプリケーションです。IssueやPull Requestに素早くアクセスでき、自律的なエージェントを活用した開発が可能です。
機能の全体像は[GitHub公式のCopilot appの説明][about-copilot-app]で確認できます。この教材では、受講者が変更の目的を伝え、エージェントの調査・実装・テストを確認し、レビューして取り込む流れを学びます。
本ワークショップでは、Astro で構築された EC アプリ「Tailspin Toys」と GitHub Copilot app を組み合わせ、ローカル環境で開発を進めます。アプリをインストールする前に、前提環境として必要な Node.js をローカルに導入し、演習用リポジトリを用意します。

本レッスンでの到達目標は次の 2 点です。

- **Node.js の導入**：ローカル環境でプロジェクトのビルドとテストを実行できる適切なバージョンを用意する
- **演習用コピーの作成**：修正済みテンプレートから Tailspin Toys リポジトリを作成し、初期バックログを準備する

## 1. Node.js のインストールとバージョン確認

本ワークショップでは、エージェントが実装した機能を検証するために、ローカル環境でTailspin Toysのテストスイートを実行します。Vitestによる単体テストとPlaywrightによるE2Eテストを動かすため、ローカルPCに[Node.js][nodejs]が必要です。

### 必要なバージョン

本教材では、**Node.js 24系のLTS版（24.19.0以降）**を使用します。すでにこの条件を満たしていれば、再インストールは不要です。

### 確認とインストール手順
Node.jsを新しく導入する場合は、公式サイトのインストーラーを利用できます。すでにnvmなどでバージョンを管理している場合は、その管理方法に合わせて切り替えてください。

1. ターミナル（Windows Terminal、macOS Terminal、または普段利用しているシェル）を開きます。
2. 次のコマンドを実行し、このターミナルで実行されるNode.jsのバージョンを確認します。

    ```shell
    node --version
    ```

3. 出力されたバージョンがNode.js 24系の24.19.0以降であれば、セクション2へ進みます。

> [!TIP]
> Node.js が未導入、またはバージョンが適合しない場合のみ、以下のステップ 4〜9 を実行してください。

4. [Node.js のダウンロードページ][node-download] を開きます。
5. 使用しているOSに合わせて、**Node.js 24系のLTS版（24.19.0以降）**をダウンロードします。
6. インストーラーを起動し、既定の設定でインストールを進めます（Windows の場合は **Add to PATH** が有効になっていることを確認してください）。
7. インストール完了後、新しいターミナルウィンドウを開き直します。
8. 再度バージョンを確認します。

    ```bash
    node --version
    ```

9. 要求バージョンが正しく表示されることを確認します（※すでに Copilot App を起動していた場合は一度完全に終了して再起動し、新しい環境変数が確実に反映されるようにしてください）。

このコマンドで確認できるのは、現在開いているターミナルで動作するNode.jsのバージョンです。Appの実装セッションでも、エージェントが使うNode.jsが要件を満たすか確認します。確認方法は、[レッスン2の実装前の環境確認](2-add-star-rating.md#実装前の環境確認)で説明します。

> [!TIP]
> 本章ではローカルに導入したNode.jsを使います。テンプレートには[dev container][dev-containers]の設定も含まれていますが、[Docker Desktop][docker]などで別の環境を使う場合は、講師の案内に従ってください。

## 2. 演習用リポジトリの作成

Tailspin Toys プロジェクトの演習用コピーを、受講者各自の GitHub アカウント上に作成します。[教材用の修正済み Tailspin Toys テンプレート](https://github.com/iwizsophy/dev-days-tailspin-template) を開き、[テンプレートからのコピー作成手順][template-repository] に沿って進めます。

後の演習でIssueの作成やコードの変更、マージを自分で行えるように、テンプレートから各自の演習用リポジトリを作成します。

### 使用するテンプレート

- **取得先リポジトリ**：`iwizsophy/dev-days-tailspin-template`
- **使用するバージョン**：[v2026.10.03](https://github.com/iwizsophy/dev-days-tailspin-template/releases/tag/v2026.10.03)
- **初期状態**：星評価やフィルター機能などの演習解答コードは含まれていません。
- **リポジトリの区別**：教材自体のリポジトリ（`dev-days-jp`）と、コードを変更する演習用コピー（Tailspin Toys）を混同しないようご注意ください。

### GitHub Web での作成手順

> [!NOTE]
> 以下の画像2点は、テンプレート取得先の変更前の操作例です。画像内のリポジトリ名ではなく、本文に記載された **`iwizsophy/dev-days-tailspin-template`** を選択してください。

1. ブラウザーで、教材用テンプレートリポジトリ `https://github.com/iwizsophy/dev-days-tailspin-template` を開きます。
2. ページ右上の **Use this template** ボタンを押し、ドロップダウンから **Create a new repository** を選択します。

    ![GitHub Web 全体と Use this template の Create a new repository メニュー](../../_images/app-1.1.20-20260913-template-menu.png)

3. 画面の各項目を設定します。

    - **Start with a template**：`iwizsophy/dev-days-tailspin-template` と表示されていることを確認
    - **Include all branches**：既定の **Off**（チェックなし）のまま
    - **Owner**：自身のアカウントまたは演習用 Organization を選択
    - **Repository name**：演習用のリポジトリ名（例：`dev-days-tailspin-toys` など）を入力
    - **Choose visibility**：演習用リポジトリの公開範囲を選択

    ![テンプレート作成フォーム上部。Owner、未入力の Repository name、Choose visibility](../../_images/app-1.1.20-20260913-template-form.png)

4. フォーム下部の任意項目 **Jumpstart your project with Copilot** の Prompt 欄は、本ワークショップでは**空欄のまま**にします。
5. 入力内容を確認し、**Create repository** ボタンを押します。
6. リポジトリの作成完了後、その完全なパス（`organization-or-user-name/repository-name`）を控えておきます（次章以降で使用します）。

> [!NOTE]
> コピー先リポジトリの作成後、GitHub Actions の **Bootstrap template issues** ワークフローが自動実行され、演習で使用する 8 件のバックログ Issue が作成されます。リポジトリの **Issues** タブに課題が表示されない場合は、自身のコピーの **Actions** タブで実行状況を確認し、必要に応じて **Bootstrap template issues → Run workflow** を手動実行してください。

## まとめと次のステップ

事前準備が完了しました。

- ローカル環境でプロジェクトをビルド・テストできるよう Node.js を用意した
- テンプレートから Tailspin Toys リポジトリの自分用コピーを作成した

次へ進む前に、「なぜ各自のコピーが必要か」「Node.jsのバージョンを確認する理由」を自分の言葉で説明してみましょう。コピーのURLと、確認したNode.jsのバージョンを控えておけば、後のトラブル時にも作業環境を照合できます。

次は GitHub Copilot app をインストールし、作成したリポジトリを接続してワークスペースの構造を確認します。[レッスン 1「GitHub Copilot app のインストール」][next-lesson] に進んでください。

## リソース

- [Node.js のダウンロード][node-download]
- [テンプレートからのリポジトリの作成][template-repository]
- [GitHub Copilot app について][about-copilot-app]

[next-lesson]: 1-install-copilot-app.md
[nodejs]: https://nodejs.org/
[node-download]: https://nodejs.org/en/download
[docker]: https://www.docker.com/products/docker-desktop/
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
[template-repository]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
[about-copilot-app]: https://docs.github.com/en/copilot/concepts/agents/github-copilot-app
