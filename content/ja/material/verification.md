# App シナリオの検証状況

本ドキュメントは、Windows 環境の GitHub Copilot App 1.1.20 における実機検証の記録です。接続、星評価、指示更新、フィルター実装と次章への継承、Playwright MCP、Agent Merge（自動マージ）、Canvas（共有保存・反復送信バグ修正・別セッション再表示）、Automation（手動実行）を確認しました。

> [!IMPORTANT]
> **Issue #2 の残る操作確認は、GitHub 連携経路と手動 Refresh を使う回避手順で確認したものです。** 新版から全章を通し直した結果や、App 本体の不具合修復を意味するものではありません。画像の差し替え記録と未実施経路は [UI 確認表](ui-check.md) と本表を参照してください。以下の実走記録は段階ごとの履歴であり、各段階の「未確認」「未作成」は当時の状態です。

## 1. 検証環境とベースラインの確認

- **検証実施日**：2026年9月13日
- **OS 環境**：Windows 11（ビルド 26200.9445、25H2）
- **ツール**：GitHub Copilot App 1.1.20（インストーラー署名：GitHub, Inc. 有効）、Node.js 24.19.0
- **アカウント**：`iwizsophy`
- **教材の開始コミット**：`cfcbad744d8349a2a7b200484470c7d439bf3cb7`
- **演習用コピー**：非公開リポジトリ `iwizsophy/dev-days-tailspin-app-verification-20260913`（`github-samples/tailspin-toys` の固定コミット `bae003609c8cff0c51d92658b8d3bd89450464f1` から作成）

### ベースラインの修正
演習用コピーの `feature/workshop-baseline`（コミット `641f557`）において、`.github/agents/pr-readiness.md` 内の無効な YAML エスケープ `"playwright/\*"` を `"playwright/*"` に修正し、同名リモートブランチへ push しました（星評価やフィルターの実装は含みません）。

### 外部シェルでの初期状態検査
App 外の PowerShell から Node 24.19.0 を明示指定して検査を実施しました。`npm ci`、単体テスト27件、Chromium E2E 21件、lint、型検査がすべて成功することを確認しています。E2E はポート4321に既存サーバーがないことを確認した上で、ビルドおよび preview を起動しました（通常の Node 24.14.1 では一部依存の要求バージョンを満たさないため、検査時のみ Node 24.19.0 のパスを使用しました。これは App のセットアップスクリプトや開発サーバーの実走結果ではありません）。

## 2. 章別の検証結果一覧（合流条件・App 実走・CLI 緊急対応）

