# App シナリオの検証状況

2026年9月13日：Windows の GitHub Copilot App 1.1.20 をインストールし、利用者によるサインイン後の初期設定、プロジェクト追加メニュー、Chats の応答と右クリックメニュー、MCP 登録フォームまで確認しました。演習用コピーを `Projects` → `+` → `Open folder` で追加し、リポジトリ設定のレビューと、完全再起動後の演習 repo の読み取り・日本語応答まで確認しました。星評価は App で実装と検査を確認しました。検証用 PR は App エージェントの `gh` 経由で作成し、CI 全4ジョブが成功しました。**App 固有の PR 作成経路・マージ・全章完走は未完了です。** 詳細は [UI 確認表](ui-check.md)を参照してください。

環境：Windows ビルド 26200.9445（25H2）、App 実行ファイルの ProductVersion 1.1.20、確認アカウント iwizsophy。教材の開始コミットは `cfcbad744d8349a2a7b200484470c7d439bf3cb7`。インストーラーの署名は GitHub, Inc. で有効でした。

演習用コピーは非公開の `iwizsophy/dev-days-tailspin-app-verification-20260913`。`github-samples/tailspin-toys` の固定コミット `bae003609c8cff0c51d92658b8d3bd89450464f1` から作成しました。`feature/workshop-baseline` の `641f557` では `.github/agents/pr-readiness.md` の無効な YAML エスケープ `"playwright/\*"` を `"playwright/*"` に修正しています。この修正は同名のリモートブランチへ push 済みで、星評価やフィルターの実装は含みません。

開始状態を App 外の PowerShell で検査し、Node 24.19.0 で `npm ci`、単体テスト27件、Chromium E2E 21件、lint、型検査が成功しました。E2E はポート4321に既存サーバーがないことを確認してからビルド・previewを起動しました。これは App のセットアップスクリプトや開発サーバーの実走結果ではありません。通常の Node 24.14.1 では一部依存の要求バージョンを満たさず、検査時のみ Node 24.19.0 のパスを指定しました。

`Open folder` 後に `New session` と `Work directly in this folder for this session` が表示されました。続いて `Accept this repository configuration?` → `Review configuration` で `.github/github-app.yml` を表示しました。設定にはセッション作成時の `npm ci`、開発・ビルド・型検査の Run メニュー、プレビューの自動表示が含まれます。利用者が `Accept and apply` を操作しても確認画面が残り、入力欄が表示されないことを確認しました。完全再起動後は確認画面が再表示されず、設定にある Run メニューとメッセージ入力欄が表示されました。セットアップスクリプトの実行成功は未確認です。

接続直後のローカルログには `pending-request event was not delivered to the session host` と `no session host is registered` の警告がありました。確認画面の停止との因果関係は調査中です。ウィンドウを通常終了して開き直しても同じ確認画面が残り、App 本体のプロセスは起動時から継続していました。利用者の承認後に App 本体を強制終了して起動し直すと、停止していた空のセッションは消え、プロジェクトの新規セッションから送信できました。強制終了には未保存の状態を失う可能性があります。今回の復帰事例であり、警告の原因や恒久対策は確定していません。

再起動後の `Tailspin toys repository` セッションでは、対象 checkout の `src/pages/index.astro`、`src/lib/games.ts`、`GameCard.astro`、テスト等の読み取りと、日本語の構成説明、応答後の Idle を確認しました。検証用 checkout の差分はなく、`git worktree list` は元の `feature/workshop-baseline` のみでした。この経路で worktree が分離されたとは扱いません。チャットは説明のみを依頼し、応答後の Idle を確認しました。MCP はフォームの表示までで、保存していません。星評価の実装セッションは `feature/app-star-rating` で実行しました。レビューでヘルパーだけのテストを差し戻し、GameCard の実レンダリング（4.2・0・null）と一覧E2Eの評価表示確認へ修正しました。App から実行した単体30件・E2E21件・lint・型検査・buildが成功しました。App の Run development site で起動し、App 内 Browser と別ブラウザーで星評価を確認後、Stop Run development site で停止しました。ポート4321の待受終了も確認しました。定期実行は未作成です。UI の表示確認を機能の実走成功と混同しません。

