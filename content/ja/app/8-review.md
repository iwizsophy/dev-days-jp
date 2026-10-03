---
title: "レッスン 8 - 振り返りと次のステップ"
description: "GitHub Copilot app で学んだ機能の使い分けを振り返り、同じ条件で調査を繰り返す Automation を作成・検証します。"
authors:
  - geektrainer
lastUpdated: 2026-10-03
---

> **この章の進め方** 読み取り専用のAutomationをManual・Localで実行し、実行結果をGitHubの情報と照合します。最後に、ワークショップで学んだ機能をどの場面で使うか振り返ります。

本ワークショップの全レッスンを通じて、GitHub Copilot app を活用した機能の企画立案から実装・検証・マージに至るエンドツーエンドの開発フローを実践してきました。これまで習得した主な内容は次の通りです。

- リポジトリを接続し、専用のワークスペース構造と用意されたバックログ（Issue）を把握した
- 任意の対話プロンプトおよび Issue を起点としてセッションを開始し、Plan モードと Autopilot モードによってエージェントの自律度を制御した
- リポジトリ固有のカスタム指示ファイルと再利用可能なエージェントスキルにより、コーディング品質を統制した
- Playwright MCP serverの接続とツールの実行を確認し、実際のブラウザーを自律操作させて動的なUI検証を実施した
- 共有キャンバスを構築・活用し、成果物中心の視覚的な協調作業を行った
- 通常の手動マージから **Agent Merge** による自動マージまで、品質を確認しながらmainへの統合を自動化した

最後に、定型的な反復作業を自動化する **Automations** 機能を体験し、エージェント活用のベストプラクティスと今後の学習ロードマップを確認しましょう。

## 繰り返し発生する作業を自動化する

