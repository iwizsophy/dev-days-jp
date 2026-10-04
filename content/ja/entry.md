# Copilot Appで開発の流れを体験する

Dev Days · 非公式の日本語教材セット

ゲームを紹介するクラウドファンディングサイト「Tailspin Toys」を題材に、星評価、フィルター、タイトル検索を追加します。カスタム指示、自動テスト、コードレビューを使い、Appの演習1〜9を一つのストーリーに沿って進めます。

[演習1：事前準備から始める](app/0-prerequisites.md) · [全体の目次と到達目標を見る](app/README.md)

この研修で学ぶのは、エージェントに作業を依頼し、その結果を判断する開発の進め方です。仕様の曖昧さをどこで解消するか、どの情報を共有すると意図が伝わるか、どんな証拠がそろえばマージできるかを、各章の具体例で考えます。元の機能を維持しながら変更を重ねるため、前章の結果を次章でも確かめます。

## 今回の流れ

準備・接続 → 星評価の実装 → カスタム指示の適用 → フィルターの計画と実装 → MCPによるブラウザー検証 → Agent Merge → 共有Canvasと検索実装 → Automationと振り返り

最初は小さな変更を自分でレビューしてマージし、確認すべきことを理解したうえで自動化の範囲を広げます。GitHub公式が示す「変更をレビューし、フィードバックを返して改善する」開発フローを、Tailspin Toysで具体的に経験します。出典：[GitHub Copilot Appの開発フロー](https://docs.github.com/en/copilot/concepts/agents/github-copilot-app#github-copilot-app-workflow)。

## 参加前の準備

Git、Node.js 24.19.0または `>=24.19.0 <25`、最新版のGitHub Copilot Appを用意します。教材用テンプレートから自分のTailspin Toysのコピーを作り、Appへ接続して応答を確認してください。

[受講準備と利用条件の確認](preparation.md#prepare)

## 途中でつまずいたら

本文の操作対象と項目名を確認し、見つからない場合は講師に相談してください。期待した動作と実際の結果を言葉にしてから、追加の指示や確認方法を考えます。

## Appの機能と成果の確認

Agent Merge、Canvas、Automationを実際に使い、操作前後の変化を確かめます。振り返りでは、何を任せ、どの結果を根拠に判断したかを説明してください。

## 参考資料・補足コース

[独立したCLIコースとMona Mayhem](../../website/ja/workshops/references.html)は補講用の発展コンテンツです。本編の受講に必須ではありません。

[Appセッション公式英語スライド](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-english.pptx)

参照元は[github/dev-days](https://github.com/github/dev-days)のイベント開催資料と、[github-samples/copilot-workshops](https://github.com/github-samples/copilot-workshops)の演習本文です。原本のライセンスと著作権表示を保持しています。参照元リポジトリへ変更を送信しません。
