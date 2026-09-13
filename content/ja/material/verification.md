# App シナリオの検証状況

2026年9月13日：Windows の GitHub Copilot App 1.1.20 をインストールし、利用者によるサインイン後の初期設定、プロジェクト追加メニュー、Chats の応答と右クリックメニュー、MCP 登録フォームまで確認しました。演習用コピーを `Projects` → `+` → `Open folder` で追加し、リポジトリ設定のレビューと、完全再起動後の演習 repo の読み取り・日本語応答まで確認しました。星評価は App で実装と検査を確認しました。検証用 PR は App エージェントの `gh` 経由で作成し、CI 全4ジョブが成功しました。その後、My work から通常マージが成功しました。指示更新の演習では GitHub 連携セッションの Create PR から PR #10 を作成できました。**Agent Merge・全章完走は未完了です。** 詳細は [UI 確認表](ui-check.md)を参照してください。

環境：Windows ビルド 26200.9445（25H2）、App 実行ファイルの ProductVersion 1.1.20、確認アカウント iwizsophy。教材の開始コミットは `cfcbad744d8349a2a7b200484470c7d439bf3cb7`。インストーラーの署名は GitHub, Inc. で有効でした。

演習用コピーは非公開の `iwizsophy/dev-days-tailspin-app-verification-20260913`。`github-samples/tailspin-toys` の固定コミット `bae003609c8cff0c51d92658b8d3bd89450464f1` から作成しました。`feature/workshop-baseline` の `641f557` では `.github/agents/pr-readiness.md` の無効な YAML エスケープ `"playwright/\*"` を `"playwright/*"` に修正しています。この修正は同名のリモートブランチへ push 済みで、星評価やフィルターの実装は含みません。

開始状態を App 外の PowerShell で検査し、Node 24.19.0 で `npm ci`、単体テスト27件、Chromium E2E 21件、lint、型検査が成功しました。E2E はポート4321に既存サーバーがないことを確認してからビルド・previewを起動しました。これは App のセットアップスクリプトや開発サーバーの実走結果ではありません。通常の Node 24.14.1 では一部依存の要求バージョンを満たさず、検査時のみ Node 24.19.0 のパスを指定しました。

`Open folder` 後に `New session` と `Work directly in this folder for this session` が表示されました。続いて `Accept this repository configuration?` → `Review configuration` で `.github/github-app.yml` を表示しました。設定にはセッション作成時の `npm ci`、開発・ビルド・型検査の Run メニュー、プレビューの自動表示が含まれます。利用者が `Accept and apply` を操作しても確認画面が残り、入力欄が表示されないことを確認しました。完全再起動後は確認画面が再表示されず、設定にある Run メニューとメッセージ入力欄が表示されました。セットアップスクリプトの実行成功は未確認です。

接続直後のローカルログには `pending-request event was not delivered to the session host` と `no session host is registered` の警告がありました。確認画面の停止との因果関係は調査中です。ウィンドウを通常終了して開き直しても同じ確認画面が残り、App 本体のプロセスは起動時から継続していました。利用者の承認後に App 本体を強制終了して起動し直すと、停止していた空のセッションは消え、プロジェクトの新規セッションから送信できました。強制終了には未保存の状態を失う可能性があります。今回の復帰事例であり、警告の原因や恒久対策は確定していません。

再起動後の `Tailspin toys repository` セッションでは、対象 checkout の `src/pages/index.astro`、`src/lib/games.ts`、`GameCard.astro`、テスト等の読み取りと、日本語の構成説明、応答後の Idle を確認しました。検証用 checkout の差分はなく、`git worktree list` は元の `feature/workshop-baseline` のみでした。この経路で worktree が分離されたとは扱いません。チャットは説明のみを依頼し、応答後の Idle を確認しました。MCP はフォームの表示までで、保存していません。星評価の実装セッションは `feature/app-star-rating` で実行しました。レビューでヘルパーだけのテストを差し戻し、GameCard の実レンダリング（4.2・0・null）と一覧E2Eの評価表示確認へ修正しました。App から実行した単体30件・E2E21件・lint・型検査・buildが成功しました。App の Run development site で起動し、App 内 Browser と別ブラウザーで星評価を確認後、Stop Run development site で停止しました。ポート4321の待受終了も確認しました。定期実行は未作成です。UI の表示確認を機能の実走成功と混同しません。

