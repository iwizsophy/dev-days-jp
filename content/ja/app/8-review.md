---
title: "レッスン 8 - 振り返りと次のステップ"
description: "GitHub Copilot app のハーネスを振り返り、繰り返し発生する作業を自動化して、次に学ぶ内容を確認します。"
authors:
  - geektrainer
lastUpdated: 2026-09-13
---

> **この章の確認範囲：** 2026年9月13日に Windows の App 1.1.20 実機にて、ローカル実行かつ Manual トリガーの automation を保存・実行し、37秒で正常終了（Succeeded）して要約結果が正しく得られることを確認済みです。なお、定期実行（CRON 等）やクラウド実行（Run in the cloud）については実機未検証です。詳細は [UI 確認表](../material/ui-check.md) を参照してください。

本ワークショップの全レッスンを通じて、GitHub Copilot app を活用した機能の企画立案から実装・検証・マージに至るエンドツーエンドの開発フローを実践してきました。これまで習得した主な内容は次の通りです。

- リポジトリを接続し、専用のワークスペース構造と用意されたバックログ（Issue）を把握した
- 任意の対話プロンプトおよび Issue を起点としてセッションを開始し、Plan モードと Autopilot モードによってエージェントの自律度を制御した
- リポジトリ固有のカスタム指示ファイルと再利用可能なエージェントスキルにより、コーディング品質を統制した
- Playwright MCP server を導入し、実際のブラウザーを自律操作させて動的な UI 検証を実施した
- 共有キャンバスを構築・活用し、成果物中心の視覚的な協調作業を行った
- 通常の手動マージから **Agent Merge** による完全自動マージまで、段階的にリリース工程を自動化した

最後に、定型的な反復作業を自動化する **Automations** 機能を体験し、エージェント活用のベストプラクティスと今後の学習ロードマップを確認しましょう。

## 繰り返し発生する作業を自動化する

GitHub Copilot app の **Automations** 機能を使用すると、設定したスケジュールや手動トリガーに応じてエージェントに定型タスクを自動実行させることができます。新しく起票された Issue の一次トリアージや、直近の開発アクティビティの定期レポート作成といった、反復的かつ定型化された業務の自動化に最適です。

ここでは、既存コードに影響を与えない安全な読み取り専用の automation を作成して実行してみます。

1. サイドバーで **Automations** を選択し、画面内の **New automation** をクリックします。
2. 名前欄に `Recap my recent work` などの分かりやすい名称を入力します。
3. **Trigger** のドロップダウンを開き、**Manual** を選択します（App 1.1.20 の実機では初期値が Daily となっており、選択肢として Manual、Hourly、Daily、Weekly、CRON、Issue、Pull request が表示されます。本演習では手動実行の Manual を選択し、**Run in the cloud** はオフのままで進めます）。
4. リポジトリに変更を加えないよう、次のような読み取り専用のプロンプトを入力します。

   ```plaintext
   このリポジトリで過去1週間にマージされた PR を要約し、バックログでまだ open の Issue を一覧にしてください。
   ```

5. **Select project** で自身の演習用 Tailspin Toys リポジトリを選択します（GitHub 連携とローカルフォルダーの両方が登録されている場合は、対象を取り違えないよう `owner/repository` 表記を必ず確認してください）。
6. **Create** ボタン横のメニューを展開し、**Create and run** を選択して保存と同時に即時実行します（保存のみを行う場合は Create を選択し、後から一覧の Run ボタンで実行することも可能です）。
7. **Recent runs** に表示された実行結果を開き、ステータスが **Succeeded** になり要約レポートが正しく出力されていることを確認します。

### 実機検証における確認記録と注意点

2026年9月13日の実走検証では、Local 環境かつ手動実行（Manual）により、**37秒で処理が正常終了（Succeeded）**しました。出力されたレポートを GitHub の Web 画面と照合したところ、「マージ済み PR 6件」「Open な Issue 6件」という集計結果が完全に一致していることを確認しています。  
なお、設定は Manual のまま保存しており、定期スケジュール実行やクラウド環境での無人実行については実機未検証です。

> [!TIP]
> Automations はローカル端末だけでなく、クラウド環境（Cloud sandboxes）上でも実行可能です。スケジュールに従って完全無人でバックグラウンド実行させたい場合は、**Run in the cloud** を有効化し、タスクの実行に必要な **Tools**（MCP やリポジトリ操作権限）を選択します。出力の正確性や安全性が十分に検証できるまでは、スケジュール実行する automation の権限を読み取り専用に限定し、破壊的な変更を伴わないタスクから運用を開始することを推奨します。

