---
title: "演習 3 - GitHub Copilot CLI でプロジェクト機能を追加する"
authors:
  - geektrainer
lastUpdated: 2026-06-30
---

GitHub Copilot CLI における最も中核的な作業は、プロジェクトへの新機能の実装やコードの追加です。本演習では、バックログにある Issue を取り上げ、Copilot CLI と協調しながらフィルター機能を完成させます。

## シナリオ

Web サイトのゲーム一覧にフィルター機能を実装します。バックログにはすでにフィルタリング機能に関する Issue が登録されており、前の演習でその土台となるデータアクセス関数（publishers helper）を追加済みです。Copilot に Issue の詳細を取得させ、既存の作業成果を踏まえたうえで残りの UI およびデータ処理を実装させます。

この演習では、次の内容を学習します。

- Plan モード（`/plan`）を活用して、フィルター機能の実装計画を策定する
- 策定した計画を承認し、Web サイトにフィルタリング機能を追加するコードを自律生成させる
- `/diff` コマンドを用いて生成されたコードの差分をレビューする

## Plan モードを活用する

生成 AI の最も有効な活用法の1つが「実装前の計画づくり」です。作りたい機能の大まかなイメージがあっても、実装手順の整理や設計上の落とし穴の洗い出しは不可欠です。AI は追加の質問を投げかけたり、考慮漏れを一緒に検討したりすることで、設計方針を明確にする強力な壁打ち相手となります。

Copilot CLI の Plan モードはまさにこの設計プロセスを支援する機能であり、事前に十分な計画を練ることで、要件に合致した高品質なコードを生成させることができます。

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

1. Copilot CLI のプロンプトに次の指示を入力し、Issue に基づく計画の策定を指示します。

   ```plaintext
   /plan リポジトリからフィルタリング追加に関する Issue を取得してください。src/lib/publishers.ts の helper は前の演習で追加済みなので、その作業を前提に、残りのゲームのフィルタリング処理、UI、テストを計画してください。
   ```

2. 計画の策定過程で、Copilot から仕様や設計に関する追跡質問が表示される場合があります。自身の実装方針に沿って回答してください。
3. 計画が生成されたら、提示された設計内容をレビューします。データアクセス層や UI コンポーネントの変更だけでなく、単体テストや結合テストの追加が盛り込まれていることを確認してください。
4. 計画に対して修正や改善の要望があれば、プロンプトからフィードバックを入力します。Copilot は要望を反映した新しいバージョンの計画を再提示します。
5. 提示された計画に問題がなければ、実装開始の選択肢を選んでコード生成へ進みます。

> [!NOTE]
> Copilot の出力は確率的に動作するため、表示される選択肢の文言はセッションごとに多少異なりますが、通常は次のような Autopilot モードへの移行を伴う選択肢が表示されます。
>
> `Yes, and switch to autopilot mode`
>
> [Autopilot モード](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot) を有効にすると、エージェントはステップごとの人間の入力を待たずに自律して作業を進めます。タスク完了と判断するまで、ファイルの作成・編集、テスト実行、エラー発生時の自己修正を連続して実行します。本ワークショップは分離された Codespace 環境で実行しているため、Autopilot を有効にして自律実行させて問題ありません。

6. Copilot がファイルの作成および編集を開始します。

> [!NOTE]
> 実装処理の完了には数分かかる場合があります。エージェントがファイルを編集し、テストコードを生成し、テストが成功することを確認する様子がターミナル上に順次出力されます。

## コードをレビューする

AI が生成したコードは、マージ前に必ず人間がレビューする必要があります。Copilot CLI の組み込みコマンドを使って変更差分を確認しましょう。

1. Copilot CLI で次のコマンドを入力し、変更の差分ビューを表示します。

   ```plaintext
   /diff
   ```

2. 変更されたファイルの一覧と差分を精査します。CLI 1.0.83 では、左右の矢印キーでファイルツリーと差分ペインを切り替え、上下矢印キーでスクロールやファイル選択を行います（操作時は画面下部に表示されるキーガイドを優先してください）。  
   フィルターコントロールが追加されたゲーム一覧ページ（`src/pages/games/index.astro` 等）、データアクセス関数（`src/lib/games.ts`）、および対応するテスト（`games.test.ts` 等）が更新されていることを確認します（必要に応じて `src/lib/publishers.ts` に細微な調整が入る場合もあります）。

## まとめと次のステップ

Copilot CLI の支援を受け、Web サイトにフィルター機能を実装しました。本演習で実施した主な内容は次の通りです。

- Plan モード（`/plan`）を活用して、Issue に基づく実装計画を策定した
- Autopilot モードに切り替え、コード生成からテスト実行までを自律的に遂行させた
- `/diff` コマンドを用いて変更差分をレビューした

コードが完成しましたので、次はブラウザー上で実際の動作を検証します。[演習 4 - Playwright MCP によるテスト][next-lesson] へ進んでください。

## リソース

- [Copilot CLI を使う][using-copilot-cli]
- [Copilot CLI について][about-copilot-cli]
- [Copilot CLI のコンテキスト管理][context-management]

[previous-lesson]: 2-custom-instructions.md
[next-lesson]: 4-mcp.md
[using-copilot-cli]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli
[about-copilot-cli]: https://docs.github.com/copilot/concepts/agents/about-copilot-cli
[context-management]: https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#context-management