| 演習 | 合流時の確認対象 | App 実走の確認結果 | 講師の CLI 緊急対応検証 |
| :--- | :--- | :--- | :--- |
| **0 準備** | 自分のコピー、Node、起動とテスト | 固定コミットからのコピー作成、外部シェルでのテスト成功。GitHub Web で Private コピー作成・課題8件の自動作成を確認。Add GitHub repository で設定承認・初回応答後の依存導入・App ビルド24ページ成功。セットアップ単独の終了コードは未取得 | 未検証 |
| **1 接続** | 同じ checkout を開き、構成について応答 | 一部確認：初期設定、Chats 応答、Open folder、設定レビュー、完全再起動後の演習 repo 読み取りと構成への応答。GitHub 連携プロジェクトを追加し、My work の8件の Issue 表示を確認 | 未検証 |
| **2 星評価** | 数値と null の表示、テスト、PR・マージ | App で実装・レビュー修正・検査・Run 起動停止を確認。gh 経由で PR #9 作成、CI 全4ジョブ成功。App 固有の PR 作成は失敗。My work から通常マージ成功、次章 worktree への星評価継承を確認 | 未検証 |
| **3 指示** | TSDoc・ヘッダーの標準と提示コード、PR・マージ | Issue #8 → New session で専用 worktree を作成。HEAD が星評価マージ済みの `9107d35` と一致し差分なし。設定承認後に7ファイル更新、単体30件・E2E 21件・lint・型検査成功。指示に沿うコード例と App の Create PR による PR #10 作成・通常マージを確認。フィルター用 worktree が `1b698ac` を継承 | 未検証 |
| **4 フィルター** | 星評価・指示を継承し、絞り込みと quality-checks | Issue #7 の専用 worktree が `1b698ac` を継承。Plan の質問へ回答し、計画承認で Autopilot に切替。実装・修正後に単体35件・E2E 25件・lint・型検査・build 成功。通常21件での Run 起動・絞り込み・停止を確認。MCP 検証も成功し、PR #12 を Agent Merge で統合 | 未検証 |
| **5 MCP** | MCP ツールの実行、複合条件・解除等の検証 | リポジトリ定義 `.mcp.json` の信頼承認・設定形式修正・`/restart-session` 後に MCP 実行成功。通常データの複合条件・解除・出版社単独・キーボードを確認。追加実走では一時隔離 DB のフィルター0件も確認。カタログ保存後に Installed 1 を確認し、新規 Chats で `browser_tabs` が成功 | 未検証 |
| **6 マージ** | CI とレビュー、演習コピーへ統合 | Agent merge から PR #12 作成、Merge pull request を有効化。CI 全4ジョブ成功後の自動マージを確認 | 未検証（通常マージのみ代替可能） |
| **7 Canvas** | 共有・保存・Issue 操作 | 新規 worktree が `5c4c3ac` を継承。6カード・全6ボタン・上位3件の理由、Refresh、共有保存と PR #13 の自動マージ、別セッションでの再表示に成功。反復送信修正 PR #14 を統合し、1通知・1応答と再追加抑止を確認。追加実走で検索 Issue の計画・実装・MCP・PR #15 の自動マージまで確認。開き直し・Refresh 後は未完了5件で GitHub と一致 | 機能代替不可。優先順位整理は未検証 |
| **8 Automation** | 手動実行、結果、終了状態 | Manual・Local で Create and run を実行し、37秒で Succeeded。PR 6件・Issue 6件の要約を GitHub と照合。定期実行なし | 機能代替不可。単発要約は未検証 |

## 3. 初期接続と各演習の実走詳細

### 初回接続と Open folder の観察（演習1）
- `Open folder` 後に `New session` と `Work directly in this folder for this session` が表示されました。
- 続いて `Accept this repository configuration?` → `Review configuration` で `.github/github-app.yml` を表示しました（セッション作成時の `npm ci`、Run メニュー、プレビュー自動表示を含む）。
- 利用者が `Accept and apply` を操作しても確認画面が残り続け、プロンプト入力欄が表示されない現象を確認しました。
- ウィンドウを通常終了しても同一画面が残り、プロセスが継続していました。タスクマネージャー等で App プロセスを強制終了して起動し直すと、停止していた空セッションが消去され、プロジェクトの新規セッションから送信可能になりました（強制終了には未保存状態の喪失リスクがあります。今回の復帰事例であり、警告ログ `pending-request event was not delivered to the session host` などの原因や恒久対策は未確定です）。
- 再起動後のセッションでは、対象 checkout の各ファイル読み取り、日本語での構成説明、応答後の Idle 復帰を確認しました。差分はなく、`git worktree list` も元の `feature/workshop-baseline` のみであり、この経路では worktree は分離されていません。