## ベストプラクティス

AI コーディングツールを活用する際、生成されるコードの品質を左右するのは、モデル自体の性能だけでなく**ツールの周囲に整備されたコンテキスト基盤**です。本ワークショップで体験した通り、指示ファイル（Instructions）、スキル（Skills）、キャンバス（Canvases）がそれぞれ重要な役割を果たしました。これらのアセットを整備し、セッション間で再利用可能な形でリポジトリへ蓄積していくことが成功の鍵となります。

- **モードとモデルの適切な使い分け**：  
  実装に着手する前のアーキテクチャ検討には **Plan** モード、人間の監督下で細かく対話しながら進めるには **Interactive** モード、明確に仕様とテストが分離された定型タスクには **Autopilot** モードを選択します。また、定型的な編集には応答速度の速いモデル、複雑な設計判断には推論能力に優れたモデルを選択するなど、タスクの難易度に応じたモデル選定が効果的です。
- **明確なコンテキストの提供**：  
  何を、なぜ、どのような制約条件で構築するのかを明確に提示することで、エージェントの出力精度は劇的に向上します。本格的な実装セッションを立ち上げる前の思考整理や前提の確認には、軽量な **Quick chats** が役立ちます。

## さらに確認する価値のある機能

本教材で扱った中核的なワークフローのほかにも、GitHub Copilot app には強力な機能が多数用意されています。

- **Quick chats**：本格的なセッションを立ち上げるまでもない、単発の疑問解消や構文確認に使える軽量チャット
- **Rubber duck**：コードを書く前に設計課題を対話形式ですり合わせ、思考の壁打ちを行う機能
- [**Custom agents**][custom-agents]：特定の専門役割、専用ツール、個別指示をパッケージ化し、繰り返し呼び出せるカスタムエージェント
- [`/chronicle`][chronicle]：セッション内で行われた作業経緯や意思決定のログを要約・記録するコマンド
- [**Bring your own key (BYOK)**][byok]：Ollama、Foundry Local、LM Studio などを通じて、独自のローカルモデルや外部プロバイダーのモデルを接続する機能
- [**Cloud sandboxes**][sandboxes]：ローカルマシンを消費せず、GitHub がホストする分離された安全なコンテナ環境でセッションを実行する機能
- [**Deep links**][deep-links]：特定のリポジトリ、セッション、初期プロンプトを指定した URL リンクからアプリを直接起動する機能

## 次のステップ

AI エージェントを自在に使いこなす最良の道は、日々の開発業務や個人プロジェクトで継続的に使い続けることです。プロダクションコードの保守、趣味のプログラミング、あるいは温めていた新しいアイデアのプロトタイプ構築にぜひ活用してください。学んだ知見をチームへ還元し、チーム固有の指示ファイルやスキルを育てていきましょう。

GitHub Copilot エコシステムの全容をさらに深く学ぶには、以下の関連教材も合わせて参照してください。

- [VS Code ハーネス](https://github-samples.github.io/copilot-workshops/vscode/)
- [Copilot CLI ハーネス](../cli/README.md)（本教材の参考コース）
- [Cloud agent ハーネス](https://github-samples.github.io/copilot-workshops/cloud/)

<a id="cli-fallback"></a>

> **講師向け：** 参加者の環境でトラブルが生じ、緊急に作業を保全する必要がある場合のみ [対応手順](../material/emergency-cli.md#chapter-8) を参照してください。なお、CLI 側で実装が完了しても、本章における App 操作の完了とは見なしません。

## リソース

- [GitHub Copilot app について][about-copilot-app]
- [GitHub Copilot app の概要][getting-started]
- [GitHub Copilot app のカスタマイズ][customize]
- [Automations の使用][using-automations]
- [Canvas extensions の操作][canvas-docs]
- [クラウドサンドボックスとローカルサンドボックスについて][sandboxes]

[about-copilot-app]: https://docs.github.com/copilot/concepts/agents/github-copilot-app
[getting-started]: https://docs.github.com/copilot/how-tos/github-copilot-app/getting-started
[customize]: https://docs.github.com/copilot/how-tos/github-copilot-app/customize-github-copilot-app
[using-automations]: https://docs.github.com/copilot/how-tos/github-copilot-app/using-automations
[canvas-docs]: https://docs.github.com/copilot/how-tos/github-copilot-app/working-with-canvas-extensions
[sandboxes]: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[byok]: https://docs.github.com/copilot/how-tos/github-copilot-app/use-byok-models
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links
