# Tailspin Toys CLI 実アカウント検証記録

2026年9月8日実施。**専用の実アカウント環境で CLI の主要演習0〜6を実行し、2本の PR と CI 成功まで確認しました。** 演習7は下記のコマンドを確認し、任意のクラウド委任・Gist 公開は対象外としました。

教材への修正・回避手順の反映履歴は [dev-days-jp Issue #1](https://github.com/iwizsophy/dev-days-jp/issues/1) に記録しています。外部テンプレート自体の修正や未検証コースの完走を保証するものではありません。

## 対象と環境の分離

- **アカウント**：`iwizsophy`（GitHub Web ブラウザー表示で確認）。
- **検証用非公開リポジトリ**：[dev-days-tailspin-cli-verification-20260908](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908)。
- **実行環境**：上記リポジトリ専用の GitHub Codespace `turbo-space-adventure-gwqv7v7674hw6p`。
- **教材原稿**：`sources.json` 記載の Copilot Workshops コミット `7ddcf241c1cd10b8e90c0df96f6bef81e710392a` の日本語版。
- **テンプレート**：`github-samples/tailspin-toys`（確認した上流コミット `bae003609c8cff0c51d92658b8d3bd89450464f1`）。
- **検証リポジトリの初期コミット**：`80d35f2625bd532e73912a2e25d36ccb4dcddf01`。
- **認証の分離**：PC 側の GitHub CLI は別アカウントであったため、認証設定を変更せず、検証の GitHub 操作には使用していません。

## 実機検証の確認結果（演習別）

### 演習0：リポジトリ作成と環境セットアップ
- テンプレートからの専用リポジトリ作成に成功。
- [初期 Issue 作成ワークフロー](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34210495054) が成功し、8件の Issue が自動作成された。
- [初期コミットの Run tests](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34210495092) が成功。これは初期コードの CI であり、Copilot による演習実装の検証ではありません。
- Codespace の作成・構築・接続が完了。途中で `The codespace is not available` と表示されたが、リポジトリの Code → Codespaces → 作成済み環境名から再接続して復旧した。
- Node.js `v24.20.0`、npm `11.19.0`、Copilot CLI `1.0.83` の動作を確認。

### 演習1：Copilot CLI の導入と基本応答
- `npm install -g @github/copilot` による導入、フォルダーの信頼、日本語でのファイル構成質問への応答、`/help`、`exit` が成功。
- 初回の読み取り専用セッションでは変更 `+0 -0`、使用量 `7.91 AI Credits` と表示された。
- Codespace 内に `gh` が未導入だったため、`sudo apt-get update -qq && sudo apt-get install -y gh` で `gh` `2.23.0` を導入し、`gh api user --jq .login` で `iwizsophy` を確認。

### 演習2：カスタム指示の追加とテスト
- リポジトリ規約の `feature/` 接頭辞を用い、`feature/update-custom-instructions` ブランチで開始。
- 初回生成では injectable な `getAllPublishers(db)` が作成された。単純な doc comment は付与されたが、ファイルヘッダー・`@param`・`@returns` は欠落していた。
- カスタム指示を追加したところ、ファイルヘッダーと完全な TSDoc が正しく反映された。
- 空データ・id/name・名前順を検証する単体テスト2件を追加。
- 単体テスト29件、E2E 21件、lint、型チェックがすべて成功。差分をレビューし、専用ブランチへ commit・push した。

### 演習3：プランモードによるフィルター実装
- `/plan` を実行し、Issue #7 の要件に沿って確認質問が表示された。「カテゴリ複数チェックボックス」「出版社単一選択」「ページ内状態」「該当なしメッセージと解除」を選択し、計画を確認して autopilot で自律実装を開始。
- 実装後、静的ビルド、単体テスト、E2E、lint、型チェックが成功し、`/diff` で8ファイルの差分を確認。

### 演習4：Playwright MCP によるブラウザー検証
- `/mcp add` で `playwright` を登録。
- Chrome 未導入エラーを `npx playwright install chrome` で解消後、sandbox namespace エラーが発生したため、起動設定に `--no-sandbox --isolated` を追加して CLI を再起動し、ブラウザー操作に成功。
- MCP 実走により、初期21件、Strategy OR Puzzle（8件）、Strategy AND CodeForge Studios（`DevOps Dominion` 1件）、解除（21件）、Shift+Tab と Space による操作（4件）を確認。
- 該当なし（0件）表示については、既存データでは全カテゴリ×出版社の組み合わせが存在するため、通常の Playwright 実行で未登録出版社を一時的に DOM へ追加して確認した。実ユーザーの通常選択で0件になるケースを確認したわけではない。

### 演習5：品質検査と Pull Request 作成
- `make-contribution` と `quality-checks` を通じ、単体テスト35件、Playwright 24件、lint、型チェックが成功。MCP 一時ファイルを除外して8ファイルを commit・push。
- [PR #11](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/11)（演習2を含む2コミット・11ファイル）を作成。Issue #7 への参照、日本語の説明、テスト結果が記載されていることをブラウザーで確認（merge は未実施）。
- PR #11 の [CI](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34214263514)（frontend-lint、frontend-tests、type-check、unit-tests の全4ジョブ）が成功。

### 演習6：カスタムエージェントとアクセシビリティ対応
- `/agent` から Accessibility agent を選択。
- PR Readiness の読み込みで、`"playwright/\*"` という無効な YAML エスケープによるエラーが発生。`"playwright/*"` への修正により parse できることをローカルで確認。
- 不足していた [Issue #12](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/issues/12) を専用リポジトリに起票し、[PR #13](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/13)（`feature/accessibility-cli` → `main`）を作成。高コントラストのオン・オフ、localStorage による設定保持、キーボード操作と再読み込み後の復元を MCP と E2E で確認。
- 生成途中で E2E 配置、ボタン名変更による locator、通常モードのヘッダー配色に不具合が見つかったため修正。全テスト・lint・型チェックの成功を確認してから PR を作成。サイト全体の WCAG 適合認証を実施したという意味ではありません。
- PR #13 の [CI](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34215288800)（全4ジョブ、単体27件・E2E 23件）が成功。PR #11 と PR #13 は独立したブランチであり、どちらも未マージのまま保持。

### 演習7：コンテキスト管理とスラッシュコマンド
- `/context` でモデル名と使用量を確認（圧縮前 `68k/400k`, `17%`）。
- `/compact` 実行後は `19k/400k`, `5%` に縮小。
- `/model` の選択画面を確認（既定の GPT-5.6 Terra を使用し、変更せず閉じた）。
- `/share` 単独ではリポジトリ閲覧者向けのセッションリンクが作成されたため、`/share off` で停止。その後 `/share file /tmp/dev-days-cli-session.md` でローカル保存を実行し、4,829行のファイル出力を確認（Gist は作成していない）。
- `/clear` によるコンテキスト消去を確認後、CLI を終了。未追跡ファイルは `.playwright-mcp/` のみで、実装の未コミット差分はゼロ。

## 教材に反映した差分と補足

- **Codespaces 作成ボタン**：環境により `Create codespace on main` と表示される場合があるため、従来の `+` 表示と併記した。
- **Node.js 要件**：現行 Tailspin Toys の要件は `22.13` 以上であり、単なる「22以上」という記述を補正した。
- **Issue 不足への対応**：演習6の高コントラストモードに対応する初期 Issue が存在しないため、本文の要件を直接使う手順を追加した。
- **品質手順の補完**：演習2の初コミット前に、リポジトリの `quality-checks` スキルに従うテスト追加・検証手順を補った。
- **CLI 環境の整備**：`gh` 未導入時のインストールと利用アカウント確認、`feature/` ブランチ名、現行 `/diff` のキー操作を補った。
- **MCP 回避策**：Playwright MCP 用 Chrome の導入、Codespaces の sandbox エラーへの限定的な回避手順、別ターミナルでの開発サーバー起動を補った。
- **コマンド・構文の補正**：PR Readiness の YAML エスケープ修正、`/share file` と `/share off`、`/model` と `/config model` の違いを反映した。

## 残る制約と未確認の範囲

- **MCP 接続の安定性**：MCP 接続時にキャンセル表示が出ることがあり、再起動後に接続・操作できた。常に初回で接続できるとは限らない。
- **エージェント自体の実行**：PR Readiness の修正は YAML 解析の成功まで確認したが、当該エージェント自体の実走は行っていない。
- **未実施コマンド**：演習7における任意の `/delegate`（クラウド委任）、Gist 公開、モデル変更は未実行である。
- **コース範囲の境界**：演習8は振り返りであり、追加の実装検証はない。また、Copilot App、Mona Mayhem、および App と CLI の往復操作は、今回の実アカウント検証には一切含まない。

## 終了時の状態

- 専用リポジトリと検証 PR を保存し、既存の他リポジトリへの書き込みは行っていない。
- テンプレートの Dependabot により自動作成された PR #9・#10 は、演習 PR と厳密に区別し、変更・マージしていない。
- PC 側の GitHub 認証設定も変更していない。
- 検証用 Codespace は停止済み（GitHub 表示から Active / Stop codespace が消去されたことを確認）。Codespace 自体は削除していないため保存領域は残る。未追跡の `.playwright-mcp/` が残るため、GitHub では Uncommitted changes と表示される。
- セッションのローカル出力は Codespace の `/tmp` にある一時ファイルであり、永続的な検証記録はこの文書と PR・CI を参照する。
