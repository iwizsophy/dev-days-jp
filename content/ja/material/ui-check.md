# App の UI が教材と異なるとき

## 1. 操作探索の原則と推測の排除

### テンプレート取得先の変更と画面例
演習0のテンプレート取得先は、修正済みの非公開リポジトリ `iwizsophy/dev-days-tailspin-template` へ変更しています。GitHub Web の掲載画像2点は、取得先変更前の操作位置を示した例です。実際の操作では、本文に記載された取得先を選択してください。なお、新テンプレートの API による複製、初期課題8件の自動作成、および CI 成功は実機確認済みです。

### 「右クリック移行」の情報に対する調査と注意点
「常設メニューがなくなり、右クリックから操作するようになった」という情報が寄せられていますが、2026年9月13日に Windows の App 1.1.20 で実機確認した結果は以下の通りです。
- PR 行の右クリックでは `New session`、`Chat`、`Copy link` が表示されましたが、`Create PR` や `Agent Merge` 自体はコンテキストメニュー内に存在しませんでした。
- 公式ドキュメント（[Issue/PR 管理](https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests)、[MCP 設定](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app#configuring-mcp-servers)）も確認しましたが、対象操作が右クリックへ移ったという裏付けは取れていません。
- 当初の報告が指していた具体的な操作や、過去の常設メニューから実際に移動したのかどうかは**未特定**のままです。

したがって、**画面上の「画像の位置」だけで操作を探したり、見つからない機能に対して推測で操作を案内したりしてはなりません。**

### UI 確認の 5 ステップ
受講者が操作に迷った場合は、次の順序で確認を進めてください。

1. **対象を確認する**：リポジトリ、Issue、セッション、変更ファイル、PR のどれを操作する場面かを本文から確認します（対象と現在の画面状態が食い違っていると、必要な操作が表示されない場合があります）。
2. **目的を確認する**：「セッションを開始する」「変更をレビューする」「PR を作る」など、何をしたいのかを明確にします。
3. **講師と入口を探す**：常設メニューや対象付近のボタンに加え、対象の右クリック／コンテキストメニューも候補として確認します（ただし、そこに必ず目的の項目があるとは限りません。OS のコンテキストメニュー操作方法も併せて確認します）。
4. **実行前に照合する**：項目名、作用対象、実際の動作を慎重に確認します。似た名前の merge、削除、自動化などを安易に試し押ししないでください。
5. **見つからなければ停止する**：講師の現行実機デモまたはペア操作へ切り替えます。CLI で実装が進んだとしても、それを App 演習の完了とはみなしません。

## 2. 2026年9月13日の実機確認記録

Windows（ビルド 26200.9445、25H2）、GitHub Copilot App 1.1.20。初期設定および未接続状態を確認後、ローカルコピーと GitHub 連携プロジェクトをそれぞれ追加して検証しました。

| 対象・開始状態 | 開き方 → 項目名 | 確認した結果 | 残る確認事項 |
| :--- | :--- | :--- | :--- |
| 初期設定・候補未選択 | Connect your repositories → Continue → テーマ画面 | リポジトリを選ばずにホームへ進める。利用者操作を挟んで完了を確認 | 演習コピーの接続は後続で確認済み |
| サイドバー・プロジェクト未接続 | Projects の + → Add GitHub repository / Clone repository / Open folder | 3種類の追加入口が表示されることを確認 | clone 完了および対象 repo の照合 |
| ローカルコピー | Projects の + → Open folder → 対象フォルダー | 既存 checkout を直接使用。設定レビュー後に確認画面が停滞したが、完全再起動後に読み取り応答が成功 | worktree 分離・セットアップ実行 |
| My work・ローカルフォルダーのみ登録 | Add GitHub repository → owner/repo を検索 → 自分の演習コピー | 「No GitHub repositories yet」から8件の Issue 一覧へ変化。ローカルフォルダーとは別のプロジェクトが追加された | Issue からの実装・PR は演習3・4で確認済み |
| ローカルプロジェクト・新規セッション | プロジェクト横の + → New → 入力欄下部のプロジェクト名 → 送信 | 星評価の実装セッションが開始し、既存 checkout 上に指定した作業ブランチを作成 | GitHub 連携経路との相違 |
| ローカル実装セッション・パネル未表示 | Toggle panel → Workspace | Browser、Terminal、Files、Canvas を表示。Changes や Create PR はこの状態では表示されなかった | GitHub 連携セッションの差分・PR 操作 |
| ローカル実装セッション・PR 作成依頼 | エージェントのプロジェクト連携 PR ツール → gh CLI に切替 | App 固有ツールはアカウント連携エラー。承認後、エージェントが gh 経由で検証用 PR #9 を作成し CI 全4ジョブ成功 | App 固有の Create PR・マージ（Ready to merge は My work 側で表示確認） |
| GitHub 連携・作成済み PR | My work → PR #9 → Changes / Ready to merge | 5ファイルの差分と Checks: Passed を表示。Merge pull request ダイアログに All checks have passed・No unresolved comments・Merge pull request・Choose merge method（Merge commit）を表示 | 通常マージ成功。Agent merge は後続 PR #12～14 で確認済み |
| GitHub 連携・既存 Issue | My work → Update our repository coding standards → New session options | New session・New session in repository...・Chat を表示 | New session で専用 worktree 作成・マージ済み HEAD の継承を確認。設定承認後に送信・指示更新・検査・PR #10 作成を確認（詳細は実走記録） |
| My work・PR 一覧行 | PR #9 の行を右クリック | New session・Chat・Copy link を表示 | 旧 UI から移動したかは未特定 |
| ローカルプロジェクト | Projects のフォルダー項目を右クリック → Settings | New session・Show in Explorer・Settings・Hide・Customize…・Manage sessions・Remove folder を表示。Settings には GitHub Account の登録名が表示された | アカウント連携エラーの原因・復旧 |
| GitHub 連携・Issue から作った実装セッション | Open changes → Changes (7) → 上部 Create PR | 7ファイルの差分を表示。App がコミット・push・PR #10 作成を実行し Ready to merge に変化 | 通常マージとフィルター用 worktree への継承を確認済み |
| GitHub 連携・PR 作成後 | Ready to merge options | Agent merge の切り替えを表示 | 後続 PR #12～14 で有効化・許可範囲・実行を確認済み |
| GitHub 連携・Issue #7 の新規セッション | Mode: Interactive → Plan → Review plan → Approve and implement this plan → Continue | 計画への質問に回答でき、承認後 Mode: Autopilot に切替。実装と検査を実行 | MCP による通常データの絞り込み検証を確認済み |
| GitHub 連携・リポジトリに .mcp.json が存在 | プロジェクトを右クリック → Settings → MCP servers | 本人の信頼承認後、servers → mcpServers 修正で3件が Connected。/restart-session 後、同じセッションから MCP ブラウザー操作成功 | 追加実走で一時隔離 DB のフィルター0件も確認済み |
| 会話・プロジェクト未接続 | Chats の +（New chat）→ Chat → 質問を送信 | worktree の説明が日本語で返り、Idle になった | GitHub 連携の実装用セッションでは後続章で worktree 分離を確認済み |
| 完了したチャット | Chats の一覧項目を右クリック | Rename、Pin、Mark as unread、Show in Explorer、Share as secret gist、Copy、Archive、Delete を表示 | 各操作の実行、実装用セッションとの違い、旧 UI からの移動 |
| MCP 未登録 | Customize → Installed → MCP Servers | 未登録からカタログ保存後の Installed 1 への変化を確認 | 既存登録がある場合は重複追加しない |
| MCP カタログ | Customize → MCP → Playwright | Local / npx / -y @playwright/mcp@latest を Add server で保存。新しい Chats で browser_tabs が成功 | 検索欄の操作は未検証 |
| GitHub Web・テンプレート | Use this template → Create a new repository | 作成フォームのテンプレート・Owner・Repository name・Choose visibility・Create repository を確認 | Private でフォーム送信成功。新コピーの Bootstrap 成功・課題8件を確認 |
| GitHub 連携・ファイル閲覧 | Toggle panel → Add tab → Files → Ctrl+P（Go to file） | copilot-instructions.md を検索して表示。View options → Show hidden files で .github がファイルツリーに表示 | 操作経路は確認済み |
| GitHub 連携・保存済みキャンバス | New → New worktree/main → Canvas を開く → Add to current session → Plan | PR #14 の修正を継承し、1通知・1応答の後、計画承認から検索実装へ移行。テスト・MCP・PR #15 の Agent Merge 成功 | 開き直し・Refresh 後に未完了5件（#2～#6）。GitHub と一致 |
| GitHub 連携・Run 未実行 | Run options → Run development site → Run ボタン | 項目選択だけでは開始せず、Run ボタンで起動。Stop Run development site で停止 | 自動セットアップの終了ログは未取得 |

> [!NOTE]
> 新版 v2026.09.13.1 のローカルセッションでは Run options の項目選択後に自動起動したため、画面上の「Run」および「Stop」の表示状態で実行状態を判断します。App 1.1.20 にて起動・停止を2回確認し、App 内ブラウザー表示、HTTP 200 の応答、停止後のポート解放を確認しました（詳細は [実走記録](verification.md) を参照）。
> 右クリック操作はチャット管理・PR 一覧行・ローカルプロジェクトで確認されましたが、PR 行に存在したのは New session・Chat・Copy link であり、Create PR や Agent Merge はありませんでした。過去の常設メニューから移行したのかは未特定です。なお、削除・共有・アーカイブ操作の実行は行っていません。

## 3. 講師が現行 App で確認すべき操作一覧

| 章 | 操作対象 | 学ぶ操作 | 入口・表記と確認範囲 |
| :--- | :--- | :--- | :--- |
| **1** | リポジトリ・Issue | 接続、バックログ確認 | Projects の `+` で追加入口を確認。My work に演習コピーの8件のバックログ Issue を表示 |
| **2** | リポジトリ・セッション | 開始、差分レビュー、実行、PR | `New session`、`Changes`、`Terminal`、`Create PR`、`Ready to merge` |
| **3** | Issue・指示ファイル | Issue から開始、ファイル確認、PR | My work → `New session`、Toggle panel → Add tab → `Files` → `Ctrl+P` |
| **4** | Issue・セッション | 計画承認、自律実装、スキル | `Plan`、`Autopilot`、`Changes`、レビュー領域 |
| **5** | カスタマイズ・セッション | MCP 登録とツール実行 | リポジトリ定義の形式修正および `/restart-session` 後の MCP ツール実行を確認。カタログ保存・新規チャットでの `browser_tabs` 実行も成功 |
| **6** | PR・セッション | Agent Merge と許可範囲の設定 | Create PR options → Agent merge → `Agent merge`。`Merge pull request` 有効化後、CI 成功と自動マージを確認 |
| **7** | Canvas・セッション | 作成、保存、開く、Issue 操作 | `New` → `New worktree/main`、共有保存、Agent Merge、別セッションでの再表示、`Add to current session`、Plan 承認後の実装と PR #15 統合を確認（反復送信は修正済み） |
| **8** | Automation | 作成、手動トリガー、結果確認 | Automations → `New automation` → `Trigger: Manual` → `Select project` → `Create and run` → `Recent runs`。Local / Succeeded と出力を確認 |

演習5は2026年9月10日に [公式文書](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app#configuring-mcp-servers) と照合し、9月13日に実機確認しました。その他の操作についても、対象を選択した状態で常設メニューとコンテキストメニューのどちらに表示されるかを確認してください。権限、セッション種別、実行状態によって表示が変化する場合は、その条件も併せて記録します。

## 4. 掲載画像の更新方針と配布判定

参照元から取り込んだ既存画像の撮影時バージョンは不明です。元画像ファイルは参照用として保管していますが、App 本編からの旧画像参照は2026年9月13日の実機画像へ差し替えました。
新たな実機画像は `sources.json` の `ui_captures` に確認日・バージョン・確認範囲を記録し、生成 HTML でも原本画像と異なる旨の注記を表示します。未確認の画面を架空の画像で置き換えることは行いません。

### 新規撮影画像一覧（全13点）

| 章 | 新規撮影画像 | 確認範囲と留意事項 |
| :--- | :--- | :--- |
| **2** | `app-1.1.20-20260913-star-rating.jpg` | Run で起動した星評価一覧。停止後に Browser パネルへ残った表示 |
| **5** | `app-1.1.20-20260913-mcp-catalog.jpg` | MCP カタログに Playwright が表示される状態 |
| **5** | `app-1.1.20-20260913-mcp-config.jpg` | Playwright の登録フォーム（保存前） |
| **0** | `app-1.1.20-20260913-template-menu.png`<br>`app-1.1.20-20260913-template-form.png` | GitHub Web のテンプレート取得入口と作成フォーム上部（送信前） |
| **2** | `app-1.1.20-20260913-new-session.png` | New 画面の入力欄、リポジトリ、worktree、ブランチ指定 |
| **2・3・4** | `app-1.1.20-20260913-changes.png` | 会話欄の Changes と差分パネル（検索機能実装中の操作例） |
| **2・4** | `app-1.1.20-20260913-run-menu.png` | Run options の選択メニュー（検索機能 PR 作成後の操作例） |
| **3・4** | `app-1.1.20-20260913-add-tab.png` | 右パネルの Files・Browser・Terminal の追加入口 |
| **3** | `app-1.1.20-20260913-file-search.png`<br>`app-1.1.20-20260913-files-options.png` | Go to file と Show hidden files の操作位置 |
| **3・4** | `app-1.1.20-20260913-issue-session.png` | My work の Issue 一覧と New session（並べ替え Issue は未着手） |
| **4・7** | `app-1.1.20-20260913-plan-mode.png`<br>`app-1.1.20-20260913-plan-review.png` | 検索 Issue のコンテキスト追加後の Canvas、モード選択、計画承認 |
| **6・7** | `app-1.1.20-20260913-agent-merge-menu.png`<br>`app-1.1.20-20260913-agent-merge-permissions.png` | Agent merge 選択と PR 作成後の許可状態（検索機能 PR の操作例） |

新規追加した13点は撮影範囲を切り抜かず、App 全体（1282×892）または GitHub Web の表示範囲全体（1265×712）を掲載しています。個人アカウント、非公開リポジトリ名、ローカルパス、個人の利用量のみを灰色でマスクし、それ以外の画素および画像寸法は原本と同一です。操作例が本文の演習と異なる場合は画像注記に明記し、実装対象や検証成功の証拠を取り違えないように配慮しています。

講師は各操作について、OS、App バージョン、確認日、操作対象、開始状態、開き方（通常メニュー／右クリック等）、表示された項目名、および操作後の結果を記録してください。画像を撮り直す場合は、個人情報や非公開情報を写さず、本文の経路と同じ状態で撮影します。
本番教材として配布する前に必須操作の経路と画像を目視照合し、[章別の検証状況](verification.md) を更新してください。確認できない章は講師デモまたは延期として扱います。

### 旧参照画像の差し替え状況

以下は旧画像の本文中での扱いです（旧画像の撮影時バージョンを確定したという意味ではありません）。

| 章 | 旧画像ファイル | 現在の状態 |
| :--- | :--- | :--- |
| **0** | `app-0-use-template.png` | 現行の template-menu 実機画像へ差し替え |
| **0** | `app-0-create-repository.png` | 現行の template-form 実機画像へ差し替え |
| **2** | `app-2-start-session.png` | 現行の new-session 実機画像へ差し替え |
| **2** | `app-2-review-panel.png` | 現行の changes / add-tab 実機画像へ差し替え |
| **2** | `app-terminal-screenshot.png` | 本文から除去。実走した Run メニューによる起動・停止へ更新 |
| **3** | `app-2-review-panel.png` | 現行の changes / add-tab 実機画像へ差し替え |
| **3** | `app-show-folder-view.png` | 本文から除去。Files・Go to file・Show hidden files の現行経路を確認 |
| **3** | `app-new-session-from-issue.png` | 現行の issue-session 実機画像へ差し替え |
| **3** | `app-select-changes.png` | 現行の changes 実機画像へ差し替え |
| **4** | `app-new-session-from-issue.png` | 現行の issue-session 実機画像へ差し替え |
| **4** | `app-4-plan-mode.png` | 現行の plan-mode 実機画像へ差し替え |
| **4** | `app-select-changes.png` | 現行の changes 実機画像へ差し替え |
| **4** | `app-terminal-screenshot.png` | 本文から除去。実走した Run メニューによる起動・停止へ更新 |
| **4** | `app-2-review-panel.png` | 現行の changes / add-tab 実機画像へ差し替え |
| **6** | `app-enable-agent-merge.png` | 現行の agent-merge-menu 実機画像へ差し替え |
| **6** | `app-agent-merge-merge.png` | 現行の agent-merge-permissions 実機画像へ差し替え |
| **7** | `app-enable-agent-merge.png` | 現行の agent-merge-menu 実機画像へ差し替え |
| **7** | `app-agent-merge-merge.png` | 現行の agent-merge-permissions 実機画像へ差し替え |

## 5. 操作による回避の判定基準（2026年9月13日）

App 本体のコード修正は本教材の対象外です。`Open folder` における設定画面の停滞および PR 作成時のアカウントエラーは、**開始時から `Add GitHub repository` を使用する教材経路を採用することで回避**します。

- 新コピーにおいて、設定承認、最初の応答、依存導入後の App ビルド（24ページ生成、Complete!）を確認しました。
- GitHub 連携側の `Create PR` は、既存の検証用 PR #10 で成功済みです。
- セットアップ単独の終了コード取得や、`Open folder` 経路自体の修復は未確認のままであり、教材の回避経路の完了条件には含めません。
- 作業ツリーの未コミット変更が自動で別経路へ移動することはないため、GitHub 連携への切り替えは演習開始前に行うことを基本とします。
