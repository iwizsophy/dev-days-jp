# App の UI が教材と異なるとき

## 画像の位置だけで操作を探さない

「常設メニューがなくなり、右クリックから操作するようになった」という情報が寄せられています。2026年9月13日に Windows の App 1.1.20 で一部の表示を確認しました。確認結果は次節に記録しています。最初の報告が指していた操作や、過去のメニューからの移動は未特定です。

1. **対象を確認する**：リポジトリ、Issue、セッション、変更ファイル、PR のどれを操作する章かを本文から確認します。対象と現在の状態が違うと、操作が表示されないことがあります。
2. **目的を確認する**：「セッションを開始する」「変更をレビューする」「PR を作る」など、やりたい操作を確認します。
3. **講師と入口を探す**：常設メニューや対象付近の操作ボタンに加え、対象の右クリック／コンテキストメニューも確認候補です。そこに必ず目的の項目があるとは限りません。OS のコンテキストメニュー操作方法も確認します。
4. **実行前に照合する**：項目名、対象、作用を確認します。似た名前の merge・削除・自動化を試し押ししないでください。
5. **見つからなければ停止する**：講師の現行 App デモかペア操作へ切り替えます。CLI の実装成功で App 演習を完了したことにはしません。

## 2026年9月13日の実機確認

Windows（ビルド 26200.9445、25H2）、GitHub Copilot App 1.1.20。初期設定と未接続状態の確認後、ローカルコピーと GitHub 連携プロジェクトをそれぞれ追加しました。

| 対象・開始状態 | 開き方 → 項目名 | 確認した結果 | 残る確認 |
| --- | --- | --- | --- |
| 初期設定・候補未選択 | Connect your repositories → Continue → テーマ画面 | リポジトリを選ばずホームへ進める。利用者操作を挟んで完了を確認 | 演習コピーの接続 |
| サイドバー・プロジェクト未接続 | Projects の + → Add GitHub repository / Clone repository / Open folder | 3種類の追加入口を表示 | clone 完了・対象 repo の照合 |
| ローカルコピー | Projects の + → Open folder → 対象フォルダー | 既存 checkout を直接使用。設定レビュー後に確認画面が停止したが、完全再起動後に読み取り応答が成功 | worktree 分離・セットアップ実行 |
| My work・ローカルフォルダーのみ登録 | Add GitHub repository → owner/repo を検索 → 自分の演習コピー | No GitHub repositories yet から8件の Issue 一覧へ変化。ローカルフォルダーとは別のプロジェクトが追加された | Issue からの実装・PR |
| ローカルプロジェクト・新規セッション | プロジェクト横の + → New → 入力欄下部のプロジェクト名 → 送信 | 星評価の実装セッションが開始し、既存 checkout 上に指定した作業ブランチを作成 | GitHub 連携経路との相違 |
| ローカル実装セッション・パネル未表示 | Toggle panel → Workspace | Browser、Terminal、Files、Canvas を表示。Changes や Create PR はこの状態では表示されなかった | GitHub 連携セッションの差分・PR 操作 |
| ローカル実装セッション・PR 作成依頼 | エージェントのプロジェクト連携 PR ツール → gh CLI に切替 | App 固有ツールはアカウント連携エラー。承認後、エージェントが gh 経由で検証用 PR #9 を作成し CI 全4ジョブ成功 | App 固有の Create PR・マージ（Ready to merge は My work 側で表示確認） |
| GitHub 連携・作成済み PR | My work → PR #9 → Changes / Ready to merge | 5ファイルの差分と Checks: Passed を表示。Merge pull request ダイアログに All checks have passed・No unresolved comments・Merge pull request・Choose merge method（Merge commit）を表示 | 通常マージは利用者承認後に成功。Agent merge は未実施 |
| GitHub 連携・既存 Issue | My work → Update our repository coding standards → New session options | New session・New session in repository...・Chat を表示 | New session で専用 worktree 作成・マージ済み HEAD の継承を確認。設定承認後に送信・指示更新・検査・PR #10 作成を確認（詳細は実走記録） |
| My work・PR 一覧行 | PR #9 の行を右クリック | New session・Chat・Copy link を表示 | 旧 UI から移動したかは未特定 |
| ローカルプロジェクト | Projects のフォルダー項目を右クリック → Settings | New session・Show in Explorer・Settings・Hide・Customize…・Manage sessions・Remove folder を表示。Settings には GitHub Account の登録名が表示された | アカウント連携エラーの原因・復旧 |
| GitHub 連携・Issue から作った実装セッション | Open changes → Changes (7) → 上部 Create PR | 7ファイルの差分を表示。App がコミット・push・PR #10 作成を実行し Ready to merge に変化 | PR #10 のマージ・後続章への継承 |
| GitHub 連携・PR 作成後 | Ready to merge options | Agent merge の切り替えを表示 | 有効化・許可範囲・実行 |
| GitHub 連携・Issue #7 の新規セッション | Mode: Interactive → Plan → Review plan → Approve and implement this plan → Continue | 計画への質問に回答でき、承認後 Mode: Autopilot に切替。実装と検査を実行 | 新規実装の MCP 検証 |
| GitHub 連携・リポジトリに .mcp.json が存在 | プロジェクトを右クリック → Settings → MCP servers | 本人の信頼承認後、servers → mcpServers 修正で3件が Connected。既存セッションはツール未公開を報告 | セッション再読み込み・MCP 実行 |
| 会話・プロジェクト未接続 | Chats の +（New chat）→ Chat → 質問を送信 | worktree の説明が日本語で返り、Idle になった | 実装用セッションの worktree 動作 |
| 完了したチャット | Chats の一覧項目を右クリック | Rename、Pin、Mark as unread、Show in Explorer、Share as secret gist、Copy、Archive、Delete を表示 | 各操作の実行、実装用セッションとの違い、旧 UI からの移動 |
| MCP 未登録 | Customize → Installed → MCP Servers | 未登録の表示を確認 | 登録保存後の表示 |
| MCP カタログ | Customize → MCP → Playwright | Local / npx / -y @playwright/mcp@latest の登録フォームを表示 | Add server の保存、接続・ツール実行 |

右クリックはチャット管理・PR 一覧行・ローカルプロジェクトで確認しました。PR 行には New session・Chat・Copy link があり、Create PR や Agent Merge はありませんでした。過去の常設メニューから移動したかは未特定です。削除・共有・アーカイブは実行していません。

## 講師が現行 App で確認する操作

| 章 | 操作対象 | 学ぶ操作 | 入口・表記と確認範囲 |
| --- | --- | --- | --- |
| 1 | リポジトリ・Issue | 接続、バックログ確認 | Projects の + で追加入口を確認。My work に演習コピーの8件のバックログ Issue を表示 |
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
| 2 | `app-1.1.20-20260913-star-rating.jpg` | Run で起動した星評価一覧。停止後に Browser パネルへ残った表示 |
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
