# Copilot Appで開発の流れを体験する

Dev Days · 非公式の日本語教材セット

この教材では、ゲームを紹介するクラウドファンディングサイト「Tailspin Toys」に、受講者が星評価の表示、カテゴリーとパブリッシャーによる絞り込み、タイトル検索を追加します。GitHub Copilot Appのカスタム指示、自動テスト、コードレビューを使い、第1〜9章を一連の開発の流れに沿って進めます。

[演習1：事前準備から始める](app/1-prerequisites.md) · [全体の目次と到達目標を見る](app/README.md)

この研修では、GitHub Copilot AppのエージェントにTailspin Toysの機能変更を依頼し、コード差分・テスト・画面を確認して実装結果を判断する開発の進め方を学びます。受講者は、機能の仕様の曖昧さをどこで解消するか、エージェントとどの情報を共有すると意図が伝わるか、どの確認結果がそろえばPRをマージできるかを、各章の具体例で考えます。前の章までに実装した機能を維持しながら変更を重ねるため、次の章でもその機能が動くことを確かめます。

## 今回の流れ

準備・接続 → 星評価の実装 → カスタム指示の適用 → フィルターの計画と実装 → MCPによるブラウザー検証 → Agent Merge → 共有Canvasと検索実装 → Automationと振り返り

最初の星評価の追加では、受講者がエージェントの変更をレビューしてPRをマージします。差分やテスト、画面で確認すべきことを理解したうえで、後の章でマージや作業の要約を自動化します。GitHub公式が示す「変更をレビューし、フィードバックを返して改善する」開発フローを、Tailspin Toysで具体的に経験します。出典：[GitHub Copilot Appの開発フロー](https://docs.github.com/en/copilot/concepts/agents/github-copilot-app#github-copilot-app-workflow)。

## 参加前の準備

Git、Node.js 24.19.0または `>=24.19.0 <25`、最新版のGitHub Copilot Appを用意します。教材用テンプレートから自分のGitHubアカウントにTailspin Toysの演習用リポジトリを作り、GitHub Copilot Appへ接続して、Copilotが応答することを確認してください。

[受講準備と利用条件の確認](preparation.md#prepare)

## 途中でつまずいたら

操作するボタンやメニューが見つからない場合は、本文が示す画面と項目名を確認し、講師に相談してください。Tailspin ToysやCopilot Appが期待したとおりに動かない場合は、期待した動作と実際の結果を言葉にしてから、エージェントへの追加指示や確認方法を考えます。

## Appの機能と成果の確認

Agent Merge、Canvas、Automationを実際に使い、操作前後の変化を確かめます。振り返りでは、何を任せ、どの結果を根拠に判断したかを説明してください。

## 参考資料・補足コース

[独立したCLIコースとMona Mayhem](../../website/ja/workshops/references.html)は補講用の発展コンテンツです。本編の受講に必須ではありません。

[Appセッション公式英語スライド](https://github.com/github/dev-days/releases/download/2026-07-30/copilot-app-english.pptx)

参照元は[github/dev-days](https://github.com/github/dev-days)のイベント開催資料と、[github-samples/copilot-workshops](https://github.com/github-samples/copilot-workshops)の演習本文です。原本のライセンスと著作権表示を保持しています。参照元リポジトリへ変更を送信しません。