星評価は `9c3d619`、読み上げ対応は `0901fc7` にコミットし、演習コピーの `origin/feature/app-star-rating` へ push 済みです。Author・Committer はともに `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`。PR Readiness で指摘された評価の意味と尺度の不足を、カードの `Rating: X out of 5 stars` という読み上げ名と装飾部分の `aria-hidden` で修正し、実レンダリング・E2E のアサーションを追加しました。

[検証用 PR #9](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/9)（非公開・閲覧権限が必要）は main 宛てで、利用者承認後に App からマージしました。App のプロジェクト連携 PR ツールは GitHub アカウントを利用できないというエラーで失敗したため、App エージェントが認証済みの `gh` CLI で作成しました。これは App 固有の Create PR 操作の成功とは数えません。その後、GitHub 連携側の My work で PR #9 を開き、Changes の5ファイルの差分、Ready to merge、マージ確認画面の All checks have passed と No unresolved comments を確認しました。利用者の承認後、同じ確認画面の Merge pull request（Merge commit）を実行し、GitHub 上の MERGED とマージコミット `9107d35c8539bb0327ec21d6b1e86f42b33a4392` を確認しました。これは通常マージであり Agent Merge の検証ではありません。Issue #8 の詳細と New session options（New session・New session in repository...・Chat）も表示確認しました。

最終コミット `0901fc759c50ecccbc75a0ac74c178fdc46c89c7` の [CI](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34750878686) は frontend-lint・type-check・unit-tests・frontend-tests の全4ジョブが成功しました。検証用 checkout はクリーンで、ポート4321・4322の待受も終了しています。

教材側の初期検査：41ページ・内部リンク／画像／アンカー773参照が成功。2回の生成結果が一致し、旧画像の未照合注記と新規実機画像2枚の確認日・バージョン注記が区別されることを確認しました。

2026年9月10日：教材の再構成・HTML 生成・内部参照を確認。この時点では App の実機操作や新しいアプリ実装を実施していませんでした。

前回の再構成時の確認（今回の修正前）：サイト39ページ・内部リンク／画像／アンカー755参照が成功。2回の生成結果が一致し、当時の App 全9章に CLI 代替手順と合流条件があることを確認しました。ブラウザーで参加者の入口、演習0への移動、章内の CLI 手順への移動と表示を確認しています。

| 演習 | 合流時の確認対象 | App 実走 | 講師の CLI 緊急対応検証 |
| --- | --- | --- | --- |
| 0 準備 | 自分のコピー、Node、起動とテスト | コピー作成・外部シェルで開始状態のテスト成功。後続の星評価セッションで App の Run 起動・停止を確認（初回セットアップは未確認） | 未検証 |
| 1 接続 | 同じ checkout を開き、構成について応答 | 一部確認：初期設定・Chats 応答・Open folder・設定レビュー・完全再起動後の演習 repo の読み取りと構成への応答。GitHub 連携プロジェクトを追加し、My work の8件の Issue 表示を確認 | 未検証 |
| 2 星評価 | 数値と null の表示、テスト、PR・マージ | App で実装・レビュー修正・検査・Run 起動停止を確認。gh 経由で PR #9 作成、CI 全4ジョブ成功。App 固有の PR 作成は失敗。My work から通常マージ成功、次章 worktree への星評価継承を確認 | 未検証 |
| 3 指示 | TSDoc・ヘッダーの標準と提示コード、PR・マージ | Issue #8 → New session で専用 worktree を作成。HEAD が星評価マージ済みの 9107d35 と一致し、差分なし。設定承認後に7ファイル更新、単体30件・E2E21件・lint・型検査成功。指示に沿うコード例と App の Create PR による PR #10 作成・通常マージを確認。フィルター用 worktree が 1b698ac を継承 | 未検証 |
| 4 フィルター | 星評価・指示を継承し、絞り込みと quality-checks | Issue #7 の専用 worktree が 1b698ac を継承。Plan の質問へ回答、計画承認で Autopilot に切替。実装・修正後に単体35件・E2E25件・lint・型検査・build 成功。通常21件での Run 起動・絞り込み・停止を確認。MCP 検証前で未コミット | 未検証 |
| 5 MCP | MCP ツールの実行、複合条件・解除等の検証 | 一部確認：カタログ・登録フォーム・リポジトリ定義 .mcp.json。本人が信頼承認後、設定形式の修正により3サーバーが Connected。既存セッションには Playwright ツールが公開されず停止。ツール実行は未実施 | 未検証 |
| 6 マージ | CI とレビュー、演習コピーへ統合 | 未検証 | 未検証（通常マージのみ代替可能） |
| 7 Canvas | 共有・保存・Issue 操作 | 未検証 | 機能代替不可。優先順位整理は未検証 |
| 8 Automation | 手動実行、結果、終了状態 | 未検証 | 機能代替不可。単発要約は未検証 |

Issue #8 の New session では、`~/.copilot/repos/copilot-worktrees/` 以下に `iwizsophy-issue-8-update-our-repository-coding-standards-05839e` という専用 worktree とブランチが作成されました。App が自動生成したブランチ名です。HEAD は `9107d35` で、StarRating の再利用・null の表示・読み上げ名を継承しています。新規プロジェクトでは再度 Accept this repository configuration? が表示され、Review configuration で npm ci のセットアップ、Run メニュー3項目、Browser の自動表示設定を確認しました。利用者が設定を承認すると入力欄が表示され、今回は再起動なしで送信できました。セットアップ成功の証拠はなく、最初の lint は依存未導入で失敗したため、App エージェントがこの worktree に npm ci を実行しました。

指示更新は `.github/copilot-instructions.md`、Astro・Drizzle・UI の指示3ファイル、README、eslint.config.js、Layout.astro の7ファイルです。意図を説明するコメント、exported function の TSDoc、注入可能な db、Astro Props の契約を記載しました。ESLint の single quotes・semicolons に合わせた既存コード修正は Layout.astro の3行のみ。単体30件、E2E21件、lint、型検査（診断ゼロ）が成功し、ポート4321のサーバー停止も確認しました。表示のみの Publisher 関数例にはファイルヘッダー、TSDoc、db の注入説明が含まれ、ファイルは追加されていません。例の要件を明示して依頼した結果であり、新規セッションで自動的に指示が反映されることの証明ではありません。

App の Open changes で Changes (7), +43, -4 を確認後、上部の Create PR を操作しました。App がコミット・同名ブランチへの push・PR 作成まで実行し、[検証用 PR #10](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/10) を作成しました。ブランチ名は App が変更した `iwizsophy-repository-coding-standards`、コミットは `97da644d628d0e5b0aaa1c893912a45a2f68b0fc`。Author・Committer は指定の Tetsuji Kato で、checkout はクリーンです。これは GitHub 連携プロジェクトの専用 worktree 経路での成功であり、ローカルフォルダー側の連携エラーが修復されたことは意味しません。Ready to merge options に Agent merge の切り替えを表示しましたが、有効化していません。PR #10 の [CI](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34751902435) は全4ジョブ成功しました。利用者による以後の検証用リポジトリ操作の承認後、App の Ready to merge → Merge pull request で PR #10 を通常マージしました。マージコミットは `1b698acc404d35ddf48b0b9df539e1257ff88fec` です。

フィルター演習は Issue #7 → New session で、`iwizsophy-issue-7-allow-users-to-filter-games-by-category-91fbc5` という専用 worktree を作成しました。App がブランチ名を `iwizsophy-filter-games-by-category-and-publisher` に変更しています。HEAD は `1b698ac`。今回は設定承認を再表示せず開始できました。Mode メニューで Plan を選択し、カテゴリ内は OR・出版社とは AND の質問に回答。Review plan → Approve and implement this plan → Continue で Mode: Autopilot に切り替わりました。

フィルターのレビューでは、出版社のラベル不整合、複数カテゴリを実際には選ばないテスト、存在しない選択肢を DOM に注入する0件テストを修正しました。通常 CSV は全5カテゴリ×4出版社を含むため、0件条件には20件の E2E 専用 CSV と分離 SQLite を使います。本番21件の CSV は変更していません。最終検査は単体35件・E2E25件・lint・型検査・build・diff --check が成功。App の Run development site で通常データを起動し、別ブラウザーで21件 → Strategy 4件 → Puzzle 追加8件 → CodeForge Studios 追加2件 → Clear filters 21件を確認しました。App の Stop で停止し、4321 の待受終了も確認しました。このブラウザー確認は Playwright MCP の実行証拠ではありません。新しいデータアクセス関数の TSDoc は確認できましたが、ファイルヘッダーが自動追加されたとは扱いません。フィルター変更は未コミットで、PR は未作成です。

MCP の確認では、GitHub 連携プロジェクトを右クリック → Settings → MCP servers に Trust this repository / Trust repository が表示されました。Repository configuration の Trusted 表示とは別の確認です。コピーに既存の `.mcp.json` は GitHub（https://api.githubcopilot.com/mcp/）、Playwright（npx @playwright/mcp@latest）、astro-docs（https://mcp.docs.astro.build/mcp）を定義しています。本人の信頼承認後、No MCP servers loaded を確認しました。設定のルートを servers から mcpServers に変更し、接続先を維持したまま Refresh 後に3サーバーの Connected 表示を確認しました。修正は外部シェルで実施し、[検証用 PR #11](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/11) は CI 全4ジョブ成功後にマージ（9a444be）。フィルター worktree にも同じ修正を7644b85として反映しています。既存フィルターセッションに MCP 実走を依頼すると、Playwright の browser 操作ツールが利用可能一覧に存在しないと報告して停止しました。Connected はセッション内の実行証拠ではありません。セッションの再読み込み方法は未確認で、MCP によるブラウザー検証も未実施です。フィルター変更は未コミットのまま保持しています。

すべての章で App → CLI → App の作業ディレクトリ・ブランチ・差分の一致も未検証です。

## 既存の実走結果を再利用できる範囲

2026年9月8日の Tailspin Toys **CLI 独立シナリオ**では、Copilot CLI 1.0.83 の応答、指示反映、フィルター実装、quality-checks、Playwright MCP、高コントラストのカスタムエージェント、PR と CI を確認しました。環境構築と問題切り分けの参考になります。

- [フィルター PR #11](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/11)：CI 全4ジョブ成功。
- [高コントラスト PR #13](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/13)：CI 全4ジョブ成功。

証拠は非公開コピーのため閲覧権限が必要です。詳細はこのリポジトリの `content/ja/verification-2026-09-08.md`。星評価の実装、App の章間マージ、Agent Merge、Canvas、Automation の証拠ではありません。

## 1回の実走で記録する項目

| 項目 | 記入内容 |
| --- | --- |
| 実施日・担当 | 日時、検証者 |
| 教材・テンプレート | 両方のコミット SHA |
| 環境 | OS、Node、App、CLI のバージョン |
| 対象 | 自分の演習 repo、branch、worktree、Issue |
| 経路 | App／CLI／手動／講師デモ、切り替え地点 |
| 結果 | 期待値・実測値、テスト名・件数・終了コード |
| 証拠 | 自分の PR・CI URL、スクリーンショット等 |
| 未確認・終了状態 | App 固有機能、制約、サーバー・Codespace 停止 |

[講師ガイド](instructor.md) · [演習目次](../app/README.md)
