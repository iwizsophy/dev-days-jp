---
title: "第1章 - 前提条件"
description: "GitHub Copilot appの演習に向けてNode.jsを準備し、Tailspin Toysのテンプレートから自分用のリポジトリを作成します。"
authors:
  - geektrainer
lastUpdated: 2026-10-04
---

## 1.1 章の概要

この教材では、ゲームを紹介するクラウドファンディングサイト「Tailspin Toys」を題材に、GitHub Copilot appのエージェントと開発を進めます。体験するのは、変更の目的を伝え、生成されたコードとテストを確認し、レビューした変更を自分のリポジトリへ取り込む流れです。

最初に、Tailspin Toysのビルドとテストを動かすNode.jsと、自分で変更できる演習用リポジトリを準備します。環境の準備ができていれば、後の章でエラーが起きたときも、環境と実装を分けて調べやすくなります。

## 1.2 この章で学ぶこと

| 到達した状態 | 後の演習でできること |
| :--- | :--- |
| 実行されるNode.jsのバージョンを確認できる | Tailspin Toysのビルドやテストに必要な環境がそろっているか判断する |
| Tailspin Toysのテンプレートから自分用のリポジトリを作成できる | Issue、ブランチ、Pull Requestを使って変更を管理する |
| 演習用Issueが用意されたことを確認できる | 課題の背景と受け入れ条件を読んで実装を依頼する |

## 1.3 取り組む前に

ブラウザーでGitHubにサインインし、自分のアカウントでリポジトリを作成できる状態にしてください。ローカルPCでは、普段使っているターミナルを開けることを確認します。

本教材ではNode.js 24系のLTS版、24.19.0以降を使用します。すでにこの条件を満たしていれば、再インストールは不要です。nvmなどでバージョンを管理している場合は、その管理方法に合わせて切り替えます。

