# 2026年10月4日 配布資料に沿ったApp実走検証

今回の環境では、配布資料の受講者向け内容に沿って第0〜8章を完了できました。画面差を読み替え、本文のレビュー工程で追加修正を行った結果として、条件付きで全章完了と判定します。初回プロンプトだけの無修正成功を保証する結果ではありません。

本レポートには、必要だった補足操作、追加修正の結果、画面の差し替え候補を記録しました。受講者向け原稿の直接修正は行っていません。初回インストール、初回サインイン、発生しなかった障害対応など、未確認の範囲も明示しています。

ツール履歴や差分の原記録は、作業用フォルダー`tmp/verification-20261004/`に保存しています。本書に記載した原記録のファイル名はその保存先を指し、原記録そのものはコミットに含めていません。確認した結果、判断理由、GitHub上の根拠、取得画像は本書と画像対応表にまとめています。

## 検証対象

| 項目 | 対象 |
| :--- | :--- |
| 検証日 | 2026年10月4日 |
| 配布PDF | `output/pdf/dev-days-app-participant.pdf`、74ページ |
| PDFのSHA-256 | `8b7e3daa22d2b7708da6b56b49dfc64f34b1f7c2f9f1d5f3806e8171023c0e1f` |
| 原稿のコミット | `af9cbaf899ac704a68ea597e647524655d1d8d7a` |
| テンプレート | [iwizsophy/dev-days-tailspin-template](https://github.com/iwizsophy/dev-days-tailspin-template) |
| テンプレートのリリースタグ | [v2026.10.03](https://github.com/iwizsophy/dev-days-tailspin-template/tree/v2026.10.03) |
| テンプレートのコミット | `ae18804e616f895ef30a15732037b9125f68ac74` |
| 演習用コピー | [iwizsophy/dev-days-tailspin-participant-check-20261004](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004) |
| GitHub Copilot App | 既存の1.1.26を使用し、更新画面で最新状態を確認 |
| セッション内のNode.js | `v24.19.0` |

今回の実走は、前回の演習用コピーを再利用せず、新しいコピーから開始しました。Appの初回インストールと初回サインインは再現していません。既存のインストールとサインイン状態で進めた結果を記録します。

## 章ごとの結果

「確認済み」は実際の操作と結果を確認した項目を指します。初回処理とレビュー後の追加修正は分けて記録し、当時の未確認項目にはその時点を明記しました。本文の手順にない操作が必要だった箇所は、補足操作と修正候補として記録しました。

| 章・内容 | 状況 | 根拠 | 補足操作 | 未確認の項目 |
| :--- | :--- | :--- | :--- | :--- |
| 0 前提条件 | コピー作成と課題生成を確認済み | GitHubのUse this templateからコピーを作成。初期コミットとテンプレートのtreeが一致し、初期設定後にIssueが8件生成された。 | 特になし。 | Appの初回インストールと初回サインイン。 |
| 1 Appの接続と基本操作 | 接続、ビュー作成、課題閲覧、Quick Chatを確認済み | Add GitHub repositoryでコピーを追加。Review repository contentから内容を確認し、Accept for new sessionsで承認。Assigned to meの空表示からNew viewを作成し、State: OpenのままSaveして8件の課題を表示。Quick Chatの日本語回答とIdleも確認した。 | 1.3のProjects選択だけではIssuesのリポジトリ範囲が変わらなかった。Issues上部の選択欄で旧コピーを解除し、新コピーだけを選択した。狭い表示ではIssue詳細を閉じてからNew viewを開いた。 | Appの初回インストールと初回サインイン。 |
| 2 星評価の表示 | 実装、テスト、画面確認、手動マージを確認済み | 初回プロンプトで実装。実際のGameCardを使う4.2・0・5・nullの検査、E2E 22件、単体テスト27件、lint、型検査、build、差分検査が成功。PR #13のCI全4ジョブ成功後に、Agent mergeをOffにして手動マージした。 | Browserが自動で開かず、本文の案内どおりRunのURLを別ブラウザーで開いた。Ready to mergeがCI実行中にも表示されたため、全成功を待ってダイアログを開き直した。追加レビュー用プロンプトは使用していない。 | 本章で求める実装とマージは確認済み。公開サイトへのデプロイは対象外。 |
| 3 カスタム指示 | 指示更新、コード例のレビュー、CI、手動マージを確認済み | 共通指示とパス固有指示を確認。Issue #8から前章のmainを継承し、固定プロンプトで更新。レビューに基づく追加修正を2回実施。固定プロンプトによるPublishersのコード例でファイルが変わらないことを確認し、PR #14のCI全4ジョブ成功後に手動マージした。Issue #8もClosedになった。 | applyToの確認にはRawへの切り替えが必要だった。入力欄の/issue-fixを全選択で置換。Node.js条件、scriptsの説明、Astro Props例のリンクとdata-testidをレビューで修正した。Appに残ったCI 3/4の表示は、本文どおりダイアログを開き直して確認した。 | ローカルの単体テスト、E2E、buildは本章で実行していない。単体テストとE2EはCIで成功。第4章の新しいworktreeへの継承も確認済み。 |
| 4 フィルター機能 | 計画、実装、品質検査、Appのbuildを完了 | Planを1回修正して承認。手動の件数・タイトルと通常CSV不変を確認。追加修正1回目と明示的なquality-checksで単体38件、E2E 26件などが成功。修正2回目では指定したE2E 10件だけが成功。Appのbuildで24ページを生成し、修正後の手動操作も21→ORとGitHub Gamesで2→Tab・Enterで21を確認した。 | Tab移動、DB指定、後片付けを修正し、検査ランナーの追加引数とSkillの実行例も2回目の修正でそろえた。 | Playwright MCP検証は第5章、コミットとPRのCI・マージは第6章で確認済み。 |
| 5 Playwright MCP | 実際のMCP検証と後片付けを完了 | 通常21→Strategy 4→OR 8→GitHub Games 2→解除21、Tab・Enter、隔離3→0→解除3をMCPで確認。補足で出版社単独5件・6件とタイトル、StrategyのSpace選択4件・解除21件を確認し、ブラウザー、サーバー、今回の出力を片付けた。 | 初回は未実施なしと報告されたが3条件の履歴がなく、5.4のレビューで追加指示を1回実施した。管理経路の差はR06に記録。 | リポジトリ定義3件の個別のGUI接続表示は未確認。演習に必要なPlaywrightの実際の呼び出しと結果は確認済み。 |
| 6 Agent Merge | CI確認後のAgent Mergeを完了 | 通常のCreate PRでPR #15を作成。最新コミットのCI全4ジョブ成功をWebとAPIで確認してから、Agent mergeをOnにした。3秒以内にMergedとなり、AppとGitHubの両方でマージを確認。Issue #7もClosedになった。 | mainのprotected=falseを確認し、本文の代替経路を使用。PR作成後のAgent mergeはスイッチのOnだけで開始し、追加の主ボタン操作はなかった。画面差をR07に記録。 | 四項目の権限メニューの表示は未確認。レビュー対応、CI失敗修復、競合修復は発生していない。第7章の新しいworktreeへの継承は確認済み。 |
| 7 Canvas | 共有、再利用、検索、CI・マージ、Refreshまで完了 | 検索実装の単体44件、E2E 29件などが成功。MCP結果を主担当の別ブラウザーでも確認し、片付けを独立に検査。PR #18の最新コミットのCI全4ジョブ成功後、Agent Mergeでマージ。Issue #1はClosed。CanvasのRefresh後にOpen #2〜#6の5件、上位#5・#2・#6、残り#3・#4を確認した。 | 7.5の操作条件を追加依頼で指定。MCPツールの一覧は結果メッセージに基づき、実際のNavigate履歴の確認と区別。検索の詳細リンクはMCPではhref確認までで、E2Eの詳細遷移は成功。 | MCPによる詳細リンクのクリック遷移は未実施。Agent merge actionsの四項目の個別表示と、発生しなかったCI・競合修復は未確認。 |
| 8 振り返りと自動化 | Manual・Localの自動化と結果照合を完了 | 8.1の固定プロンプトを変更せずCreate and run。Recent runsでLocal、Succeeded、53秒を確認。対象とJSTの期間を明記し、期間内のマージ済みPR 5件とOpen Issue 5件を報告。主担当のAPI照合で番号・タイトル・URL・日時・状態が一致した。mainと作業ツリー、Issueのコメントと更新時刻の不変も確認。 | 特になし。通常のSetupが作る自動生成物と、演習内容の変更を区別して確認した。 | 継続的なスケジュール実行とクラウド実行は今回のManual・Local検証の対象外。 |

## コピー作成の根拠

| 確認対象 | 記録 |
| :--- | :--- |
| 作成経路 | GitHub WebのUse this template → Create a new repository |
| コピーの初期コミット | `1c7e310a24859158555425970af0f590cfb41012` |
| コピーとテンプレートで一致したtree | `8a02e4a24c4d8423f3259bdb0aad5bd0e0e9c5eb` |
| 初期設定後のmain | `d9b32bfc2bde6fe784c035d4633f3a7c73f8a13d` |
| 生成された演習用Issue | #1〜#8の8件 |
| 初期設定の実行結果 | [成功したワークフロー](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37166872793) |

初期コミットのtreeが一致しているため、テンプレートと同じファイル構成から演習を開始したと確認できます。第2章の開始位置は、初期設定後のmainです。

## セッションとPRの記録

| 章 | 開始時のmain・HEAD | worktree・ブランチ | PR | CI・マージ |
| :--- | :--- | :--- | :--- | :--- |
| 2 | `d9b32bfc2bde6fe784c035d4633f3a7c73f8a13d` | 開始時は`iwizsophy-vigilant-engine`。実装中に`iwizsophy-game-card-ratings`へ変更された。 | [PR #13](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/13) | [CI全4ジョブ成功](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37168609105)。Appから手動マージし、AppとGitHub WebでMergedを確認。 |
| 3 | `c42adb3e00e592a1c5474afcdc403e8fdbcf0952`、開始時に作業ツリーの未変更を確認 | `iwizsophy-issue-8-update-our-repository-coding-standards-801210`。ブランチは`iwizsophy-update-coding-standards`。 | [PR #14](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/14) | [CI全4ジョブ成功](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37170430963)。Appで手動マージし、AppとGitHub WebでMergedを確認。 |
| 4〜6 | `59d8ea1af5d0922a2f892c8a9deb365f79f932bf`、第4章の開始時は未変更。同じセッションで第5〜6章を継続 | `iwizsophy-issue-7-allow-users-to-filter-games-by-category-51494e`。ブランチは`iwizsophy-allow-users-to-filter-games-by-category`。 | [PR #15](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/15) | [最新コミットのCI全4ジョブ成功](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37173455164)を確認後、Agent Mergeでマージ。AppとGitHubでMergedを確認。 |
| 7 Canvas共有 | `3acdd179f1a1d88b5a5418035d889071951f5e59`、開始時に作業ツリーの未変更を確認 | `iwizsophy-fictional-telegram`。ブランチは`iwizsophy-issue-triage-kanban`。 | [PR #17](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/17) | [最新コミットのCI全4ジョブ成功](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37175377043)後、Agent Mergeでマージ。AppとGitHubでMergedを確認。 |
| 7 Canvas再利用・検索 | `aa74cee0eb29edfcbc52e83ab60d1dfd85c6e1ee`、別セッションで最新mainを継承 | worktreeは`iwizsophy-musical-guacamole`。ブランチは開始時の同名から`iwizsophy-game-title-search`へ変更。 | [PR #18](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/18) | [最新コミットのCI全4ジョブ成功](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37177105230)後、Agent Mergeでマージ。AppとGitHubでMergedを確認。 |
| 8 自動化 | `566da7b02aa0319bba6c6ee67d088e8f84165151`、作成前に確認したmain | worktreeとブランチは`iwizsophy-ideal-adventure`。 | 読み取りのみ。PRは作成していない。 | Manual・Localの実行がSucceeded。実行後もmainと作業ツリーは未変更。 |

第2章の作業ディレクトリは次の場所です。

```text
iwizsophy-vigilant-engine
```

各章の開始位置、PRのURL、最新コミットのCI結果、マージ先を記録しました。ブランチ名の変更だけでは、ファイル変更や実装完了の根拠として扱いません。

## 第2章の実装と確認結果

配布資料の初回プロンプトで星評価を実装できました。追加レビュー用プロンプトは使用していません。生成中のE2E用fixtureのbuildや文字化けは、エージェントが追加指示なしで修正しました。PR作成と手動マージは、実装確認後にAppの操作で進めています。

### 表示とテスト

| 確認対象 | 結果 |
| :--- | :--- |
| 既存部品の再利用 | GameCardで既存のStarRatingを再利用した。 |
| 未評価 | nullではNo rating yetを表示した。 |
| 評価値0 | 数値として0.0を表示し、未評価と区別した。 |
| 実際のレンダリング | GameCardを使うE2E用fixtureで4.2、0、5、nullの評価欄を期待値との完全一致で検査した。カードのA要素とhrefも検査した。 |
| ローカルE2E | 22件成功。 |
| 単体テスト | PR作成処理中にtest:unitを実行し、27件成功。 |
| その他の検査 | lint、型検査、build、diff checkが成功。通常のbuildにはE2E用fixtureを含めていない。 |
| 通常データの画面 | 21件のカードと21件の評価を確認。タイトル、説明、カテゴリー、パブリッシャーを維持した。 |
| 詳細へのリンク | Binary Frontierのカードから/game/14へ移動し、詳細の評価3.8を確認。Back all gamesで一覧に戻れた。 |
| 差分レビュー | 別担当による差分確認で不具合の指摘はなかった。 |

### 開発サーバーの起動と停止

Run optionsからRun development siteを起動し、Runに表示された次のURLを別ブラウザーで開きました。AppのBrowserパネルは自動で開かなかったため、本文にある代替操作を使用しています。

```text
http://127.0.0.1:4321/
```

画面確認後にStopを選び、Shell session endedの表示を確認しました。停止後の接続状態の確認でも、ポート4321の待ち受けはありませんでした。

既存のPlaywright設定にはreuseExistingServerが残っています。別のworktreeへ進む際は、テストが使うサーバーと対象の作業場所が一致することを引き続き確認します。

### PRとmainへの反映

| 項目 | 記録 |
| :--- | :--- |
| PR作成 | Appの通常のCreate PRを使用。作成処理中に補助Issue #12が自動作成された。 |
| 実装コミット | `2038d40c6c0d3bac313f672e87871ae3908c4626` |
| Author・Committer | `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`で一致。 |
| 送信先 | `origin iwizsophy-game-card-ratings`。同名ブランチへ送信し、追跡先を設定した。 |
| PR | [#13](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/13)、取り込み先main |
| CI | [実行37168609105](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37168609105)のfrontend-lint、type-check、unit-tests、frontend-testsがすべて成功。 |
| マージ方式 | Agent mergeをOffにし、Appから手動でMergeを選択した。 |
| マージ確認 | AppとGitHub Webの両方でMergedを確認。 |
| マージコミット | `c42adb3e00e592a1c5474afcdc403e8fdbcf0952` |
| マージ日時 | `2026-10-04T01:42:16Z` |

Ready to mergeは、CIが3/4件の段階でも表示されました。本文どおり全ジョブの成功を待ち、ダイアログを開き直してからマージしています。ボタンの表示だけでCIの成功を判断しない説明は、今回の実走でも必要でした。

Appが作成した補助Issue #12は、演習用課題#1〜#8と別枠の記録です。

## 第3章の指示更新と確認結果

### 指示ファイルの確認

Filesを開き、Ctrl+Pでcopilot-instructions.mdを検索しました。`.github/instructions`内のパス固有指示も読み、unit-tests.instructions.mdのapplyToと、Drizzleの指示にある相対リンクを確認しています。

Rich text表示ではファイル冒頭のapplyToが見えず、Rawに切り替える必要がありました。View optionsの隠しファイル表示は、本文のShow hidden filesに対し、実機ではShow all hidden filesとShow tracked hidden filesの選択肢でした。

### Issueからの開始と初回更新

| 項目 | 記録 |
| :--- | :--- |
| 対象Issue | [#8 Update our repository coding standards](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/8) |
| セッション | `553a73b5-35f8-40ff-b99e-6d4bffdf9a8b` |
| 開始時のHEAD | `c42adb3e00e592a1c5474afcdc403e8fdbcf0952`。第2章のマージ済みmainを継承し、作業ツリーに未変更を確認。 |
| 作業モード | Interactive |
| 初回プロンプト | 3.3に記載された固定プロンプトをそのまま送信。Issue起点の入力欄にあった/issue-fixは、Ctrl+Aで全選択して置換した。 |
| 初回応答終了時の差分 | 11ファイル、138行追加、27行削除。 |
| 初回更新後の検査 | npm run lint、npm run typecheck:all、git diff --checkが成功。 |
| PR | 初回更新時は未作成。その後、PR #14を作成した。 |

第3章の作業ディレクトリは次の場所です。

```text
iwizsophy-issue-8-update-our-repository-coding-standards-801210
```

初回応答と変更一覧の根拠は`tmp/verification-20261004/chapter3-update-ui.txt`です。この記録は初回更新終了時のもので、追加修正後の最終結果を示すものではありません。

### レビューに基づく追加修正

初回更新では、READMEとDrizzle指示にNode.js 22.13以上の説明が残りました。package.jsonの24.19.0以上、25未満という条件と一致していません。また、共通指示のscriptsディレクトリが存在しないという説明は、実際のscripts/serve.mjsと矛盾していました。

3.4の差分レビューで見つかった矛盾として追加修正を依頼し、共通指示、README、Drizzle指示、CONTRIBUTINGの4箇所の修正とIdleを確認しました。修正後のNode.js説明は、package.jsonの条件と`.nvmrc`の24.19.0に一致しています。

Astro 7.3.3自体の条件は22.12.0以上であり、プロジェクト側でより厳しい条件を設定しています。主担当がインストール済みのnode_modules/astro/package.jsonを読み、この違いを確認しました。

追加修正は文書だけで、git diff --checkが成功しました。この追加修正直後にlintは再実行していません。その後のコード例をレビューし、Astro Props例のリンクとdata-testidの補足だけを追加する2回目の修正を依頼しました。この修正後もgit diff --checkが成功しています。最終差分は12ファイル、142行追加、31行削除でした。

### コード例とファイル変更の有無

3.4の固定プロンプトをそのまま送り、ファイルを変更せずにPublishersを返すコード例を提示できました。関数の目的、注入可能なdb引数の@param、戻り値の@returns、名前順の並び方を確認しています。Publisher型は既存のidとnameに一致しました。

コード例の提示前後で保存した差分のSHA-256が一致しました。このプロンプトによってファイルが変更されていないことを、応答内容と差分の両方で確認しています。

| 根拠 | 記録 |
| :--- | :--- |
| 提示前の差分 | `tmp/verification-20261004/chapter3-before-example.diff` |
| 提示後の差分 | `tmp/verification-20261004/chapter3-after-example.diff` |
| 両ファイルのSHA-256 | `3213DDFA6026877F136FFD0CB7755FF12AD052BA58F6929D612C925F4F01D234` |
| コード例の応答 | `tmp/verification-20261004/chapter3-code-example-ui.txt` |

### PR、CI、マージ

| 項目 | 記録 |
| :--- | :--- |
| PR作成 | Appの通常のCreate PRを使用。 |
| 実装コミット | `d0899d25b344ed6fc8c893e1ff6a04f3c9ac3fa7` |
| Author・Committer | `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`で一致。 |
| PR | [#14](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/14) |
| CI | [実行37170430963](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37170430963)のfrontend-lint、type-check、unit-tests、frontend-testsがすべて成功。対象は上記の最新コミット。 |
| CI終了日時 | `2026-10-04T02:16:04Z` |
| マージ方式 | Agent mergeをOffにしてAppから手動マージ。 |
| マージ確認 | AppとGitHub Webの両方でMergedを確認。 |
| マージコミット | `59d8ea1af5d0922a2f892c8a9deb365f79f932bf` |
| マージ日時 | `2026-10-04T02:18:15Z` |
| Issueの終了 | Issue #8が`2026-10-04T02:18:17Z`にClosedになった。 |

AppにはCI 3/4の表示が残ったため、本文どおりダイアログを閉じて開き直しました。Successful 4を展開して各ジョブを確認し、手動マージしています。

本章ではローカルの単体テスト、E2E、buildを実行していません。単体テストとE2EはPRのCIで成功しました。初回更新後にローカルで行ったlintと型検査、追加修正後の差分検査は、実施時点を分けた記録です。

## 第4章の計画、実装、品質検査

### Planの開始と承認

| 項目 | 記録 |
| :--- | :--- |
| 対象Issue | [#7 Allow users to filter games by category and publisher](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/7) |
| セッション | `275c65e7-cf14-4eef-a37a-a684c74ef41b` |
| 開始時のHEAD | `59d8ea1af5d0922a2f892c8a9deb365f79f932bf`。第3章のマージ済みmainを継承し、作業ツリーが未変更であることを確認。 |
| 初回プロンプト | 4.2の固定プロンプトをPlanでそのまま送信。あらかじめ入力されていた/issue-fixは置換した。 |
| エージェントの質問 | 複数カテゴリの条件についてA. ORを選び、Continueで回答。 |
| 計画の修正 | 本文のレビュー条件に基づき、Suggest changes to planを1回使用した。 |
| 承認 | A. Approve and implementをクリック。この選択だけで承認が送信された。 |
| 承認後の状態 | Autopilotで初回実装と検査を終えてIdleになった。その後の追加修正依頼でWorkingに戻った。 |
| コミット・PR | まだ作成していない。 |

第4〜6章で使用する作業ディレクトリは次の場所です。

```text
iwizsophy-issue-7-allow-users-to-filter-games-by-category-51494e
```

`tmp/verification-20261004/chapter4-initial-plan-ui.txt`と`tmp/verification-20261004/chapter4-approved-plan-ui.txt`を保存しました。

### 初期Planで補った内容

初期Planに含まれた項目は、出版社の単一選択、カテゴリのOR、出版社とのAND、条件解除、0件表示、静的データ、ヘルパー、アクセシビリティ、テストです。既存の星評価と詳細リンクの維持、具体的な期待値、隔離したE2Eの条件が不足していました。

本文のレビュー条件に従って修正を求めた結果、改訂Planには不足した条件も明記されました。件数だけでなく、残るゲームのタイトルを確認する方針も含まれています。以下は計画の期待値と、その後の確認状況です。自動検査の件数と、個別の手動操作の結果を分けて記録します。

| 検証対象 | Planの期待値 | 実施状況 |
| :--- | :--- | :--- |
| 通常データでStrategyのみ | 4件。該当するタイトルも確認する。 | 手動で4件とタイトル一致を確認。 |
| 通常データでPuzzleのみ | 4件。該当するタイトルも確認する。 | 単独選択の手動確認は未実施。 |
| StrategyとPuzzleをORで組み合わせる | 8件。両カテゴリのタイトルが含まれることを確認する。 | 手動で8件とタイトル一致を確認。 |
| 上記にGitHub GamesをANDで組み合わせる | 2件。出版社とカテゴリの両方に一致するタイトルを確認する。 | 手動で2件とタイトル一致を確認。 |
| 通常データで全解除 | 全21件に戻る。 | 手動で全21件へ戻ることを確認。 |
| 隔離データでPuzzleとNova Interactive | 0件。通常CSVとDBを変更せず、専用CSV、SQLite、別ポートのサーバーを使う。 | 隔離準備の修正後に根拠を再確認する。 |
| 隔離データで条件解除 | テスト用の全3件に戻る。 | 隔離準備の修正後に根拠を再確認する。 |

期待値の確認に使用した通常のdb/games.csvのSHA-256は次の値です。初回実装後にもこの値と一致しました。修正後の再検査でも通常データを維持するために記録しています。

```text
9877F4BF116D993453FB4B1C5626E087F154B7D7CD523A0AB77CABF533CDB6D1
```

### Skillの読取りと未確認事項

実装の進行中に4.5.1のFiles操作を先に行い、quality-checksのSKILL.mdを読みました。Rich textではnameとdescriptionが見えず、Rawで確認しています。

初回実装中の自動検査と4.4の手動操作は、次の表に記録しました。4.5.3の/quality-checksも本文どおり明示的に呼び出し、検査終了とIdleを確認しました。Skillファイルを読んだ段階と、Skillを呼び出して検査した段階を分けて記録しています。

### 初回実装と手動確認

初回実装後にIdleを確認しました。Changesは14ファイル、626行追加、33行削除です。自動検査は成功しましたが、手動確認と差分レビューで修正が必要な点が見つかりました。

| 確認対象 | 初回結果 |
| :--- | :--- |
| 自動検査 | 単体テスト32件、E2E 26件、lint、型検査、build、diff checkが成功。buildは24ページを生成した。 |
| サーバーの起動 | AppのRun development siteから起動し、表示されたhttp://127.0.0.1:4321/を外部ブラウザーで開いた。 |
| カテゴリと出版社 | 21件からStrategy 4件、Puzzle追加で8件、GitHub Games追加で2件となり、表示されたタイトルも一致した。 |
| 全解除 | 全21件に戻った。 |
| 出版社だけの選択 | GitHub Gamesで5件、CodeForgeで6件を確認した。 |
| キーボードのカテゴリ選択 | Spaceでカテゴリを選ぶと4件になった。 |
| 既存の表示 | 星評価とゲーム詳細へのリンクが維持されていた。 |
| 通常CSV | 初回実装後のSHA-256は上記の値と一致した。 |
| サーバーの停止 | Appで停止し、Shell session endedを確認。停止時にポート4321と4322の待ち受けはなかった。 |

### 修正を依頼した問題

| ID | 見つかった問題 | 初回の観測・根拠 | 依頼した修正 | 状況 |
| :--- | :--- | :--- | :--- | :--- |
| F01 | PublisherからのTab移動 | PublisherからTabを押すと、条件解除ではなく最初のゲームリンクへ移動した。資料の操作条件を満たしていなかった。 | キーボードで予定した順序へ移動し、解除操作まで確認できるよう修正する。 | Publisher直後へ解除ボタンを配置。E2Eと主担当の手動再確認で、Tabがclear-game-filtersへ移動し、Enterで21件へ戻ることを確認。 |
| F02 | 隔離準備時のDB指定 | prepare-filter-e2e.tsは、DATABASE_URLが未設定の場合に通常DBへテスト用の3件を読み込む構造だった。 | 通常DBを使わず、隔離したDBを明示して準備と検査を行う。正常な通常21件も維持する。 | DB接続前に未指定と通常DBを拒否するガードを実装。修正後の検査成功を確認。 |
| F03 | 一時DBの後片付け | 初回検査後、サーバーは停止していたが、今回作成した一時DBが4件残っていた。 | 今回の一時DB4件を片付け、検査後にも残さないよう修正する。 | 親プロセスの後片付けを実装。古い一時DB4件を個別に削除し、修正とquality-checks終了時に一時DBと待ち受けがないことを確認。 |
| F04 | E2Eの追加引数 | run-e2e.mjsが追加のargvを転送せず、対象指定を検査へ渡せない。 | 親のnpm実行経路を保ちながら追加引数を転送し、対象を指定して検査する。 | 修正2回目でargv転送を実装。games.spec.tsを指定し、対象10件だけの成功を確認。 |
| F05 | Skillの直接実行例 | Skillにある直接のnpx playwright実行例は、親から渡す環境が必須で、そのままでは失敗する。 | Skillの例を親のnpm経由へそろえ、対象指定と後片付けを確認する。 | 修正2回目でSkillの例を親のnpm経由に変更し、検査と後片付けを確認。 |

F01〜F03をまとめて修正を1回依頼し、修正後のIdleと検査結果を確認しました。その後、本文どおり/quality-checksを送信して再検査しています。残ったF04・F05も2回目の修正で対応し、対象指定の検査と後片付けを確認しました。コミット、push、PR作成、マージは行わない指示を維持しています。

F01〜F05は生成された実装と検証手順の問題です。教材の説明や画面操作で必要な補足とは分けて記録します。第4章では品質検査とAppからのbuildを完了し、ブラウザー操作の検証は同じセッションの第5章へ継続しました。

### 修正1回目とquality-checksの結果

修正1回目では、Publisher直後の解除ボタン、DB接続前のガード、親プロセスによる後片付けを実装したと報告されました。単体38件、E2E 26件、lint、型検査、build、diff checkが成功し、buildは24ページを生成しています。

主担当も修正1回目の終了時にポート4321・4322と一時フォルダーを確認し、待ち受けと一時DBが残っていないことを確認しました。初回に残った一時DB4件は個別に削除されています。

続けて/quality-checksを明示的に送信し、Idleまで確認しました。根拠は`tmp/verification-20261004/chapter4-quality-ui.txt`です。この記録には修正1回目の完了報告も含まれています。

| 明示的なquality-checks | 結果 |
| :--- | :--- |
| 単体テスト | 38件成功。 |
| E2E | 26件成功。フィルター、Publisher→Tab→Enter、0件表示、星評価、詳細リンクを含むと報告された。 |
| lint | 成功。 |
| 型検査 | エラー、警告、ヒントなし。 |
| 差分検査 | git diff --checkが成功。 |
| 後片付け | 一時DBの残存なし。終了時にポート4321・4322が停止していた。 |

検査結果の成功後にも、run-e2e.mjsの追加引数とSkillの直接実行例に問題が残りました。親のnpm経由で対象を指定し、検査と後片付けを確認する2回目の修正を依頼して対応しました。

### 修正2回目とAppからのbuild

run-e2e.mjsは追加のargvを転送する形に修正し、Skillの実行例も親のnpm経由にそろえています。次のコマンドではgames.spec.tsの10件だけが実行され、すべて成功しています。

```text
npm run test:e2e -- e2e-tests/games.spec.ts
```

検査後の一時DBは残らず、ポートの停止、lint、diff checkも成功しました。追加のテスト実装は行わず、対象指定と後片付けの実測で修正を確認しています。

AppのRunからBuild static siteを実際に選択し、24ページ、904msの出力とBuild Completeを確認しました。最終確認の根拠は`tmp/verification-20261004/chapter4-final-ui.txt`です。

第5章でサーバーを起動している間に、主担当が修正後の通常画面を別ブラウザーで再確認しました。初期21件、Strategy・PuzzleとGitHub Gamesの組み合わせで2件を確認。PublisherからTabでclear-game-filtersボタンへ移動し、Enterで全21件へ戻りました。これはMCP操作とは別に行った手動確認です。

## 第5章の管理画面とMCP検証

プロジェクトを右クリックしてSettingsへ進んでも、本文5.2.1にあるMCP serversは見つかりませんでした。SettingsのCustomizeからGo to Customizeを選び、Installedで管理画面へ進みました。

[GitHub公式のAppカスタマイズ説明](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app)も、リポジトリやCopilot CLIで設定したMCP serverがAppで自動的に利用可能になることと、登録済みのサーバーをCustomizeのInstalledで管理することを説明しています。2026年10月4日にこのページを読み、実機の管理画面との対応を確認しました。

| 確認対象 | 結果 |
| :--- | :--- |
| 管理画面の入口 | Customize → Installed |
| Installedの接続表示 | 既存Global PlaywrightのConnectedを確認。準備段階ではGlobalのJustRightも接続表示された。 |
| Playwrightの設定 | TypeはLocal、Commandはnpx、Argumentsは-y @playwright/mcp@latest。設定は変更していない。 |
| リポジトリ定義3件 | 実ファイル.mcp.jsonを確認。githubはHTTPでhttps://api.githubcopilot.com/mcp/へ接続、playwrightはnpx @playwright/mcp@latest、astro-docsはHTTP。個別の接続状態を示すGUIは未確認。 |
| 実際のツール | 初回と補足でNavigate、カテゴリと出版社の選択、Tab・Enter、Shift+Tab、Space、browser_closeを実行して結果を確認。 |
| フィルター検証 | 通常データの組み合わせ、出版社単独、キーボードの選択・解除、隔離3→0→解除3をMCPで確認済み。 |

Globalで確認した既存接続を、リポジトリ定義3件それぞれの接続確認とは扱いません。リポジトリのPlaywright定義には-yがなく、既存Global設定とは引数が異なることも記録しました。設定は変更していません。

第4章と同じセッションとHEADで、5.3の固定プロンプトを全文送信しました。初回はIdleまで進みましたが、履歴のレビューで未確認の操作が見つかったため、補足を依頼しました。補足3条件と後片付けを確認して、第5章のブラウザー検証を完了しています。

### 主担当の独立した確認とMCPの初回結果

| 確認主体 | 接続先・操作 | 確認した結果 | 未確認の範囲 |
| :--- | :--- | :--- | :--- |
| 主担当の別ブラウザー | 通常サイト4321で組み合わせとキーボード解除を再確認。 | 初期21件、組み合わせ2件、PublisherからTabでclear-game-filtersへ移動し、Enterで21件へ戻った。 | MCPによる確認とは別の結果。 |
| 主担当の別ブラウザー | 隔離サイト4322でPuzzleとNova Interactiveを選び、解除。 | 初期3件→0件。No games match the selected filters.と件数0のstatusを確認し、解除で3件へ戻った。 | MCPによる確認とは別の結果として記録。 |
| CopilotのPlaywright MCP・初回 | 通常と隔離データへNavigateし、カテゴリのclick、出版社のselect、Tab・Enter、browser_closeを実行。 | 通常21→4→8→2→21、StrategyとGitHub Gamesで1件からTab・Enterで21件へ解除。隔離3→0→解除3。 | 出版社単独5件・6件とカテゴリSpaceは初回履歴になく、次の補足で確認した。 |

主担当が別ブラウザーで確認できた項目を、CopilotがMCPで実施した項目へ置き換えて報告しません。最終結果では、ツールの履歴、各操作の結果、後片付けをそろえて確認します。

### 初回終了時の片付けと追加レビュー

初回の根拠は`tmp/verification-20261004/chapter5-mcp-ui.txt`です。browser_closeでブラウザーを閉じ、2つのサーバーを停止しました。今回のMCP snapshot 14件と隔離fixtureの一時DBを個別に削除しています。主担当も終了時にポート4321・4322と一時フォルダーを確認し、接続待ちと一時ファイルがないことを確認しました。

初回は「未実施なし」と報告されましたが、出版社単独のGitHub Games 5件、CodeForge Studios 6件、カテゴリをSpaceで選ぶ操作の履歴がありませんでした。5.4の結果レビューに基づき、この3条件だけを実際のMCP操作で補足する指示を1回送りました。件数、タイトル、チェック状態を照合し、初回に実施していない操作と区別して報告するよう依頼しています。

補足は実装を変更せずに行い、実施後のブラウザー、サーバー、一時DBとMCP出力の片付けも依頼しました。初回の全完了という報告だけでは、資料の確認項目をすべて満たしたと判定しません。補足のIdleと各結果を次の表に記録します。

### 補足3条件の実際のMCP結果

最終全文は`tmp/verification-20261004/chapter5-mcp-final-ui.txt`に保存しました。初回に未実施だった3条件を、MCPの実際の選択とキー入力で確認しています。

| 追加した操作 | 実際の結果 |
| :--- | :--- |
| カテゴリ未選択でGitHub Gamesのみ | 5件。Bug Buster Brainteaser、Digital Debugger's Dream、Infrastructure Innovator、Repo Rampart、Server Siege。 |
| カテゴリ未選択でCodeForge Studiosのみ | 6件。Cloud Conqueror、Code Puzzle Chronicles、Code Quest Odyssey、DevOps Dominion、Script Strike、Virtual Server Simulator。 |
| PublisherからShift+TabでStrategyへ移り、Space | checkedとなり4件。DevOps Dominion、Pipeline Conquest、Repo Rulers、Server Siege。 |
| 続けてSpaceで解除 | uncheckedとなり21件。Publisherも未選択。 |

補足後もbrowser_closeを実行し、今回のサーバーを停止してMCP出力を片付けました。主担当の確認でもポート4321・4322の待ち受けはなく、Gitの変更一覧は演習に必要な18ファイルだけで、MCP出力は含まれていませんでした。最後の差分レビューで追加必須の修正はありません。

Appで完了していたbuildのシェルもStopで終了させました。第5章の検証を終え、同じセッションのまま第6章へ進んでいます。

## 第6章のCI確認とAgent Mergeの結果

開始前のmainは59d8ea1af5d0922a2f892c8a9deb365f79f932bfで、APIからprotectedがfalseであることを確認しました。本文6.1の条件が未設定、または分からない場合の経路に従い、Agent mergeをOffにして通常のCreate PRをAppで選択しています。

PR作成後に、最新コミットのCI全4ジョブが成功したことをWebとAPIで確認しました。この確認を終えてから、Ready to merge optionsのAgent mergeスイッチをOffからOnへ切り替えています。

| 項目 | 記録 |
| :--- | :--- |
| PR | [#15 Add category and publisher filters to game catalog](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/15) |
| PRの差分 | 18ファイル、842行追加、36行削除。 |
| 実装コミット | `20d5daaa19c9964c191e4b988764c93477b41295` |
| Author・Committer | `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`で一致。 |
| CI | [実行37173455164](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37173455164)。対象が上記の最新コミットであることを確認し、全4ジョブが成功。 |
| Agent Mergeの開始 | Ready to merge optionsのAgent mergeスイッチをOffからOnへ変更。追加の主ボタンはクリックしていない。 |
| マージ結果 | スイッチ変更から3秒以内にMergedとなった。 |
| Appの確認 | PRペインのMergedとSuccessful 4を確認。 |
| GitHubの確認 | 対象PRのMergedと全4ジョブ成功を確認。 |
| マージコミット | `3acdd179f1a1d88b5a5418035d889071951f5e59` |
| マージ日時 | `2026-10-04T03:16:32Z` |
| Issueの終了 | Issue #7が`2026-10-04T03:16:34Z`にClosedになった。 |
| UIの根拠 | `tmp/verification-20261004/chapter6-final-ui.txt` |

今回のPR作成後の経路では、スイッチをOnにした時点でAgent Mergeが始まり、すぐにマージされました。本文のように選択後に主ボタンをもう一度押す操作はありません。CI全成功を確認する前にスイッチをOnにしないためにも、開始操作の説明を現行画面へ合わせる必要があります。

Address reviews、Fix CI failures、Resolve conflicts、Merge pull requestの四項目メニューの表示は、この実走では確認していません。レビュー対応、CI失敗修復、競合修復も発生していないため、これらの成功を検証済みとは扱いません。通常のPR作成とCI確認を人が行った後、Agent Mergeにマージを任せた範囲までを確認しました。

第7章の新しいworktreeで、第6章のマージコミットから開始したことを確認しました。

## 第7章のCanvas共有、再利用と検索の結果

Projectsを右クリックしてNew sessionを開き、New worktreeとmainを選択しています。開始時のHEADは第6章のマージコミットと一致し、作業ツリーは未変更です。配布資料7.1の固定プロンプトを全文送り、Open Issueを取得するCanvasの初回生成とIdleまでを確認しました。

| 確認対象 | 記録 |
| :--- | :--- |
| セッション | `22f9c4a0-34ba-4414-b700-bbd68ae23e3d` |
| worktree | `iwizsophy-fictional-telegram` |
| ブランチ | `iwizsophy-issue-triage-kanban` |
| 開始時のHEAD | `3acdd179f1a1d88b5a5418035d889071951f5e59` |
| 開始時の作業ツリー | 未変更を確認。 |
| 最初の依頼 | 配布資料7.1の固定プロンプトを全文送信。カードのIssue実装とPR作成は依頼していない。 |
| 保存範囲の質問 | A: project、B: session、C: userが提示された。7.2でprojectへ共有する流れに沿って、今回はB: sessionを選択。 |
| 回答の送信 | B: sessionのクリックで自動送信された。Continueの追加操作はなかった。 |
| セッションの拡張 | `.copilot/session-state/22f9c4a0-34ba-4414-b700-bbd68ae23e3d/extensions/issue-priority-kanban/extension.mjs` |
| 初回の取得エラー | 認証なしAPIの404が発生。初回処理内でgh apiのGETを使う方法へ自動修正された。 |
| CanvasのOpen Issue | #1〜#6の6件。マージ済みの#7と#8は含まれない。 |
| 優先順位の表示 | 上位3件は#5・#2・#1、残りは#6・#3・#4。優先理由の妥当性はレビュー前。 |
| Refresh | 固定配列ではなく、動的に再取得する動作が成功。 |
| 独立したGitHub確認 | Open Issueは#1〜#6の6件で、Canvasの表示対象と一致。#7と#8はClosed。 |
| リポジトリへの影響 | 演習用の実装ファイルに変更はない。`.playwright-mcp`の出力だけが残っている。 |
| 初回の終了 | この時点ではIdleで、コミットとPRは未作成。その後の共有PRとマージは後述。 |

セッションへの保存は、後からprojectへ共有する操作を検証するための今回の選択です。認証方法の変更は初回処理の中で行われており、レビュー後の追加依頼による修正とは分けて記録します。

### 初回画面と本文追加ボタンの実操作

初回Canvasでは白背景にほぼ白い文字が使われ、見出しと優先理由が読みにくい状態でした。[初回の取得エラー](../../_images/verification-20261004/app-20261004-07-canvas-initial-error.jpg)と[初回レイアウト](../../_images/verification-20261004/app-20261004-07-canvas-initial-layout.jpg)は、生成結果とレビュー前の問題を示す根拠として保存済みです。

主担当がIssue #5の本文追加ボタンを1回押し、通知、受領応答、Refresh後の状態を実際に確認しました。対象は[Issue #5](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/5)です。他のカードを追加した結果まで確認済みとは扱いません。

| 確認対象 | 実際の結果 |
| :--- | :--- |
| 会話への追加 | Issue番号、タイトル、URL、受入条件を含む本文全体が1回追加された。 |
| エージェントの応答 | 参照情報として受け取り、調査や実装を開始しない旨の受領応答が1回だけ返った。 |
| Refresh後のボタン | 再取得後もAdded to this sessionの無効状態が保持された。 |
| 再通知の防止 | Refreshしても通知と受領応答は増えていない。 |
| 演習用の実装 | git statusは`.playwright-mcp`の出力だけで、Issueの実装変更はなかった。 |
| 操作の根拠 | `tmp/verification-20261004/chapter7-ack-ui.txt`に本文、受入条件、受領応答、送信済みボタンの状態を保存。 |

### レビュー後の追加修正と確認結果

配色と通知の表現を見直し、今回作成したMCP出力の片付けも追加依頼しました。`tmp/verification-20261004/chapter7-review-followup.txt`には、明暗両テーマのコントラストとフォーカス表示、全文の追加と重複防止の維持、Issueの実装やPR作成を始めずに停止する条件を記録しています。

通知の先頭は、追加の命令から、Issueが現在の会話に参照情報として追加された事実を伝える文へ修正されました。Appの実際のPlaywright MCP履歴で、明暗両テーマのcomputedStyleによるコントラストとTab移動時のoutlineの検査を確認しています。`tmp/verification-20261004/chapter7-review-ui.txt`には修正完了の応答とIdleを保存しました。

| 検査対象 | Light | Dark |
| :--- | ---: | ---: |
| 本文のコントラスト比 | 15.80:1 | 17.39:1 |
| ボタンのコントラスト比 | 14.84:1 | 13.98:1 |
| リンクのコントラスト比 | 7.59:1 | 9.73:1 |
| Tab移動時のoutline | 3px | 3px |

修正後は主担当がIssue #6のボタンを1回押して確認しました。事実を伝える通知に続いて番号、タイトル、URL、受入条件を含む本文全体が1回追加され、受領のみの応答も1回です。Refresh後も#5と#6のボタンはAdded to this sessionの無効状態を保ち、通知と応答は増えていません。`tmp/verification-20261004/chapter7-receipt-ui.txt`に修正後の通知、本文、受領応答を保存しています。

主担当の確認でもリポジトリは未変更で、今回のMCP一時出力は0件でした。Issueの実装、コミット、push、PR作成は、このCanvasの修正とボタン確認では行っていません。[修正後のCanvas](../../_images/verification-20261004/app-20261004-07-canvas-readable.jpg)を掲載候補として取得しました。[受領応答の画像](../../_images/verification-20261004/app-20261004-07-canvas-receipt.jpg)はRefresh途中のFetchingを含むため、教材へ掲載する場合は会話部分を切り出すなど、掲載範囲の確認が必要です。

### project共有の初回結果と追加レビュー

7.2の固定プロンプトで、Canvasと再利用手順をリポジトリへ保存しました。初回の共有結果は`tmp/verification-20261004/chapter7-shared-initial-ui.txt`に記録しています。

| 確認対象 | 初回の共有結果 |
| :--- | :--- |
| 保存したファイル | `.github/extensions/priority-kanban/extension.mjs`とREADMEの2ファイル。 |
| 初回の差分 | 543行追加、5行削除。Canvasと再利用手順の範囲。 |
| 検査 | 構文検査と差分検査が成功。PRのCIはまだ実行していない。 |
| 一覧とRefresh | 最新のOpen Issue 6件を取得し、全カードの番号、タイトル、URL、本文全体、追加ボタンを確認。Refreshの再取得も成功。 |
| #1の本文追加 | Playwright MCPで1回追加。重複送信はAPIで遮断され、Refresh後も追加済みボタンの無効状態が保持された。 |
| 初回の受領確認 | 非同期の送信APIのため、エージェントは初回報告で実際の受領応答を未確認と明記した。 |
| その後の受領確認 | 次のターンで主担当が、Issue #1を現在の会話の参照情報として受領する応答が1回だけ返ったことを実際に確認。 |
| PR | 初回の共有時点では未作成。 |

共有化のレビューでは、同じセッションの送信済み状態を引き継がない問題が見つかりました。初回の共有版を実ファイルで確認したところ、旧セッション版のissue-priority-kanbanに#5と#6、共有版のpriority-kanbanに#1が保存され、共有版は旧状態を読み込んでいませんでした。このため、同じ会話にすでに追加した#5と#6の再送を防げない構造でした。実際に#5と#6を再送して確認する操作は行っていません。

`tmp/verification-20261004/chapter7-shared-review-followup.txt`で、同じセッションの送信済み番号[1,5,6]を安全に統合し、別セッションではそのセッション自身の状態を使うよう追加依頼しました。確認には状態の読み取りとボタンの無効表示を使い、#1、#5、#6を再通知しない条件も指定しています。

追加修正は完了し、`tmp/verification-20261004/chapter7-shared-review-ui.txt`に結果を保存しました。確認した範囲は次のとおりです。

| 確認対象 | 修正後の結果 |
| :--- | :--- |
| 共有用の送信済み状態 | 同じセッションの新旧状態を統合し、実際の保存内容とAPI応答は[1,5,6]。 |
| 旧セッション版の状態 | [5,6]のまま保持され、旧ファイルを書き換えていない。 |
| 主担当の画面確認 | #1、#5、#6の3件で追加ボタンが無効。 |
| Refresh後のMCP確認 | Open 6件を再取得しても3件の無効状態が保持され、再送は行われていない。 |
| 検査と後片付け | 構文検査と差分検査が成功。今回のMCP一時出力は0件。 |
| 共有レビュー終了時の差分 | CanvasとREADMEの2ファイル、555行追加、1行削除。PR作成中の追加修正後は556行追加、1行削除。 |
| 別セッションの確認 | 共有レビュー終了時点では実表示と追加操作は未確認だった。その後、7.3で再利用と本文追加、状態の分離を確認。 |

共有版のレビューでは、追加の必須修正は残っていません。[Canvasの差分](../../_images/verification-20261004/app-20261004-07-changes-canvas.jpg)を取得済みです。その後の通常のCreate PRで追加修正と検査が行われ、以下の確定したPRとマージ結果につながっています。

### 共有版のPR、CI、Agent Mergeと更新承認

Appの通常のCreate PRを使用しました。作成処理で補助Issue #16が自動作成され、lintに基づくCanvasの追加修正と再検査も行われています。共有レビュー時点の555行追加から、PRの確定差分は556行追加に変わりました。

| 項目 | 記録 |
| :--- | :--- |
| PR | [#17](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/17) |
| 確定差分 | CanvasとREADMEの2ファイル、556行追加、1行削除。 |
| 実装コミット | `f5a8a2ed2d859c61f6c01b83bf13a10e61e6d11f` |
| Author・Committer | `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>`で一致。 |
| Appの作成処理での検査 | lint、単体テスト38件、24ページのbuild、E2E 26件、構文検査、差分検査が成功。 |
| CI | [実行37175377043](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37175377043)。対象が上記の最新コミットであることを確認し、全4ジョブが成功。 |
| CIの照合 | 主担当がAPI、GitHub Web、AppのSuccessful 4を照合。Appの古い3/4表示は閉じて開き直した。 |
| Agent Merge | OffのスイッチをOnにすると数秒でMerged。追加の主ボタンはクリックしていない。 |
| マージコミット | `aa74cee0eb29edfcbc52e83ab60d1dfd85c6e1ee` |
| マージ日時 | `2026-10-04T03:58:52Z` |
| 補助Issue | [#16 Share the Priority Kanban canvas across project sessions](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/16)。`2026-10-04T03:58:53Z`にClosed。 |
| マージの照合 | AppとGitHub Webの両方でMergedを確認。 |

PR作成で補助Issue #16がOpenとなった期間は、元の未完了課題6件に補助Issue 1件が加わります。マージ後に#16はClosedとなりました。Canvasの一覧では、演習用Issueとこの一時的な補助Issueを取り違えず、実際のOpen一覧との一致で判断します。

Agent merge actionsのメニューは一瞬表示されましたが、四項目を個別には確認していません。今回もCI全成功を人が確認してから、スイッチをOnにしてマージする経路を検証した範囲です。

更新内容の承認ではReview repository contentを開き、ダイアログの`.github/extensions/database-explorer`、`priority-kanban`、scriptsを実ファイルと照合してから、Accept for new sessionsを完了しました。[承認画面](../../_images/verification-20261004/app-20261004-07-canvas-trust.jpg)を保存しています。

### 別セッションでの再利用と検索Issueの受領

共有版のマージ後、別の新しいセッションを最新mainから開始しました。7.3の固定プロンプトで共有Canvasを開き、Open Issue 6件と6件の有効な追加ボタンを確認しています。主担当がIssue #1のボタンを1回押して、本文追加と受領を実際に確認しました。

| 確認対象 | 結果 |
| :--- | :--- |
| 新しいセッション | `166614fd-22b1-4372-85f4-9fe693468948` |
| worktreeと開始時のブランチ | `iwizsophy-musical-guacamole` |
| 開始時のHEAD | `aa74cee0eb29edfcbc52e83ab60d1dfd85c6e1ee` |
| 再利用したCanvas | リポジトリ共有版。Open Issueは#1〜#6の6件で、最初は6件の本文追加ボタンが有効。 |
| #1の本文追加 | 番号、タイトル、URL、受入条件を含む本文全体が1回通知された。 |
| 受領応答 | 参照情報を受領した旨の応答が1回だけ返った。 |
| 新しいセッションの状態 | 本文追加後は[1]。 |
| 元のセッションの状態 | [1,5,6]を保持し、新しいセッションの状態と分離されている。 |
| リポジトリと実装の確認 | 作業ツリーは未変更。7.4の承認前に検索などの実装は始まっていない。 |
| 操作の根拠 | `tmp/verification-20261004/chapter7-reopened-ack-ui.txt`に再利用と受領の結果を保存。 |

これにより、同じセッションの重複防止と、別セッションで同じIssueを改めて受け取る操作の両方を確認できました。検索Issueの受領は参照情報の追加までで、検索機能の実装成功とは扱いません。

### 検索機能のPlanと承認

7.4の固定プロンプトをPlanモードで送り、作成したPlanを全文レビューしました。Clear filtersで検索語も解除するかという質問には、既定のA: はいを選び、Continueで回答しています。`tmp/verification-20261004/chapter7-search-plan-ui.txt`に計画と質問の結果を保存しました。

Planでは、既存の静的な21件のカードとクライアント側フィルターの同じ層に検索を加える理由を示しています。DBのgetAllGamesと星評価を維持し、カテゴリ内のOR条件も保ったうえで、検索、カテゴリ、出版社をAND条件で組み合わせる構成です。

| Planの確認対象 | 記載内容 |
| :--- | :--- |
| 検索判定 | `src/lib/game-search.ts`に純粋な`matchesGameTitle(title, query)`を作成。 |
| 文字列の処理 | trim、小文字化、部分一致、空文字列の扱い。 |
| 既存機能 | 全21件の静的カード、カテゴリ内のOR、検索・カテゴリ・出版社のAND、星評価、DBのgetAllGamesを維持。 |
| キーボード操作 | 検索の入力、解除、Clear filtersですべて解除する動作。 |
| 承認前の確認 | ブランチは`iwizsophy-game-title-search`へ変更されたが、演習用の実装はまだ始まっていない。 |
| 承認操作 | Approve and implementを1回クリックすると即座にAutopilotへ移行し、Workingで実装を開始。追加の開始指示は送っていない。 |

次の件数とタイトルはPlanの期待値で、実装後の確認結果ではありません。タイトルは実際のデータに合わせ、単語間の空白も含めて記録しています。

| Planで検査する条件 | 期待件数 | 期待タイトル |
| :--- | ---: | :--- |
| `devops dominion`の検索 | 1 | DevOps Dominion |
| 前後の空白を含むServer Siegeの検索 | 1 | Server Siege |
| repoの検索 | 2 | Repo Rampart、Repo Rulers |
| no-such-titleの検索 | 0 | なし。 |
| repo、Action、GitHub Gamesの組み合わせ | 1 | Repo Rampart |

### 検索実装と自動検査の結果

検索実装の初回処理はIdleで完了しました。`tmp/verification-20261004/chapter7-search-implementation-ui.txt`に結果を保存し、主担当がChangesで検索入力のlabel、input、0件の文面を確認しています。差分レビューでは追加の必須修正は残っていません。

| 確認対象 | 実装完了時の結果 |
| :--- | :--- |
| 差分 | 5ファイル、149行追加、5行削除。 |
| 検索判定 | 実装の純粋なhelperをブラウザーと単体テストで共有している。 |
| 条件の組み合わせ | カテゴリ内のORを維持し、検索、カテゴリ、出版社をANDで組み合わせる。 |
| 既存機能とデータ | 星評価と詳細リンク、通常CSV、テスト用fixtureを維持。通常CSVのハッシュ一致も確認。 |
| 単体テスト | 44件成功。 |
| E2E | 29件成功。 |
| その他の自動検査 | lint、型検査、24ページのbuild、差分検査が成功。 |
| 一時DB | 残存0件を確認。 |
| 画面の差分 | [07-changes-search.jpg](../../_images/verification-20261004/app-20261004-07-changes-search.jpg)を取得。 |

この段階の完了は、実装の差分と自動検査の結果までです。本文で求めるブラウザーの操作結果は、次のPlaywright MCP検証で確認します。

### 検索のPlaywright MCP検証の結果

7.5には固定プロンプトがないため、本文の確認条件を`tmp/verification-20261004/chapter7-search-mcp-followup.txt`で追加依頼しました。実行済みの単体テスト、E2E、lint、型検査は結果と件数を照合し、未実施の必須検査がある場合だけquality-checksで補う条件です。最終結果は`tmp/verification-20261004/chapter7-search-mcp-ui.txt`に保存しています。

開発サーバーのURLは`http://127.0.0.1:4321/`です。MCPの最終結果メッセージでは、次の操作結果が報告されました。主担当の独立した画面確認と区別して記録します。

| MCPで報告された条件 | 報告された結果 |
| :--- | :--- |
| 通常の一覧 | 21件。 |
| sErVeRの検索 | Server SiegeとVirtual Server Simulatorの2件。 |
| 前後の空白を含むsErVeRの検索 | 同じ2件。 |
| 検索、Strategy、GitHub GamesのAND | Server Siegeの1件。 |
| 存在しない検索語 | 0件の説明と結果通知を表示。 |
| キーボードで入力し、PublisherからTab、Clear filtersでEnter | 検索語、カテゴリ、出版社をすべて解除し、21件へ戻る。 |
| Server Siegeのカード | 星評価3.3と詳細リンクのhref`/game/3`を維持。 |
| Virtual Server Simulatorのカード | 星評価3.7と詳細リンクのhref`/game/9`を維持。 |

最終結果メッセージが挙げたMCPツールは、`playwright-browser_navigate`、`playwright-browser_snapshot`、`playwright-browser_find`、`playwright-browser_click`、`playwright-browser_type`、`playwright-browser_evaluate`、`playwright-browser_press_key`、`playwright-browser_fill_form`、`playwright-browser_select_option`、`playwright-browser_close`です。主担当が直接確認した実際のNavigate履歴と、結果メッセージに記載された一覧を区別します。ほかの列挙したツールすべてを個別の履歴で照合したとは扱いません。

MCPでは詳細リンクのhrefを確認し、リンクをクリックして詳細画面へ移る操作は行っていません。この点は最終報告でも未実施と明記されています。E2Eの詳細ページ遷移は成功しているため、MCPの手動操作と自動検査で確認した範囲を分けて記録します。

主担当も別のブラウザーで同じ件数とタイトル、星評価、href、Tab移動時のフォーカス、Enterでの解除を独立に確認しました。取得した[初期状態](../../_images/verification-20261004/app-20261004-07-search-default.jpg)、[検索2件](../../_images/verification-20261004/app-20261004-07-search-two.jpg)、[AND条件の1件](../../_images/verification-20261004/app-20261004-07-search-combined.jpg)、[0件表示](../../_images/verification-20261004/app-20261004-07-search-zero.jpg)は、主担当の別ブラウザーでの結果です。CopilotがMCPで取得した画像とは扱いません。

後片付けは、エージェントのbrowser_close、サーバー停止、一時DBとMCP出力の削除の報告後に、主担当も独立に確認しました。4321と4322の待受はなく、title-search-manual.dbもありません。`.playwright-mcp`は空のフォルダーだけが残り、出力ファイルは0件です。通常CSVのハッシュは第4章の記録と一致し、差分検査も成功。演習用の変更は検索の5ファイルだけでした。

### 検索PRのCI、Agent MergeとCanvasのRefresh

| 項目 | 確認結果 |
| :--- | :--- |
| PR | [#18](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/18)。Closes #1。 |
| 確定差分 | 5ファイル、149行追加、5行削除。 |
| 実装コミット | `f516e73ebdf5f61c8d3e9ea7fd0532ec271ad081` |
| CI | [実行37177105230](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/actions/runs/37177105230)。対象が上記の最新コミットであることを確認し、全4ジョブが成功。 |
| CIの照合 | App、GitHub Web、APIで全成功を照合。 |
| Agent Merge | OffからOnへ切り替えると即座にMerged。 |
| マージコミット | `566da7b02aa0319bba6c6ee67d088e8f84165151` |
| マージ日時 | `2026-10-04T04:32:50Z` |
| Issueの終了 | Issue #1が`2026-10-04T04:32:51Z`にClosed。 |
| マージの照合 | AppとGitHub WebでMergedを確認。 |
| Refresh後のOpen Issue | #2〜#6の5件。マージ済みの#1が除外された。 |
| Refresh後の優先表示 | 上位は#5・#2・#6、残りは#3・#4。 |
| Canvasのstatus | 5 open、画面の更新時刻13:34:39。 |
| Refreshの根拠 | `tmp/verification-20261004/chapter7-canvas-after-search-ui.txt`と[マージ後のCanvas](../../_images/verification-20261004/app-20261004-07-canvas-after-search-merge.jpg)。 |

第7章は、共有と再利用、検索実装のレビューとMCP結果の照合、最新CI全成功後のマージ、課題一覧の更新まで完了しました。MCPでの詳細リンクのクリック遷移、四項目のAgent merge actionsの個別表示、発生しなかったCIと競合の修復は、検証済みと扱いません。第8章の実行と照合結果は次のとおりです。

## 第8章のManual・Local自動化と結果の照合

New Automationで「Recap my recent work 20261004」を作成しました。配布資料8.1の固定プロンプトは一字も変更せず、読み取りと会話内の報告だけを依頼しています。Manual、Run in the cloudをOff、今回の演習用コピー、新しいworktreeを選び、Create and runを実行しました。

| 項目 | 実行記録 |
| :--- | :--- |
| 自動化名 | Recap my recent work 20261004 |
| 実行方法 | Manual、Local。Run in the cloudはOff。 |
| workflow ID | `47282f5e-eacc-4a01-abbe-9feedcd1f9c6` |
| run ID | `3a13945d-b1a6-414b-b7ec-cb1a14c2f8bd` |
| Recent runs | 画面はLocalと緑の成功アイコン、時刻13:37、実行時間53秒。AXでもSucceededを確認。 |
| worktreeとブランチ | `iwizsophy-ideal-adventure` |
| 終了時のHEAD | `566da7b02aa0319bba6c6ee67d088e8f84165151` |
| 対象リポジトリ | `iwizsophy/dev-days-tailspin-participant-check-20261004` |
| 取得時点 | 2026-10-04 13:37:58 JST、UTC+09:00。 |
| 集計期間 | 2026-09-27 13:37:58〜2026-10-04 13:37:58 JSTの直近7日間。 |
| 結果の根拠 | `tmp/verification-20261004/chapter8-automation-ui.txt` |
| ツール履歴の根拠 | `tmp/verification-20261004/chapter8-automation-tools-ui.txt` |

### 報告されたPRとIssue

期間内にマージされたPRは5件で、報告件数と一覧が一致しました。主担当がGitHub APIから独立に取得した番号、タイトル、URL、マージ日時も全5件で一致しています。検索PR #18を含む結果です。

| 番号 | PRのタイトルとURL | マージ日時、JST |
| :--- | :--- | :--- |
| #18 | [Add title search to the game catalog](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/18) | 2026-10-04 13:32:50 |
| #17 | [Share Priority Kanban across project sessions](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/17) | 2026-10-04 12:58:52 |
| #15 | [Add category and publisher filters to game catalog](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/15) | 2026-10-04 12:16:32 |
| #14 | [Update repository coding standards](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/14) | 2026-10-04 11:18:15 |
| #13 | [Show game ratings on cards](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/pull/13) | 2026-10-04 10:42:16 |

Open Issueは5件で、番号、タイトル、URL、状態も主担当のAPI照合と全5件で一致しています。マージ済みの検索Issue #1は含まれていません。

| 番号 | IssueのタイトルとURL | 状態 |
| :--- | :--- | :--- |
| #6 | [Implement pagination on the game list page](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/6) | Open |
| #5 | [Show a catalog summary on the home page](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/5) | Open |
| #4 | [Add a publisher page listing that publisher's games](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/4) | Open |
| #3 | [Show category and publisher descriptions on the game detail page](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/3) | Open |
| #2 | [Allow users to sort the game list](https://github.com/iwizsophy/dev-days-tailspin-participant-check-20261004/issues/2) | Open |

### 読み取りだけで完了したことの確認

実際のツール履歴は4件です。`gh repo view`、期間とマージ時刻を指定する`gh pr list`、現在Openを取得する`gh issue list`、JustRightの校正だけで完了しました。PRの取得はlimit 100、Issueの取得はlimit 1000で、対象期間と状態はツール引数にも明示されています。

主担当の独立確認でもmainは変わらず、今回の全10件のIssueのコメント数は0件、更新時刻は自動化前の演習終了時と同じでした。自動化のworktreeはtrackedとuntrackedの変更がなく、セットアップの自動生成物と演習内容の変更を区別して確認しています。

自動化の報告は対象リポジトリ、取得時点、タイムゾーン、期間、件数と一覧を含み、その対象データの未確認情報はないと記載しました。主担当の照合により、このPR 5件とOpen Issue 5件の報告内容を確認できたため、第8章は完了と判定します。継続的なスケジュール実行やクラウド実行は、今回のManual・Localの検証範囲には含めていません。

## 補足操作と教材の修正候補

| ID | 該当箇所 | 観測した内容 | 修正候補 | 状況 |
| :--- | :--- | :--- | :--- | :--- |
| R01 | 1.3 課題一覧 | Projectsでコピーを選んでも、Issues上部には旧コピーの指定が残った。 | Issues上部で対象リポジトリを確認し、演習用コピーだけを選ぶ操作を示す。操作の意図は、別のコピーの課題に指示を出さないためと説明する。 | 原稿への反映は未実施。 |
| R02 | 1.3 ビューの作成 | 狭い表示でIssue詳細が開いていると、New viewの入口が見えなかった。詳細を閉じると作成できた。 | New viewが見えない場合は、右側のIssue詳細を閉じる案内を補う。 | 原稿への反映は未実施。 |
| R03 | 3.2 applyTo、4.5.1 Skillの冒頭 | Rich textではapplyToやSkillのname・descriptionが表示されず、Rawで確認できた。 | ファイル冒頭のメタデータを読む前にRawへ切り替える操作を追加する。指示の適用対象やSkillの使用条件を本文と分けて確認する理由も保つ。 | 原稿への反映は未実施。 |
| R04 | 3.2 隠しファイルの表示 | 実機の項目名はShow all hidden filesとShow tracked hidden filesだった。 | 本文のShow hidden filesを現行の項目名に合わせ、`.github`を表示する手順を示す。 | 原稿への反映は未実施。 |
| R05 | 3.3・4.2 プロンプトの入力 | Issueから開始した入力欄に、/issue-fixがあらかじめ入っていた。 | 既存の入力を全選択して固定プロンプトへ置き換える操作を補う。初回指示を同じ条件で送るためと説明する。 | 原稿への反映は未実施。 |
| R06 | 5.2.1 MCPの既存設定 | Project SettingsにMCP serversがなかった。実機の管理経路はCustomize → Installedで、公式説明も同じだった。 | MCPの管理経路を現行画面に合わせる。Globalの接続表示とリポジトリ定義の確認を区別し、実際のツール操作まで確認する説明を保つ。根拠は[GitHub公式](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app)。 | 原稿への反映は未実施。 |
| R07 | 6.2 PR作成後のAgent Merge | Ready to merge optionsのAgent mergeスイッチをOnにしただけで開始し、3秒以内にマージされた。追加の主ボタン操作はなく、四項目の権限メニューは未確認。 | PR作成後の経路は現行スイッチの操作で説明する。Onで即時に開始するため、CI全成功の確認を先に行う理由を保つ。確認していない権限メニューや修復機能を実走済みと説明しない。 | 原稿への反映は未実施。 |

レビューによる追加修正は、本文で求める確認条件に基づく操作です。初回の生成結果、必要だった指示、再試行の結果を分けて記録しました。画面の項目名や入口が変わった箇所は、上記のR01〜R07として原稿の修正候補にしています。

## 画面の取得と掲載判断

掲載箇所ごとの候補は[画像対応表](verification-images-20261004.md)のとおりです。既存画像の差し替え、追加する画面、重複掲載の削除候補を掲載箇所ごとに判断します。

以下は取得した撮影ファイルと用途の記録です。掲載候補と検証記録を分け、対象リポジトリ、課題、作業モード、表示結果が合う画像を選ぶ判断材料として残しました。

| 取得ファイル | 対応する内容 | 掲載判断 |
| :--- | :--- | :--- |
| [00-template-menu.jpg](../../_images/verification-20261004/app-20261004-00-template-menu.jpg) | 教材用テンプレートのコピー作成入口。 | 差し替え候補。公開時の表示との整合を確認する。 |
| [00-template-form-top.jpg](../../_images/verification-20261004/app-20261004-00-template-form-top.jpg) | コピー作成時のテンプレート、名前、設定。 | 差し替え候補。必要な設定が読める範囲を選ぶ。 |
| [00-repository-created.jpg](../../_images/verification-20261004/app-20261004-00-repository-created.jpg) | 新しいコピーの作成結果。 | 検証の根拠として取得済み。本文への追加要否は未判定。 |
| [00-bootstrap-issues.jpg](../../_images/verification-20261004/app-20261004-00-bootstrap-issues.jpg) | 初期設定後の課題一覧。 | 追加候補。8件の表示と対象コピーを確認する。 |
| [01-repository-trust.jpg](../../_images/verification-20261004/app-20261004-01-repository-trust.jpg) | リポジトリ内容の確認と承認。 | 追加候補。本文に必要な画面範囲を確認する。 |
| [01-issues-assigned-empty.jpg](../../_images/verification-20261004/app-20261004-01-issues-assigned-empty.jpg) | Assigned to meに課題が表示されない状態。 | 追加候補。ビューを作る理由と対応するか確認する。 |
| [01-issues-new-view.jpg](../../_images/verification-20261004/app-20261004-01-issues-new-view.jpg) | State: Openのビュー作成。 | 追加候補。New view、検索条件、Saveが読めるか確認する。 |
| [01-quick-chat-complete.jpg](../../_images/verification-20261004/app-20261004-01-quick-chat-complete.jpg) | Quick Chatの説明と完了状態。 | 検証の根拠として取得済み。本文への追加要否は未判定。 |
| [02-new-session.jpg](../../_images/verification-20261004/app-20261004-02-new-session.jpg) | New worktree、main、Interactiveの開始条件。 | 差し替え候補。開始条件が読めるか確認する。 |
| [02-environment-output.jpg](../../_images/verification-20261004/app-20261004-02-environment-output.jpg) | セッション内のNode.jsと作業場所の確認。 | 検証の根拠として取得済み。本文への追加要否は未判定。 |
| [02-changes-game-card.jpg](../../_images/verification-20261004/app-20261004-02-changes-game-card.jpg) | GameCardの星評価の差分。 | 星評価と関係のない既存Changes画像の差し替え候補。 |
| [02-changes-render-tests.jpg](../../_images/verification-20261004/app-20261004-02-changes-render-tests.jpg) | 実際のGameCardを使うレンダリング検査の差分。 | テストを確認する画面の追加候補。 |
| [02-run-menu.jpg](../../_images/verification-20261004/app-20261004-02-run-menu.jpg) | Run development siteの起動入口。 | 既存Runメニュー画像の差し替え候補。 |
| [02-star-rating.jpg](../../_images/verification-20261004/app-20261004-02-star-rating.jpg) | 通常データの星評価付きカード。 | 既存の完成例の差し替え候補。 |
| [02-game-detail.jpg](../../_images/verification-20261004/app-20261004-02-game-detail.jpg) | カードから移動したゲーム詳細。 | リンク動作の根拠として取得済み。本文への追加要否は未判定。 |
| [02-run-stopped.jpg](../../_images/verification-20261004/app-20261004-02-run-stopped.jpg) | Stop後のShell session ended。 | サーバーの停止確認を示す画面の追加候補。 |
| [02-pr-ci-running.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-running.jpg) | Ready to mergeが表示され、CIが進行中の状態。 | ボタン表示とCIの完了を区別する画面の追加候補。 |
| [02-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-passed.jpg) | AppでのCI全成功の表示。 | マージ前に確認する画面の追加候補。 |
| [02-pr-checks-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-checks-passed.jpg) | GitHub WebでのCI全成功の表示。 | Appの表示との照合の根拠として取得済み。本文への追加要否は未判定。 |
| [02-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-02-pr-merged-app.jpg) | AppのMerged表示。 | マージ完了を示す画面の追加候補。 |
| [02-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-02-pr-merged-github.jpg) | GitHub WebのMerged表示。 | Appの表示との照合の根拠として取得済み。本文への追加要否は未判定。 |
| [03-add-tab-files.jpg](../../_images/verification-20261004/app-20261004-03-add-tab-files.jpg) | Add tabからFilesを開く入口。 | 第3章の既存Add tab画像の差し替え候補。 |
| [03-file-search.jpg](../../_images/verification-20261004/app-20261004-03-file-search.jpg) | copilot-instructions.mdのファイル検索。 | 既存Go to file画像の差し替え候補。 |
| [03-files-options.jpg](../../_images/verification-20261004/app-20261004-03-files-options.jpg) | 現行の隠しファイル表示設定。 | 旧Show hidden filesの画像の差し替え候補。 |
| [03-unit-test-instructions.jpg](../../_images/verification-20261004/app-20261004-03-unit-test-instructions.jpg) | 単体テストのパス固有指示の本文。 | 指示の内容を確認した根拠として取得済み。本文への追加要否は未判定。 |
| [03-unit-test-applyto.jpg](../../_images/verification-20261004/app-20261004-03-unit-test-applyto.jpg) | Rawで確認したapplyTo。 | 適用対象を読む操作を示す画面の追加候補。 |
| [03-drizzle-links.jpg](../../_images/verification-20261004/app-20261004-03-drizzle-links.jpg) | Drizzle指示の相対リンク。 | 指示ファイルの関係を確認した根拠として取得済み。本文への追加要否は未判定。 |
| [03-drizzle-links-final.jpg](../../_images/verification-20261004/app-20261004-03-drizzle-links-final.jpg) | 更新後のDrizzle指示と参照リンク。 | 第3章の指示ファイルの関係を示す追加候補。掲載は更新後の画像を優先する。 |
| [03-issue-details.jpg](../../_images/verification-20261004/app-20261004-03-issue-details.jpg) | 規約更新のIssue #8の詳細。 | 別課題を示す既存Issue画像の差し替え候補。 |
| [03-changes-instructions.jpg](../../_images/verification-20261004/app-20261004-03-changes-instructions.jpg) | 指示ファイルの差分。 | 第3章の既存Changes画像の差し替え候補。 |
| [03-code-example.jpg](../../_images/verification-20261004/app-20261004-03-code-example.jpg) | Publishersを返すコード例の応答。 | 目的、引数、戻り値をレビューする画面の追加候補。 |
| [03-pr-ci-running.jpg](../../_images/verification-20261004/app-20261004-03-pr-ci-running.jpg) | Appに残ったCI 3/4の表示。 | 表示を開き直して確認する根拠として取得済み。本文への追加要否は未判定。 |
| [03-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-03-pr-ci-passed.jpg) | Successful 4のジョブ一覧。 | 第3章のマージ前確認を示す画面の追加候補。 |
| [03-pr-checks-passed.jpg](../../_images/verification-20261004/app-20261004-03-pr-checks-passed.jpg) | GitHub WebでのCI全成功。 | Appの表示との照合の根拠として取得済み。本文への追加要否は未判定。 |
| [03-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-03-pr-merged-app.jpg) | AppのMerged表示。 | 第3章のマージ完了を示す画面の追加候補。 |
| [03-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-03-pr-merged-github.jpg) | GitHub WebのMerged表示。 | Appの表示との照合の根拠として取得済み。本文への追加要否は未判定。 |
| [04-issue-details.jpg](../../_images/verification-20261004/app-20261004-04-issue-details.jpg) | フィルター機能のIssue #7の詳細。 | 別課題を示す既存Issue画像の差し替え候補。 |
| [04-plan-mode.jpg](../../_images/verification-20261004/app-20261004-04-plan-mode.jpg) | Planのモード選択。 | 第4章の既存モード選択画像の差し替え候補。 |
| [04-plan-question.jpg](../../_images/verification-20261004/app-20261004-04-plan-question.jpg) | OR条件を選ぶ質問とContinue。 | 仕様を判断して回答する画面の追加候補。 |
| [04-plan-review-initial.jpg](../../_images/verification-20261004/app-20261004-04-plan-review-initial.jpg) | 修正前のPlan。 | 計画レビューの根拠として取得済み。本文への追加要否は未判定。 |
| [04-plan-review.jpg](../../_images/verification-20261004/app-20261004-04-plan-review.jpg) | 修正後のPlanと承認の入口。 | 第4章の既存Plan承認画像の差し替え候補。 |
| [04-quality-skill.jpg](../../_images/verification-20261004/app-20261004-04-quality-skill.jpg) | Rawで読むquality-checksのnameとdescription。 | Skillのメタデータを確認する画面の追加候補。 |
| [04-changes-filters.jpg](../../_images/verification-20261004/app-20261004-04-changes-filters.jpg) | 初回フィルター実装のChanges。 | 第4章の既存Changes画像の差し替え候補。修正後の差分も確認してから採用する。 |
| [04-filter-default.jpg](../../_images/verification-20261004/app-20261004-04-filter-default.jpg) | 初回実装の通常21件の一覧とフィルター。 | 初回確認の根拠として保管。掲載は修正後の画像を優先する。 |
| [04-filter-combined.jpg](../../_images/verification-20261004/app-20261004-04-filter-combined.jpg) | 初回実装のカテゴリと出版社を組み合わせた表示。 | 初回確認の根拠として保管。掲載は修正後の画像を優先する。 |
| [04-run-stopped.jpg](../../_images/verification-20261004/app-20261004-04-run-stopped.jpg) | Run停止後のShell session ended。 | 停止確認の根拠として取得済み。本文への追加要否は未判定。 |
| [04-run-menu.jpg](../../_images/verification-20261004/app-20261004-04-run-menu.jpg) | AppのRunからBuild static siteを選ぶ入口。 | 第4章の既存Run画像の差し替え候補。 |
| [04-build-complete.jpg](../../_images/verification-20261004/app-20261004-04-build-complete.jpg) | 24ページの出力とBuild Complete。 | Skillの検査とは別にbuildを確認する画面の追加候補。 |
| [04-filter-default-final.jpg](../../_images/verification-20261004/app-20261004-04-filter-default-final.jpg) | 修正後の通常21件の一覧とフィルター。 | 最終の初期状態を示す画面の追加候補。 |
| [04-filter-combined-final.jpg](../../_images/verification-20261004/app-20261004-04-filter-combined-final.jpg) | 修正後のカテゴリと出版社を組み合わせた2件。 | 最終のORとANDの操作結果を示す画面の追加候補。 |
| [05-isolated-three.jpg](../../_images/verification-20261004/app-20261004-05-isolated-three.jpg) | 主担当が別ブラウザーで確認した隔離データ3件。 | 通常21件とは別のテスト環境を示す画面の追加候補。 |
| [05-isolated-zero.jpg](../../_images/verification-20261004/app-20261004-05-isolated-zero.jpg) | 主担当が確認した隔離データの0件表示。 | 0件の説明と件数通知を示す画面の追加候補。 |
| [05-mcp-result-combined.jpg](../../_images/verification-20261004/app-20261004-05-mcp-result-combined.jpg) | Copilotの実際のMCP結果で2件とタイトルを確認。 | 操作の根拠を示す画面の追加候補。主担当の別ブラウザー画像と区別する。 |
| [05-mcp-installed.jpg](../../_images/verification-20261004/app-20261004-05-mcp-installed.jpg) | CustomizeのInstalledにあるGlobalのMCP接続表示。 | 現行の管理入口を示す画面の追加候補。リポジトリ定義3件の接続確認を示す画像とは扱わない。 |
| [05-playwright-config.jpg](../../_images/verification-20261004/app-20261004-05-playwright-config.jpg) | 既存PlaywrightのLocal設定。 | 接続設定を読む画面の差し替え候補。新規追加の成功を示す画像とは扱わない。 |
| [06-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-06-agent-merge-before.jpg) | CI全成功後、Agent mergeがOffの開始前画面。 | PR作成後の現行の開始操作を示す差し替え候補。 |
| [06-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-06-pr-merged-app.jpg) | AppのMergedとSuccessful 4。 | 第6章の自動マージ完了を示す画面の追加候補。 |
| [06-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-06-pr-merged-github.jpg) | GitHub WebのMergedと全4ジョブ成功。 | Appの表示との照合の根拠として取得済み。本文への追加要否は未判定。 |
| [07-canvas-initial-error.jpg](../../_images/verification-20261004/app-20261004-07-canvas-initial-error.jpg) | 初回処理の認証なしAPIの404。 | 初回の自動修正を確認する根拠として保管。受講者向けの掲載候補とはまだ扱わない。 |
| [07-canvas-initial-layout.jpg](../../_images/verification-20261004/app-20261004-07-canvas-initial-layout.jpg) | 初回Canvasの6件と優先順位、読みにくい配色。 | 可読性レビュー前の根拠として保管。掲載は修正後の画像を優先する。 |
| [07-canvas-readable.jpg](../../_images/verification-20261004/app-20261004-07-canvas-readable.jpg) | 可読性修正後のCanvasと6件の課題。 | 第7章のCanvas生成結果を示す差し替え候補。初回の読みにくい画面よりこちらを優先する。 |
| [07-canvas-receipt.jpg](../../_images/verification-20261004/app-20261004-07-canvas-receipt.jpg) | 修正後の本文追加と受領応答。 | 本文を1回追加し、受領のみを返す操作を示す追加候補。Refresh途中のFetchingが写るため、掲載範囲を確認する。 |
| [07-changes-canvas.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas.jpg) | 共有版Canvasファイルの差分を全幅で表示。 | 7.2で共有するファイルと変更内容を確認する画面の追加候補。 |
| [07-changes-canvas-final.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas-final.jpg) | 共有版Canvasの最終差分。 | PR作成時の追加修正を含む最終版のChangesを示す追加候補。 |
| [07-changes-canvas-readme.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas-readme.jpg) | 共有Canvasの再利用手順を記載したREADME。 | 別セッションでCanvasを開く説明を確認する画面の追加候補。 |
| [07-canvas-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-07-canvas-agent-merge-before.jpg) | 共有版のCI全成功後、Agent mergeをOnにする前。 | 第7章の開始操作を示す差し替え候補。 |
| [07-canvas-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-app.jpg) | 共有版PRのAppのMerged表示。 | Canvas共有のマージ完了を示す追加候補。 |
| [07-canvas-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-github.jpg) | 共有版PRのGitHub WebのMerged表示。 | Appの表示との照合の根拠として保管。本文への追加要否は未判定。 |
| [07-canvas-trust.jpg](../../_images/verification-20261004/app-20261004-07-canvas-trust.jpg) | 更新した拡張とscriptsを確認する承認画面。 | 共有Canvasを別セッションで使う前の確認を示す追加候補。 |
| [07-canvas-reopened.jpg](../../_images/verification-20261004/app-20261004-07-canvas-reopened.jpg) | 最新mainの別セッションで開いた共有Canvas。 | 7.3の再利用を示す画面の追加候補。 |
| [07-canvas-search-card.jpg](../../_images/verification-20261004/app-20261004-07-canvas-search-card.jpg) | 検索Issue #1の本文と追加ボタン。 | 別セッションの会話へ課題を渡す入口を示す追加候補。 |
| [07-search-issue-receipt.jpg](../../_images/verification-20261004/app-20261004-07-search-issue-receipt.jpg) | 新しいセッションでのIssue #1の受領応答。 | 実装を始めず、参照情報を受領した結果を示す追加候補。 |
| [07-search-plan-question.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-question.jpg) | Clear filtersで検索語も解除する仕様の質問。 | Planで仕様を判断し、Continueで回答する操作を示す追加候補。 |
| [07-search-plan-review.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-review.jpg) | 検索のPlanとApprove and implement。 | 検索と既存フィルターの関係、期待値を確認して承認する画面の追加候補。 |
| [07-changes-search.jpg](../../_images/verification-20261004/app-20261004-07-changes-search.jpg) | 検索入力、0件の文面などの実装差分。 | 検索実装のChangesをレビューする画面の追加候補。 |
| [07-search-default.jpg](../../_images/verification-20261004/app-20261004-07-search-default.jpg) | 主担当の別ブラウザーで確認した検索前の21件。 | 検索の初期状態を示す画面の追加候補。 |
| [07-search-two.jpg](../../_images/verification-20261004/app-20261004-07-search-two.jpg) | 主担当が確認したServer SiegeとVirtual Server Simulatorの2件。 | 大小文字を区別しない部分一致を示す追加候補。 |
| [07-search-combined.jpg](../../_images/verification-20261004/app-20261004-07-search-combined.jpg) | 主担当が確認した検索・カテゴリ・出版社のANDで1件。 | 既存フィルターと検索の組み合わせを示す追加候補。 |
| [07-search-zero.jpg](../../_images/verification-20261004/app-20261004-07-search-zero.jpg) | 主担当が確認した0件の説明と結果通知。 | 0件時の表示を示す追加候補。 |
| [07-search-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-07-search-agent-merge-before.jpg) | 検索PRのCI全成功後、Agent mergeをOnにする前。 | 検索実装のマージ開始を示す画面の追加候補。 |
| [07-search-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-07-search-pr-merged-app.jpg) | 検索PRのAppのMerged表示。 | 検索実装のマージ完了を示す追加候補。 |
| [07-search-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-07-search-pr-merged-github.jpg) | 検索PRのGitHub WebのMerged表示。 | Appとの照合の根拠として保管。本文への追加要否は未判定。 |
| [07-canvas-after-search-merge.jpg](../../_images/verification-20261004/app-20261004-07-canvas-after-search-merge.jpg) | Refresh後のOpen 5件と更新した優先順位。 | 完了した検索Issueが一覧から消える結果を示す追加候補。 |
| [08-automation-settings.jpg](../../_images/verification-20261004/app-20261004-08-automation-settings.jpg) | Manual、Local、演習用コピーなどの自動化設定。 | 第8章の設定画面の差し替え候補。 |
| [08-automation-create-and-run.jpg](../../_images/verification-20261004/app-20261004-08-automation-create-and-run.jpg) | 固定プロンプトとCreate and runの入口。 | 読み取りの範囲と開始操作を示す差し替え候補。 |
| [08-automation-result-prs.jpg](../../_images/verification-20261004/app-20261004-08-automation-result-prs.jpg) | 対象、時刻、期間とマージ済みPR 5件の報告。 | 実行時点と期間を含む結果の読み方を示す追加候補。 |
| [08-automation-result-issues.jpg](../../_images/verification-20261004/app-20261004-08-automation-result-issues.jpg) | 現在OpenのIssue 5件の報告。 | 件数と一覧、完了課題の除外を確認する追加候補。 |
| [08-automation-succeeded.jpg](../../_images/verification-20261004/app-20261004-08-automation-succeeded.jpg) | Localと緑の成功アイコン、53秒。状態はAXでもSucceededを確認。 | 第8章の正常終了を示す差し替え候補。Succeededという文字が画像内に表示されているとは扱わない。 |

Issues一覧の画像は、旧コピーの詳細や複数リポジトリの選択が残っていない画面を採用します。設定画面や操作途中の画像は、確認記録として保管する対象です。受講者向けの掲載候補とは分けて扱います。

## 最終判定と反映の状況

画面差の読み替えと本文のレビュー工程による追加修正を行い、第0〜8章を完了しました。実装の判定には画面、差分、実際の自動検査、PRの最新CI結果を使い、自動化の報告はGitHub APIで独立に照合しています。初回プロンプトだけで無修正に進められる保証は、この結果に含みません。

今回の受講者向け原稿は直接修正していません。本文の修正候補はR01〜R07、画像の差し替え・追加・重複掲載の削除候補は[画像対応表](verification-images-20261004.md)で確認できます。本レポートと画像対応表は別ファイルで管理しています。

初回インストール、初回サインイン、発生しなかった障害対応、Agent merge actionsの四項目の個別表示、MCPによる検索結果からの詳細リンクのクリック遷移は未確認です。詳細遷移はE2Eで成功しています。継続的なスケジュール実行とクラウド実行も今回の検証範囲には含めていません。