### 演習2：星評価の実装と PR #9
- 作業ブランチ `feature/app-star-rating` でセッションを開始しました。
- 実装レビューにおいて、エージェントが提示したヘルパー単体のテストを差し戻し、`GameCard` の実レンダリングテスト（4.2、0、null）および一覧 E2E の評価表示確認へ修正しました。
- PR Readiness で指摘された評価の意味と尺度の不足に対し、カードの読み上げ名 `Rating: X out of 5 stars` と装飾部分への `aria-hidden="true"` を追加しました（コミット `9c3d619`、`0901fc7`。Author/Committer: Tetsuji Kato）。
- 単体30件、E2E 21件、lint、型検査、build が成功しました。Run development site で起動し、App 内ブラウザーと外部ブラウザーで表示を確認後、Stop で停止しました（ポート4321の解放を確認）。
- **PR 作成とマージ**：App のプロジェクト連携 PR ツールは GitHub アカウントエラーで失敗したため、エージェントが認証済み `gh` CLI で [検証用 PR #9](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/9) を作成しました（App 固有ツールの成功とは数えません）。その後、GitHub 連携側の My work から PR #9 を開き、Changes（5ファイル差分）、All checks have passed、No unresolved comments を確認し、Merge pull request（Merge commit）を実行しました。マージコミット `9107d35` を確認しています（通常マージであり Agent Merge ではありません）。CI（[実行ログ](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34750878686)）全4ジョブの成功を確認しました。

### 演習3：指示更新と PR #10
- Issue #8 から New session を開始しました。`~/.copilot/repos/copilot-worktrees/` 配下に `iwizsophy-issue-8-update-our-repository-coding-standards-05839e` という専用 worktree とブランチが自動生成されました。HEAD は `9107d35` を継承しています。
- 設定承認後にプロンプト入力欄が表示されました（再起動不要）。最初の lint は依存未導入で失敗したため、エージェントが worktree 内で `npm ci` を実行しました。
- `.github/copilot-instructions.md`、Astro・Drizzle・UI の指示3ファイル、README、eslint.config.js、Layout.astro の計7ファイルを更新しました。単体30件、E2E 21件、lint、型検査（診断ゼロ）が成功しました。
- Publisher 関数例に TSDoc とヘッダーが含まれることを確認しましたが、これはプロンプトで要件を明示して依頼した結果であり、新規セッションで自動反映されることの証明ではありません。
- App の Open changes（Changes (7), +43, -4）から上部の `Create PR` を実行しました。App がコミット・push・PR 作成まで完了し、[検証用 PR #10](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/10)（ブランチ：`iwizsophy-repository-coding-standards`、コミット `97da644`、Author/Committer: Tetsuji Kato）を作成しました。
- PR #10 の CI（[実行ログ](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34751902435)）全4ジョブ成功後、App の Ready to merge → Merge pull request で通常マージしました（マージコミット `1b698ac`）。

### 演習4：フィルター計画・自律実装
- Issue #7 から New session を開始しました。専用 worktree `iwizsophy-issue-7-allow-users-to-filter-games-by-category-91fbc5`（ブランチ：`iwizsophy-filter-games-by-category-and-publisher`、HEAD：`1b698ac`）を作成しました。
- Mode で Plan を選択し、カテゴリ間 OR・出版社間 AND の仕様質問に回答後、計画を承認して Mode: Autopilot へ移行し実装しました。
- レビューにて、出版社のラベル不整合、複数カテゴリを実際には選ばないテスト、存在しない選択肢を DOM に注入する0件テストを修正しました。通常 CSV（21件）は全組み合わせを含むため、0件条件には20件の E2E 専用 CSV と分離 SQLite を使用して検証しました（本番 CSV は未変更）。
- 単体35件、E2E 25件、lint、型検査、build、`diff --check` が成功しました。Run development site で起動し、21件 → Strategy 4件 → Puzzle 追加8件 → CodeForge Studios 追加2件 → Clear filters 21件を確認して停止しました。

### 演習5：MCP 設定修正とテスト実行
- GitHub 連携プロジェクトの Settings → MCP servers で本人の信頼承認（Trust）を実施しました。
- 既存の `.mcp.json` ではルートキーが `servers` となっていたため `No MCP servers loaded` となりました。ルートキーを `mcpServers` へ修正し、Refresh 後に3サーバー（GitHub、Playwright、astro-docs）の Connected 表示を確認しました（外部シェルで修正し、[検証用 PR #11](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/11) としてマージ `9a444be`。フィルター worktree にも反映 `7644b85`）。
- 既存セッションで MCP 実行を依頼したところ、ツール一覧にブラウザーツールが存在しないと報告して停止しました（Connected は実行可能を保証しません）。セッション内で `/restart-session` を送信して再起動後、Playwright MCP ツール群（`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_select_option`, `browser_press_key`, `browser_close`）の呼び出しに成功しました。
- 通常データでの複合条件、出版社単独6件、Tab/Enter 解除を確認しました。

### 演習6：Agent Merge による PR #12 自動マージ
- Create PR options → Agent merge を選択して実行しました。App がコミット `40ca912` を作成し push して [検証用 PR #12](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/12) を作成しました。
- Agent merge options のうち、Address reviews、Fix CI failures、Resolve conflicts は初期状態で有効、`Merge pull request` は初期状態で無効だったため、手動で有効化しました。
- CI 全4ジョブ（[実行ログ](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34753452098)）成功後、自動マージを確認しました（マージコミット `5c4c3ac`）。CI 失敗や競合の自動修正は発生しなかったため未検証です。

### 演習7：Canvas 作成と反復送信バグの解消
- New worktree/main で worktree `iwizsophy-symmetrical-pancake`（HEAD：`5c4c3ac`）を作成しました。全6カード・全6ボタン・上位3件の理由・Refresh を備えた Issue triage board（`.github/extensions/issue-triage-board/extension.mjs`）を共有保存しました。[PR #13](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/13)（コミット `98e48fa`）が Agent Merge で自動マージされました（マージコミット `b15fd07`）。
- 新規セッション（worktree `iwizsophy-ideal-meme`）でキャンバスを開き `Add to current session` を押した際、命令形通知を受けたエージェントが `add_issue_context` を再呼び出して通知が無限反復するバグが発生しました（Stop and discard で停止）。
- 通知の事実化、重複防止、再入循環待ち防止を実装し、回帰テスト3件（`test:extensions`）を追加しました。[PR #14](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/14)（コミット `68af6d7`）が Agent Merge で自動マージされました（マージコミット `c6e8652`）。ボタン再テストで 1通知・1応答、Refresh 後の再クリックでの重複抑止を確認しました。

### 演習8：Automation 手動実行
- Automations 画面から `Trigger: Manual`、`Run in the cloud: Off`、検証プロジェクトを選択し、`Tailspin App verification recap 20260913` を作成して Create and run を実行しました。
- Recent runs は Local・37秒・Succeeded でした。基準日時 2026-09-13 20:33:02 JST 時点のマージ済み PR 6件（#9〜#14）および Open Issue 6件（#1〜#6）の要約結果が GitHub 一覧と完全に一致しました。定期実行やクラウド実行は未検証です。

## 4. 追加実走：キャンバスからの検索機能実装完走

2026年9月13日、修正済みキャンバスの実効性を証明するため、追加実走を行いました。

- GitHub 連携プロジェクトの New worktree/main から worktree `iwizsophy-studious-journey`（ブランチ：`iwizsophy-training-validation`、開始 HEAD：`c6e8652`）を作成しました。最初の応答時に依存導入済みを確認しました（エージェント自身は導入コマンド未実行。自動セットアップの終了ログは未取得です）。
- 保存済み Issue triage board を開き、Issue #1 の `Add to current session` を1回選択しました。1通知・確認応答を確認後、Mode: Plan でタイトル検索機能の計画を作成・承認し、Autopilot で実装しました。
- レビューにて SQL `LIKE` とブラウザー `includes` の特殊文字解釈の差異を指摘し、`ESCAPE '!'` と特殊文字（`%`, `_`, `!`, `\`）の回帰テストを追加しました。
- 最終検査で Vitest 39件、拡張回帰3件、Playwright E2E 28件、lint、型検査、build が成功しました。実際の Playwright MCP は9種類・31回の呼び出しを記録しました。通常データでの検索、大文字小文字無視、複数条件絞り込み、および一時隔離 DB による0件表示を確認しました。
- App の Agent merge により [検証用 PR #15](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/15)（コミット `eaa8243`）を作成し、CI 全4ジョブ（[実行ログ](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34756052959)）成功後に自動マージされました（マージコミット `6cab45d`）。Issue #1 は Closed となり、作業ツリーはクリーンです。
- 開き直し・手動 Refresh 後にキャンバスの未完了件数が5件（#2〜#6）となり、GitHub の実データと一致することを確認しました。

## 5. テンプレートの修正とセキュリティ監査記録

演習用コピーの元となる非公開リポジトリ [iwizsophy/dev-days-tailspin-template](https://github.com/iwizsophy/dev-days-tailspin-template) を作成し、原本（`github-samples/tailspin-toys`、コミット `bae0036`）から必要な修正のみを適用しています（参照元への変更送信は行っていません）。

### 配布版 v2026.09.13 の監査記録
- PR Readiness の YAML エスケープ修正、MCP の `mcpServers` ルートキー修正、Node 24.19.0 指定を適用しました。
- 初期版での `npm audit` 詳細結果は **40件（Critical 1・High 24・Moderate 14・Low 1）**（Astro の AVIF 最適化に関する GHSA-26w7-cxv4-gfx2 等）でした。機能テスト成功を安全性の判定とはみなさず、本番配布前の依存更新課題として記録しています。

### 現在の教材対応版（v2026.09.13.1）
現在の教材対応版は **v2026.09.13.1**（コミット `aea4c027a073dd757017829bd988857877c1a545`）です。

1. **Astro 7.3 のプロセス管理問題と起動スクリプト刷新**：
   Astro 7.3 の CLI がエージェント環境でサーバーを自動的にバックグラウンド起動し、Playwright の起動監視を失敗させる問題を確認しました。dev / preview を公開 API 経由で起動する `scripts/serve.mjs` を導入し、プロセス管理を確実にしました。
2. **監査結果の改善と残存課題**：
   Vitest 4.1.11 への更新や互換範囲内の間接依存更新により、`npm audit` は **Critical 0・High 0・Moderate 4・Low 0** に低減しました。残る Moderate 4件は `drizzle-kit` 配下の `esbuild` 関連の同一経路です。自動修正案は drizzle-kit の互換性を損なうダウングレードとなるため適用していません（通常の migrate/seed は tsx 経由ですが、到達可能性の網羅的評価は未実施であり、配布前の確認事項として残します）。
3. **ネイティブ App Run / Stop の再確認**：
   ローカル checkout を Open folder で開き、WORKSHOP.md の版名読み取りセッション後に Run options → Run development site で起動しました（実プロセス：`node scripts/serve.mjs dev`、HTTP 200 応答）。App の Stop でプロセスが終了しポート4321が解放されることを2回確認しました。

## 6. 実走記録の再利用境界と記録項目

### CLI 独立コースの実績を再利用できる範囲
2026年9月8日の Tailspin Toys **CLI 独立シナリオ**（Copilot CLI 1.0.83）の実走結果（[フィルター PR #11](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/11)、[高コントラスト PR #13](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/13)）は、環境構築やトラブルシューティングの参考にはなります。しかし、**星評価の実装、App の章間マージ、Agent Merge、Canvas、Automation の証拠ではありません**。

### 1回の実走で記録すべき必須項目

| 項目 | 記入内容 |
| :--- | :--- |
| **実施日・担当** | 検証日時、検証者アカウント |
| **教材・テンプレート** | 教材リポジトリおよびテンプレート双方のコミット SHA |
| **実行環境** | OS ビルド、Node.js、App、CLI のバージョン |
| **検証対象** | 演習用リポジトリ名、ブランチ名、worktree パス、Issue 番号 |
| **実施経路** | App／CLI／手動／講師デモ、切り替えが発生した地点 |
| **実行結果** | 期待値と実測値、実行したテスト名・件数・終了コード |
| **客観的証拠** | PR URL、CI 実行ログ URL、画面キャプチャ画像 |
| **未確認・終了状態** | 未実施の App 固有機能、残存する制約、サーバー・Codespace の停止確認 |

[講師ガイド](instructor.md) · [演習目次](../app/README.md)