GitHub Copilot appの **Automations** では、繰り返す作業の指示を保存し、手動または設定したトリガーで実行できます。新しいIssueの調査や、最近のPRの要約などが公式の用途例です。本演習では、過去1週間の開発状況を調べる作業を保存します。[GitHub公式のAutomationsの説明](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations#about-automations)

毎回チャットへ指示を書き直すと、ある日はマージ済みPR、別の日は作成したPRを数えるなど、調査の条件が変わりがちです。Automationに対象リポジトリ、期間、対象の状態、報告する証拠を保存すれば、同じ範囲を繰り返し調べられます。結果を比較するときにも、作業が進んだから件数が変わったのか、集計条件を変えたのかを見分けやすくなります。

ここでは読み取り専用の作業をManual・Localで実行します。まず自分が結果を読めるタイミングで動かし、GitHubの実データと照合するためです。定期実行に進む前に、1回の調査で何を読み、どのような報告が得られるかを理解しましょう。Manualは実行するタイミング、Localは実行場所を表す別々の設定です。

1. サイドバーで **Automations** を選択し、画面内の **New automation** をクリックします。
2. 名前欄に `Recap my recent work` などの分かりやすい名称を入力します。
3. **Trigger**で **Manual** を選択し、**Run in the cloud**はオフにします。Dailyなど別の値が選ばれている場合はManualに変更してください。公式には時刻やIssue・PRのイベントを使うトリガーもありますが、本演習では手動実行の結果を確認します。[公式の設定手順](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations#creating-an-automation)
4. リポジトリに変更を加えないよう、次のような読み取り専用のプロンプトを入力します。

   ```plaintext
   このリポジトリで過去1週間にマージされたPRを要約し、現在OpenのIssueを一覧にしてください。
   GitHubの最新情報を読み取り、対象リポジトリ、実行時点とタイムゾーン、集計した期間を最初に示してください。PRとIssueには番号・タイトル・URLを添え、PRはマージ日時、Issueは現在の状態が分かるようにしてください。
   件数と一覧を対応させ、取得できなかった情報は未確認と書いてください。
   読み取りと会話内の報告だけを行ってください。ファイル変更、Issue・PRの作成や更新、コメント投稿、コミット、push、マージは行わないでください。
   ```

5. **Select project** で自身の演習用 Tailspin Toys リポジトリを選択します（GitHub 連携とローカルフォルダーの両方が登録されている場合は、対象を取り違えないよう `owner/repository` 表記を必ず確認してください）。
6. **Create** ボタン横のメニューを展開し、**Create and run** を選択して保存と同時に即時実行します（保存のみを行う場合は Create を選択し、後から一覧の Run ボタンで実行することも可能です）。
7. **Recent runs**で実行結果を開き、実行場所がLocal、ステータスが **Succeeded** になったことを確認します。続いてレポートを読み、同じリポジトリ・期間・状態でGitHubの一覧と照合します。

Succeededは処理の終了状態です。調査対象を取り違えたり、マージ日時の範囲を誤ったりしても、文章を出力する処理自体は完了する場合があります。PRは「その期間にマージされたもの」を数えているか、Issueは「現在Openのもの」を取得しているかをそれぞれ確認してください。URLから個別の項目を開くと、件数が同じでも対象が違う場合に気づけます。

件数が一致しない場合は、リポジトリ名、集計開始・終了日時、マージ済みとClosedの区別、一覧取得の漏れを確認します。権限不足や取得失敗がある場合は、0件と断定せず未確認として報告されているかも読みます。プロンプトを修正したら再びManualで実行し、同じ確認をしてください。

### 集計範囲と結果を確認する

集計結果は、実行する時点と演習の進み具合によって変わります。レッスン7でマージした検索PRが期間内なら要約に含まれ、そのIssueがClosedになっていればOpen一覧から外れます。また、実行日が変われば「過去1週間」の範囲も変わります。決まった件数を正解とせず、出力に書かれた対象期間と実行時点を基準に確認してください。

照合中に別のPRがマージされたり、Issueの状態が変わったりした場合は、その変更時刻も見ます。日時、番号、URLを出力に含めるのは、件数の違いを調査条件の誤りと判断する前に、どの情報をいつ取得したかを追えるようにするためです。

> [!TIP]
> 公式ではCloud実行も案内されており、端末の電源が入っていない間にも実行できます。利用にはリポジトリや組織の設定などの前提があり、Toolsで作業に必要な操作を選びます。定期実行とCloud実行は発展課題です。試す場合は、[公式の前提条件と設定方法](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations#prerequisites-for-using-cloud-automations)を確認し、Manualで検証した調査範囲と結果の確認方法を引き継いでください。

## ベストプラクティス

本ワークショップでは、エージェントへ要件を渡す方法、進め方を決める方法、結果を検証する方法を段階的に学びました。指示ファイル、スキル、MCP、Canvas、Automationは、それぞれ違う課題に使います。どれか1つを導入して終えるのではなく、今回の作業で足りない情報や確認手段を考え、必要な機能を選んでください。

| 機能 | どのような場面で使うか | 人が確認すること |
| :--- | :--- | :--- |
| Instructions | リポジトリ共通の規約を伝える | Issueが求めるコメントと、生成されたコード例が一致するか |
| Skills | 繰り返す検査手順をまとめて使う | 必要な検査が実際に実行され、結果が成功したか |
| MCP | エージェントから外部ツールを操作する | 接続表示に加え、実ブラウザーで目的の操作ができたか |
| Canvas | 課題や成果物を同じ画面で比較・操作する | 最新一覧か、本文追加が実装を勝手に始めないか、別セッションでも使えるか |
| Agent Merge | レビュー後のPR監視とマージを任せる | 許可した操作、CI全ジョブの成功、AppとGitHubのMerged |
| Automations | 保存した調査条件で作業を繰り返す | 実行終了に加え、期間・一覧・件数がGitHubと一致するか |

指示ファイルやスキルを保存すると、次のセッションへチームの進め方を渡せます。ただし、書いた指示が期待どおりに適用されたかは、生成物と実行結果で確認します。公式の[カスタマイズの説明](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app)でも、指示、スキル、MCPを別の機能として扱っています。規約を伝えたいのか、手順を再利用したいのか、外部の情報や操作が必要なのかを先に整理すると選びやすくなります。

セッションのモードも、作業の段階に合わせて使います。Planでは、実装前に条件や影響範囲を読み、質問へ回答して計画を承認します。Interactiveでは、差分を見ながら修正の意図を細かく伝えられます。Autopilotへ進むときは、要件と検証方法に加えて、「ここまで進めたら止める」という範囲も示してください。たとえばレッスン4の実装を依頼するときは、レッスン5のMCP検証を終えるまでPRを作らないと指定します。工程の区切りを伝えることで、人が実画面を確認する時間を確保できます。[公式のモード説明](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions#choosing-a-session-mode)

次に別の機能を作るときは、「何を作るか」「なぜ必要か」「既存の何を維持するか」「どの結果なら完了か」を伝えてみてください。検索機能なら、検索対象はタイトルで、カテゴリ・出版社の条件とANDにし、既存の星評価を残すという要件がそれに当たります。期待する件数を実データから決め、テストと実画面の両方で確認する方法も再利用できます。

## さらに確認する価値のある機能

本教材で扱った流れを自分の仕事に適用するときは、次の機能も検討できます。以下は公式情報に基づく紹介で、本演習の完了条件には含めません。

- [**Chats**](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions#using-chats)：専用ブランチやworktreeを作る前に、疑問や要件を整理する会話。実装セッションに渡す前提を明確にするときに使えます。
- [**Rubber duck**](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions#using-the-rubber-duck-agent)：現在の計画、実装、テストへ具体的な批評を求める機能。指摘を受けた後は、要件と実データに照らして修正するかを判断します。
- [**Custom agents**][custom-agents]：特定の専門役割、専用ツール、個別指示をパッケージ化し、繰り返し呼び出せるカスタムエージェント
- [`/chronicle`][chronicle]：セッション履歴から最近の作業を振り返るためのコマンド。本章のAutomationはGitHubのPRとIssueを調べましたが、こちらはセッションでの作業履歴を調べる入口です。
- [**Cloud sandboxes**][sandboxes]：GitHubがホストする分離されたLinux環境でセッションを実行する機能。ローカルの開発環境から実行場所を変えたい場合に、利用条件と必要なツールを確認して検討します。
- [**Deep links**][deep-links]：特定のリポジトリ、セッション、初期プロンプトを指定した URL リンクからアプリを直接起動する機能

## 次のステップ

AI エージェントを自在に使いこなす最良の道は、日々の開発業務や個人プロジェクトで継続的に使い続けることです。プロダクションコードの保守、趣味のプログラミング、あるいは温めていた新しいアイデアのプロトタイプ構築にぜひ活用してください。学んだ知見をチームへ還元し、チーム固有の指示ファイルやスキルを育てていきましょう。

最初の実践では、小さな課題を1つ選び、完了条件と検証方法を言葉にしてから着手してください。作業後には、最初の指示で伝わったこと、レビューで補ったこと、次回も使える指示や確認手順を振り返ります。自動化できた操作だけでなく、どの判断を人が行ったかも残すと、次に任せる範囲を決めやすくなります。

たとえば、同じ調査を繰り返すならAutomation、チームで課題を比較するならCanvas、実ブラウザーで再現する必要があるならMCPを使います。今回もっとも手戻りした場面を1つ選び、その原因に合う機能と確認方法を説明できれば、機能名を覚えるだけでなく自分の作業に応用できます。

GitHub Copilot エコシステムの全容をさらに深く学ぶには、以下の関連教材も合わせて参照してください。

- [VS Code ハーネス](https://github-samples.github.io/copilot-workshops/vscode/)
- [Copilot CLI ハーネス](../cli/README.md)（本教材の参考コース）
- [Cloud agent ハーネス](https://github-samples.github.io/copilot-workshops/cloud/)

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
[sandboxes]: https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/about-cloud-and-local-sandboxes
[chronicle]: https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions#using-chronicle-with-app-sessions
[custom-agents]: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-custom-agents
[deep-links]: https://docs.github.com/copilot/how-tos/github-copilot-app/open-with-deep-links
