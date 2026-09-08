# Tailspin Toys CLI 実アカウント検証記録

2026年9月8日実施。**専用の実アカウント環境で CLI の主要演習0〜6を実行し、2本の PR と CI 成功まで確認しました。** 演習7は下記のコマンドを確認し、任意のクラウド委任・Gist 公開は対象外としました。

教材への修正・回避手順の反映履歴は [dev-days-jp Issue #1](https://github.com/iwizsophy/dev-days-jp/issues/1) に記録しています。外部テンプレート自体の修正や未検証コースの完走を保証するものではありません。

## 対象と分離

- アカウント：`iwizsophy`（GitHub のブラウザー表示で確認）。
- 専用の非公開リポジトリ：[dev-days-tailspin-cli-verification-20260908](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908)。
- 環境：このリポジトリ専用の GitHub Codespace `turbo-space-adventure-gwqv7v7674hw6p`。
- 教材：`sources.json` 記載の Copilot Workshops コミット `7ddcf241c1cd10b8e90c0df96f6bef81e710392a` の日本語版。
- テンプレート：`github-samples/tailspin-toys`、確認した上流コミット `bae003609c8cff0c51d92658b8d3bd89450464f1`。
- 作成された検証リポジトリの初期コミット：`80d35f2625bd532e73912a2e25d36ccb4dcddf01`。
- PC 側の GitHub CLI は別アカウントだったため、認証設定を変更せず、検証の GitHub 操作には使用していません。

## 確認済み

- テンプレートから専用リポジトリを作成できた。
- [初期 Issue 作成ワークフロー](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34210495054)が成功し、8件の Issue が作成された。
- [初期コミットの Run tests](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34210495092)が成功した。これは初期コードの CI であり、Copilot による演習実装の検証ではない。
- Codespace の作成・構築・接続が完了した。途中で `The codespace is not available` と表示されたが、リポジトリの Code → Codespaces → 作成済み環境名から再接続して復旧した。
- Node.js `v24.20.0`、npm `11.19.0`、Copilot CLI `1.0.83` を確認した。
- `npm install -g @github/copilot` による導入、フォルダーの信頼、日本語のファイル構成質問への応答、`/help`、`exit` が成功した。初回の読み取り専用セッションでは変更 `+0 -0`、使用量 `7.91 AI Credits` と表示された。
- `gh` が未導入だったため、Codespace 内で `sudo apt-get update -qq && sudo apt-get install -y gh` を実行した。`gh` `2.23.0` の導入と、`gh api user --jq .login` の結果 `iwizsophy` を確認した。
- 演習2はリポジトリ規約の `feature/` 接頭辞を使い、`feature/update-custom-instructions` で開始した。
- 演習2の初回生成では injectable な `getAllPublishers(db)` が作成された。単純な doc comment は最初から付いたが、ファイルヘッダー・`@param`・`@returns` はなかった。
- カスタム指示の追加後、ファイルヘッダーと完全な TSDoc が反映された。空データ・id/name・名前順を検証する単体テスト2件も追加した。
- 演習2の検証：単体テスト29件、E2E21件、lint、型チェックが成功。生成された helper、テスト、指示差分をレビューした。
- 演習2の3ファイルを専用ブランチに commit・push した。
- 演習3の `/plan` が Issue #7 の要件に沿って確認質問を表示した。カテゴリ複数チェックボックス、出版社単一選択、ページ内状態、該当なしメッセージと解除を選び、helper・UI・単体/E2E テストの計画を確認して autopilot で実装を開始した。
- 演習3の実装後に静的ビルド・単体テスト・E2E・lint・型チェックが成功し、`/diff` で8ファイルの差分を表示できた。
- 演習4の `/mcp add` で `playwright` を登録できた。Chrome 未導入エラーを `npx playwright install chrome` で解消後、sandbox namespace エラーが残った。専用 Codespace の起動設定に `--no-sandbox --isolated` を追加して CLI を再起動し、MCP のブラウザー操作が成功した。
- MCP で確認：初期21件、Strategy OR Puzzle は8件、Strategy AND CodeForge Studios は `DevOps Dominion` の1件、解除で21件、Shift+Tab と Space で Strategy 選択後4件。MCP の操作ツールが実行されたことを確認した。
- 該当なし表示は、有効なカテゴリ×出版社の組み合わせがすべてデータを持つため、通常の Playwright 実行で未登録出版社を一時的に DOM に追加して確認した。実ユーザーの通常選択で0件になるケースを確認したわけではない。
- 演習5の `make-contribution` と `quality-checks` を通じて、単体テスト35件、Playwright24件、lint、型チェックが成功した。MCP が生成した一時ファイルを除外し、対象8ファイルを commit・push する手順が進んだ。
- 演習5で [PR #11](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/11) を作成した。head `feature/update-custom-instructions` → base `main`、演習2を含む2コミット・11ファイル。Issue #7 を参照し、日本語の説明とテスト結果が記載されていることをブラウザーで確認した。merge はしていない。
- PR #11 の [CI](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34214263514) は4ジョブ（frontend-lint、frontend-tests、type-check、unit-tests）すべて成功した。
- 演習6の `/agent` から Accessibility agent を選択できた。PR Readiness は `"playwright/\*"` の無効な YAML エスケープで読み込みエラーになったため、本文に `"playwright/*"` への修正を記載した。元の YAML が失敗し、補正後は parse できることもローカルで確認した。
- 演習6では不足していた [Issue #12](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/issues/12) を専用リポジトリに作成し、[PR #13](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/pull/13) を作成した。head `feature/accessibility-cli` → base `main`。高コントラストのオン・オフ、localStorage による設定保持、キーボード操作と再読み込み後の復元を MCP と E2E で確認した。
- 演習6の生成途中で E2E の配置、ボタン名変更による locator、通常モードのヘッダー配色に不具合が見つかった。修正後、全テスト・lint・型チェックが成功してから PR を作成した。サイト全体の WCAG 適合認証を実施したという意味ではない。
- 演習7の `/context` はモデル名と使用量を表示した（圧縮前 `68k/400k`, `17%`）。
- PR #13 の [CI](https://github.com/iwizsophy/dev-days-tailspin-cli-verification-20260908/actions/runs/34215288800) は4ジョブすべて成功。ログでも単体テスト27件、E2E23件の成功を確認した。PR #11 と #13 は独立したブランチで、どちらも未マージ。
- 演習7の `/compact` 後は `19k/400k`, `5%` に縮小した。`/model` の選択画面を確認し、変更せず閉じた。モデルは既定の GPT-5.6 Terra を使用した。
- `/share` 単独ではリポジトリ閲覧者向けのセッションリンクが作成されたため、`/share off` で共有を停止した。`/share file /tmp/dev-days-cli-session.md` によるローカル保存を改めて実行し、4,829行のファイルが存在することを確認した。Gist は作成していない。
- `/clear` のコンテキスト消去を確認後、CLI を終了した。終了時の未追跡ファイルは `.playwright-mcp/` のみで、実装の未コミット差分はない。

## 教材に反映した差分

- Codespaces の作成ボタンは `Create codespace on main` と表示される場合がある。従来の `+` 表示と併記した。
- 現行 Tailspin Toys の Node.js 要件は `22.13` 以上。単なる `22` 以上という記述を補正した。
- 演習6の高コントラストモードに対応する初期 Issue がない。Issue がない場合に、本文の要件を直接使う手順を追加した。
- 演習2の最初の commit 前に、リポジトリの `quality-checks` スキルに従うテスト追加・検証手順を補った。
- `gh` 未導入時のインストールと利用アカウントの確認、`feature/` ブランチ名、現行 `/diff` のキー操作を補った。
- Playwright MCP 用 Chrome の導入、Codespaces の sandbox エラーへの限定的な回避手順、新しいターミナルで開発サーバーを起動する操作を補った。
- PR Readiness の YAML 修正、`/share file` と `/share off`、`/model` と `/config model` の違いを反映した。

## 残る制約・未確認の範囲

MCP は接続時にキャンセル表示が出ることがあり、再起動後に接続・操作できた。常に初回で接続できるとは限らない。PR Readiness の修正は YAML の解析まで確認し、当該エージェント自体の実行はしていない。

演習7の任意の `/delegate`（クラウド委任）、Gist 公開、モデル変更は未実行。演習8は振り返りであり、追加の実装検証はない。Copilot App、Mona Mayhem、App と CLI の往復操作は今回の実アカウント検証に含まない。

## 終了時の状態

専用リポジトリと検証 PR を保存し、既存の他リポジトリへの書き込みは行っていない。テンプレートの Dependabot により自動作成された PR #9・#10 は演習 PR と区別し、変更・マージしていない。PC 側の GitHub 認証も変更していない。

検証用 Codespace は停止済み。GitHub の表示から Active と Stop codespace が消えたことを確認した。Codespace 自体は削除していないため、保存領域は残る。未追跡の `.playwright-mcp/` が残るため、GitHub では Uncommitted changes と表示される。セッションのローカル出力は Codespace の `/tmp` にある一時ファイルであり、永続的な検証記録はこの文書と PR・CI を参照する。