星評価は `9c3d619`、読み上げ対応は `0901fc7` にコミットし、演習コピーの `origin/feature/app-star-rating` へ push 済みです。Author・Committer はともに `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`。PR Readiness で指摘された評価の意味と尺度の不足を、カードの `Rating: X out of 5 stars` という読み上げ名と装飾部分の `aria-hidden` で修正し、実レンダリング・E2E のアサーションを追加しました。

[検証用 PR #9](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/pull/9)（非公開・閲覧権限が必要）は main 宛てで未マージです。App のプロジェクト連携 PR ツールは GitHub アカウントを利用できないというエラーで失敗したため、App エージェントが認証済みの `gh` CLI で作成しました。これは App 固有の Create PR 操作の成功とは数えません。その後、GitHub 連携側の My work で PR #9 を開き、Changes の5ファイルの差分、Ready to merge、マージ確認画面の All checks have passed と No unresolved comments を確認しました。確認画面は閉じ、マージはまだ実行していません。Issue #8 の詳細と New session options（New session・New session in repository...・Chat）も表示確認しました。

最終コミット `0901fc759c50ecccbc75a0ac74c178fdc46c89c7` の [CI](https://github.com/iwizsophy/dev-days-tailspin-app-verification-20260913/actions/runs/34750878686) は frontend-lint・type-check・unit-tests・frontend-tests の全4ジョブが成功しました。検証用 checkout はクリーンで、ポート4321・4322の待受も終了しています。

教材側の初期検査：41ページ・内部リンク／画像／アンカー773参照が成功。2回の生成結果が一致し、旧画像の未照合注記と新規実機画像2枚の確認日・バージョン注記が区別されることを確認しました。

2026年9月10日：教材の再構成・HTML 生成・内部参照を確認。この時点では App の実機操作や新しいアプリ実装を実施していませんでした。

前回の再構成時の確認（今回の修正前）：サイト39ページ・内部リンク／画像／アンカー755参照が成功。2回の生成結果が一致し、当時の App 全9章に CLI 代替手順と合流条件があることを確認しました。ブラウザーで参加者の入口、演習0への移動、章内の CLI 手順への移動と表示を確認しています。

| 演習 | 合流時の確認対象 | App 実走 | 講師の CLI 緊急対応検証 |
| --- | --- | --- | --- |
| 0 準備 | 自分のコピー、Node、起動とテスト | コピー作成・外部シェルで開始状態のテスト成功。後続の星評価セッションで App の Run 起動・停止を確認（初回セットアップは未確認） | 未検証 |
| 1 接続 | 同じ checkout を開き、構成について応答 | 一部確認：初期設定・Chats 応答・Open folder・設定レビュー・完全再起動後の演習 repo の読み取りと構成への応答。GitHub 連携プロジェクトを追加し、My work の8件の Issue 表示を確認 | 未検証 |
| 2 星評価 | 数値と null の表示、テスト、PR・マージ | App で実装・レビュー修正・検査・Run 起動停止を確認。gh 経由で PR #9 作成、CI 全4ジョブ成功。App 固有の PR 作成は失敗、マージは未実施 | 未検証 |
| 3 指示 | TSDoc・ヘッダーの標準と提示コード、PR・マージ | 未検証 | 未検証 |
| 4 フィルター | 星評価・指示を継承し、絞り込みと quality-checks | 未検証 | 未検証 |
| 5 MCP | MCP ツールの実行、複合条件・解除等の検証 | 一部確認：カタログ・登録フォーム。保存・ツール実行は未実施 | 未検証 |
| 6 マージ | CI とレビュー、演習コピーへ統合 | 未検証 | 未検証（通常マージのみ代替可能） |
| 7 Canvas | 共有・保存・Issue 操作 | 未検証 | 機能代替不可。優先順位整理は未検証 |
| 8 Automation | 手動実行、結果、終了状態 | 未検証 | 機能代替不可。単発要約は未検証 |

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
