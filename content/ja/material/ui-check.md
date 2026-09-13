# App の UI が教材と異なるとき

## 画像の位置だけで操作を探さない

「常設メニューがなくなり、右クリックから操作するようになった」という情報が寄せられています。2026年9月13日に Windows の App 1.1.20 で一部の表示を確認しました。確認結果は次節に記録しています。最初の報告が指していた操作や、過去のメニューからの移動は未特定です。

1. **対象を確認する**：リポジトリ、Issue、セッション、変更ファイル、PR のどれを操作する章かを本文から確認します。対象と現在の状態が違うと、操作が表示されないことがあります。
2. **目的を確認する**：「セッションを開始する」「変更をレビューする」「PR を作る」など、やりたい操作を確認します。
3. **講師と入口を探す**：常設メニューや対象付近の操作ボタンに加え、対象の右クリック／コンテキストメニューも確認候補です。そこに必ず目的の項目があるとは限りません。OS のコンテキストメニュー操作方法も確認します。
4. **実行前に照合する**：項目名、対象、作用を確認します。似た名前の merge・削除・自動化を試し押ししないでください。
5. **見つからなければ停止する**：講師の現行 App デモかペア操作へ切り替えます。CLI の実装成功で App 演習を完了したことにはしません。

## 2026年9月13日の実機確認

Windows（ビルド 26200.9445、25H2）、GitHub Copilot App 1.1.20。利用者によるサインイン後、演習用リポジトリ未接続の状態で確認しました。

| 対象・開始状態 | 開き方 → 項目名 | 確認した結果 | 残る確認 |
| --- | --- | --- | --- |
| 初期設定・候補未選択 | Connect your repositories → Continue → テーマ画面 | リポジトリを選ばずホームへ進める。利用者操作を挟んで完了を確認 | 演習コピーの接続 |
| サイドバー・プロジェクト未接続 | Projects の + → Add GitHub repository / Clone repository / Open folder | 3種類の追加入口を表示 | clone 完了・対象 repo の照合 |
| 会話・プロジェクト未接続 | Chats の +（New chat）→ Chat → 質問を送信 | worktree の説明が日本語で返り、Idle になった | 実装用セッションの worktree 動作 |
| 完了したチャット | Chats の一覧項目を右クリック | Rename、Pin、Mark as unread、Show in Explorer、Share as secret gist、Copy、Archive、Delete を表示 | 各操作の実行、実装用セッションとの違い、旧 UI からの移動 |
| MCP 未登録 | Customize → Installed → MCP Servers | 未登録の表示を確認 | 登録保存後の表示 |
| MCP カタログ | Customize → MCP → Playwright | Local / npx / -y @playwright/mcp@latest の登録フォームを表示 | Add server の保存、接続・ツール実行 |

右クリックはチャットの管理メニューで確認したもので、PR 作成や Agent Merge の入口を確認したことにはなりません。削除・共有・アーカイブは実行していません。

## 講師が現行 App で確認する操作

| 章 | 操作対象 | 学ぶ操作 | 入口・表記と確認範囲 |
| --- | --- | --- | --- |
| 1 | リポジトリ・Issue | 接続、バックログ確認 | Projects の + で追加入口を確認。My work の表示あり。バックログは未確認 |
| 2 | リポジトリ・セッション | 開始、差分レビュー、実行、PR | New session、Changes、Terminal、Create PR、Ready to merge |
| 3 | Issue・指示ファイル | Issue から開始、ファイル確認、PR | My work → New session、Toggle review panel |
| 4 | Issue・セッション | 計画承認、自律実装、スキル | Plan、Autopilot、Changes、レビュー領域 |
| 5 | カスタマイズ・セッション | MCP 登録とツール実行 | Customize → MCP、Installed、Playwright 登録フォームを実機確認。保存とツール実行は未確認 |
| 6 | PR・セッション | Agent Merge と許可範囲の設定 | Create PR のドロップダウン、Agent merge |
| 7 | Canvas・セッション | 作成、保存、開く、Issue 操作 | Home screen、New session、Agent merge |
| 8 | Automation | 作成、手動トリガー、結果確認 | Automations → New automation、Manual |

演習5は2026年9月10日に [公式文書](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app#configuring-mcp-servers)と照合し、9月13日に上記の範囲を実機確認しました。その他の操作は、対象を選択した状態で常設メニューとコンテキストメニューのどちらに表示されるかを確認します。権限、セッション種別、実行状態で表示が変わる場合は条件も記録します。

[Issue・PR の公式手順](https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests)も確認しましたが、対象操作が右クリックへ移ったという情報はこの文書では裏付けられませんでした。実機の確認が必要です。

## 画像の更新・配布判定

参照元から取り込んだ既存画像の撮影時バージョンは不明です。参照用として残し、現行画面と誤認しない注記を表示します。新たな実機画像は `sources.json` の `ui_captures` に確認日・バージョン・確認範囲を記録し、生成 HTML でも参照画像と異なる注記を表示します。未確認の画面を架空画像で置き換えません。

| 章 | 新規撮影画像 | 確認範囲 |
| --- | --- | --- |
| 5 | `app-1.1.20-20260913-mcp-catalog.jpg` | MCP カタログに Playwright が表示される |
| 5 | `app-1.1.20-20260913-mcp-config.jpg` | Playwright の登録フォーム・保存前 |

講師は各操作について、OS・App のバージョン・確認日・操作対象・開始状態・開き方（通常メニュー／右クリック等）・表示された項目名・操作後の結果を記録してください。現行画像を撮り直す場合はアカウント・非公開情報を写さず、本文の経路と同じ状態で撮影します。

本番用教材として配布する前に、必須操作の経路と画像を照合し、[章別の検証状況](verification.md)を更新します。確認できない章は講師デモまたは延期として案内します。

## 参照画像の確認対象

以下は取り込み済み画像の一覧です。「未確認」は画像が誤っていると断定する意味ではなく、現行 App との照合が済んでいないことを表します。演習0の画像は GitHub Web 側です。

| 章 | 画像ファイル | 状態 |
| --- | --- | --- |
| 0 | `app-0-use-template.png` | 未確認 |
| 0 | `app-0-create-repository.png` | 未確認 |
| 2 | `app-2-start-session.png` | 未確認 |
| 2 | `app-2-review-panel.png` | 未確認 |
| 2 | `app-terminal-screenshot.png` | 未確認 |
| 3 | `app-2-review-panel.png` | 未確認 |
| 3 | `app-show-folder-view.png` | 未確認 |
| 3 | `app-new-session-from-issue.png` | 未確認 |
| 3 | `app-select-changes.png` | 未確認 |
| 4 | `app-new-session-from-issue.png` | 未確認 |
| 4 | `app-4-plan-mode.png` | 未確認 |
| 4 | `app-select-changes.png` | 未確認 |
| 4 | `app-terminal-screenshot.png` | 未確認 |
| 4 | `app-2-review-panel.png` | 未確認 |
| 6 | `app-enable-agent-merge.png` | 未確認 |
| 6 | `app-agent-merge-merge.png` | 未確認 |
| 7 | `app-enable-agent-merge.png` | 未確認 |
| 7 | `app-agent-merge-merge.png` | 未確認 |