演習に使うのは、[教材用のTailspin Toysテンプレート](https://github.com/iwizsophy/dev-days-tailspin-template)です。使用する教材のバージョンは[v2026.10.03](https://github.com/iwizsophy/dev-days-tailspin-template/releases/tag/v2026.10.03)で、星評価やフィルター機能の解答コードは含まれていません。教材リポジトリの`dev-days-jp`と、これからコードを変更するTailspin Toysのコピーを区別して進めます。

## 1.4 体験すること

<a id="nodejs-のインストールとバージョン確認"></a>
<a id="確認とインストール手順"></a>

### 1.4.1 Node.jsのバージョンを確認する

PCにインストールしたNode.jsのバージョンと、今のターミナルが実行するNode.jsのバージョンは一致するでしょうか。まずバージョンを確認するコマンドの出力を調べます。

1. Windows Terminal、macOS Terminalなど、普段使うターミナルを開きます。
2. 次のコマンドを実行します。

   ```shell
   node --version
   ```

3. Node.js 24系の24.19.0以降が表示されたら、[演習用リポジトリの作成](#演習用リポジトリの作成)へ進みます。コマンドが見つからない場合や、条件を満たさない場合は、次の手順で準備します。

<a id="インストールが必要な場合"></a>

#### 1.4.1.1 インストールが必要な場合

1. [Node.jsのダウンロードページ][node-download]を開きます。
2. 使用するOSに合わせて、Node.js 24系のLTS版、24.19.0以降をダウンロードします。
3. インストーラーを起動し、既定の設定で進めます。Windowsでは、**Add to PATH**が有効であることを確認してください。
4. インストール後、新しいターミナルを開き直します。
5. もう一度`node --version`を実行し、条件を満たすバージョンが表示されることを確認します。

Node.jsのインストール後、すでにGitHub Copilot appを起動している場合は、完全に終了して再起動します。新しい環境変数をAppに反映したうえで、エージェントに実装を依頼するセッションでもNode.jsのバージョンを確認してください。確認方法は、[第3章の実装前の環境確認](3-add-star-rating.md#実装前の環境確認)で扱います。

<a id="演習用リポジトリの作成"></a>
<a id="使用するテンプレート"></a>
<a id="github-web-での作成手順"></a>

### 1.4.2 テンプレートから演習用リポジトリを作る

後の章では、各自が作成したTailspin Toysの演習用リポジトリでIssueやPull Requestを扱います。作成前に、コピー元のテンプレートと作成先の所有者を確認しましょう。操作の詳細は[GitHub公式のテンプレートからの作成手順][template-repository]も参照できます。

1. ブラウザーで`https://github.com/iwizsophy/dev-days-tailspin-template`を開きます。
2. **Use this template → Create a new repository**を選択します。

   ![Tailspin ToysテンプレートのUse this templateメニュー](../../_images/app-20261004-public/app-20261004-00-template-menu.jpg)

3. 作成フォームで次の項目を設定します。

   | 項目 | 設定する内容 |
   | :--- | :--- |
   | Start with a template | `iwizsophy/dev-days-tailspin-template`であることを確認する |
   | Include all branches | 既定のOff、チェックなしのままにする |
   | Owner | 自分のアカウントまたは演習用Organizationを選ぶ |
   | Repository name | 自分の演習用の名前を入力する。例は`dev-days-tailspin-toys` |
   | Choose visibility | 演習用リポジトリの公開範囲を選ぶ |

   ![テンプレートとコピー先のOwner、Repository nameを指定するフォーム](../../_images/app-20261004-public/app-20261004-00-template-form-top.jpg)

4. フォーム下部の任意項目**Jumpstart your project with Copilot**では、Prompt欄を空欄のままにします。
5. 入力内容を確認し、**Create repository**を選択します。
6. 作成したリポジトリの`owner/repo`を控えます。次章では、作成した演習用リポジトリをAppに接続します。

<a id="演習用issueの準備を確認する"></a>

### 1.4.3 演習用Issueを確認する

Tailspin Toysの演習用リポジトリの作成後に、GitHub Actionsで自動実行されるのが**Bootstrap template issues**ワークフローです。実行が終わると、そのリポジトリに演習で使う8件のIssueが作成されます。

1. 作成した演習用リポジトリの**Issues**タブを開き、8件の課題が表示されることを確認します。
2. 課題が表示されない場合は、同じ演習用リポジトリの**Actions**タブでワークフローの実行状況を確認します。
3. 必要に応じて**Bootstrap template issues → Run workflow**を実行し、終了後にIssuesを開き直します。

作成された演習用Issueのタイトルには、フィルター機能やコーディング規約など、これから取り組む変更が表れています。演習用リポジトリのコードとIssueがそろったことを確認して、次へ進んでください。

<a id="完了の確認"></a>
<a id="振り返り"></a>

## 1.5 結果の整理と振り返り

Tailspin Toysを実行するNode.jsと、自分で変更できる演習用リポジトリを用意しました。次の項目を確認してください。

- `node --version`で、Node.js 24系の24.19.0以降を確認できた。
- テンプレートから自分のコピーを作成し、`owner/repo`を控えた。
- コピーのIssuesに、演習用の8件の課題が表示された。

「各自のコピーが必要な理由」と「インストール後にバージョンを確認する理由」を、自分の言葉で説明してみましょう。予想したバージョンと実際の出力が違った場合は、何を切り替えて解決したかも振り返ります。

<a id="次のステップ"></a>

次章ではGitHub Copilot appをインストールし、今回作成した演習用リポジトリを接続します。[第2章「GitHub Copilot appのインストール」][next-lesson]へ進んでください。

<a id="補足"></a>

## 1.6 補足

<a id="この教材で体験する開発の流れ"></a>

### 1.6.1 この教材で体験する開発の流れ

GitHub Copilot appは、エージェントの作業とGitHubのリポジトリ管理をまとめて扱うデスクトップアプリケーションです。Issueから実装を始め、差分やテスト結果を読み、Pull Requestを通じて変更を取り込めます。機能の全体像は[GitHub公式の説明][about-copilot-app]で確認できます。

この教材で変更の目的と確認条件を伝えるのは受講者です。エージェントの完了報告を受けた後も、実際のコードや画面を確認し、必要なら修正を依頼します。環境を準備する段階から、説明と実際の結果を照合する習慣をつけましょう。

<a id="nodejsと実行環境"></a>

### 1.6.2 Node.jsと実行環境

演習用サイトTailspin ToysはAstroで構築されています。ローカルPCの[Node.js][nodejs]でTailspin Toysをビルドし、Vitestの単体テストとPlaywrightのE2Eテストを実行します。

ターミナルで確認できるのは、そのターミナルが使うNode.jsです。GitHub Copilot appの実装セッションで使うNode.jsのバージョンも確認すると、演習の要件との違いを見つけられます。バージョン管理ツールを使っている場合も、コマンドの出力を確かめてください。インストールの完了と、実行されるバージョンの確認は別の作業です。

Tailspin Toysの教材用テンプレートには[dev container][dev-containers]の設定もあります。[Docker Desktop][docker]などで別の環境を使う場合は、講師の案内に従ってください。

<a id="各自の演習用コピーを使う理由"></a>

### 1.6.3 各自の演習用コピーを使う理由

演習用Issueを起点に実装し、レビューした変更を自分の演習用リポジトリのmainへ取り込むため、各自のTailspin Toysのコピーを作ります。他の受講者の作業と分けて進められ、試した変更の履歴も自分で確認できます。

テンプレートからの作成は、用意されたファイルを基に新しいプロジェクトを始める操作です。詳細は[GitHub公式のテンプレート説明][template-repository]を参照してください。

<a id="リソース"></a>

### 1.6.4 参考資料

- [Node.jsのダウンロード][node-download]
- [テンプレートからのリポジトリの作成][template-repository]
- [GitHub Copilot appについて][about-copilot-app]

[next-lesson]: 2-install-copilot-app.md
[nodejs]: https://nodejs.org/
[node-download]: https://nodejs.org/en/download
[docker]: https://www.docker.com/products/docker-desktop/
[dev-containers]: https://code.visualstudio.com/docs/devcontainers/containers
[template-repository]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
[about-copilot-app]: https://docs.github.com/en/copilot/concepts/agents/github-copilot-app
