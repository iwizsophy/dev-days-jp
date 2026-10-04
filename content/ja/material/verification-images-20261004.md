# 配布資料に使う画像の選定案

2026年10月4日、全章の実走と不足画像の再取得を終えた段階の取得画像95枚を対象にしています。本文に使う主候補は30枚、必要に応じて使う補足候補は22枚です。主候補と補足候補を合わせた掲載可は52枚、要再撮影は1枚、記録のみは42枚です。元画像はすべて保存します。

30枚のうち23枚は切り取りが必要です。元画像のまま使える候補は7枚です。ここでの判定は画像の内容とファイルの状態を対象とし、PDFへ配置した後の文字サイズは別に確認します。切り取り、画像の改変、受講者原稿への挿入は実施していません。

## ファイルの確認

95枚すべてをJPEGとして正常に読み込めました。拡張子の不一致、読み込みエラー、候補ファイルの欠落はありません。寸法は幅807〜1282ピクセル、高さ712〜892ピクセルです。ファイルごとの容量・寸法・SHA256・掲載判定は[image-inventory.json](../../_images/verification-20261004/app-20261004-image-inventory.json)に保存しました。

この確認だけでは掲載の可否を決めません。対象の課題が正しく、受講者が読む操作や結果を画像内で確認できることも条件にしました。旧コピーや検証者の会話が大きく映る画像は、切り取りを条件にしています。

## 掲載判定

| 判定 | 枚数 | 扱い |
| :--- | ---: | :--- |
| 掲載可 | 52 | 主候補30枚と補足候補22枚。切り取りや説明の条件を満たして使う。 |
| 要再撮影 | 1 | 公開テンプレートの入口。公開後に再撮影する。 |
| 記録のみ | 42 | 途中経過、修正前、環境出力、重複する結果の証拠。本文へ一律に追加しない。 |
| 合計 | 95 | 全ファイルの判定はimage-inventory.jsonに記載。 |

要再撮影は`00-template-menu.jpg`の1枚です。Drizzleのリンク表示とCanvasの最終保存差分は再取得しました。以前の部分画像`03-drizzle-links.jpg`と`07-changes-canvas.jpg`は記録のみへ変更しています。

## 章ごとの枚数

| 対象 | 主候補の枚数 | 残す内容 |
| :--- | ---: | :--- |
| 第0章 | 1 | テンプレートからコピーを作る入力例 |
| 第1章 | 2 | 設定の信頼、Open一覧の表示条件 |
| 第2章 | 3 | 開始条件、星評価、手動マージとCI |
| 第3章 | 4 | Issue開始、隠しファイル、Raw、規約の差分 |
| 第4章 | 4 | Plan選択、計画承認、規約と実装の差分、複合フィルター |
| 第5章 | 4 | 既存MCP設定、隔離データの3件と0件 |
| 第6章 | 2 | 既存PRの自動マージ開始、CIとMerged |
| 第7章 | 7 | Canvasの完成例、共有保存先、別セッションでの受領、検索計画、併用検索と0件、手動更新 |
| 第8章 | 3 | Manualと実行場所、実行の成功状態、報告内容の照合 |
| 合計 | 30 | 同じ操作や結果の重複掲載を避ける |

## 主候補30枚

表は教材内の順序で使うための案です。番号は選定用で、原稿の項番ではありません。

| 番号 | 章節 | 取得画像 | 学ぶこと | 掲載条件 |
| :--- | :--- | :--- | :--- | :--- |
| P01 | 0.2.2 | [00-template-form-top.jpg](../../_images/verification-20261004/app-20261004-00-template-form-top.jpg) | テンプレート、Include all branches、Owner、コピー名 | テンプレートと入力欄を残し、Private選択と個人の上部アイコンは範囲外にする。公開範囲とJumpstart空欄は本文で説明する。 |
| P02 | 1.2 | [01-repository-trust.jpg](../../_images/verification-20261004/app-20261004-01-repository-trust.jpg) | 設定を読んで信頼を承認する区切り | Repository trustのダイアログに絞り、過去のProjectsを除く。 |
| P03 | 1.3 | [01-issues-new-view.jpg](../../_images/verification-20261004/app-20261004-01-issues-new-view.jpg) | Open一覧の表示条件と8件の課題 | リポジトリ、New view、State Open、Save、一覧を残し、過去のProjectsを除く。 |
| P04 | 2.1 | [02-new-session.jpg](../../_images/verification-20261004/app-20261004-02-new-session.jpg) | New worktree・main・Interactiveの開始条件 | 現在のプロジェクトと開始条件に絞り、過去のProjectsを除く。 |
| P05 | 2.4 | [02-star-rating.jpg](../../_images/verification-20261004/app-20261004-02-star-rating.jpg) | ゲームカード上の星評価の完成例 | タイトル・星評価・View detailsを読める完成例として使う。 |
| P06 | 2.5 | [02-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-passed.jpg) | Agent mergeが無効の手動マージとCI全成功 | ダイアログ内の4ジョブとMerge pull requestを残す。 |
| P07 | 3.2 | [03-files-options.jpg](../../_images/verification-20261004/app-20261004-03-files-options.jpg) | 現在の隠しファイル表示メニュー | Show all hidden filesとShow tracked hidden files、対象ファイルを残す。 |
| P08 | 3.2 | [03-unit-test-applyto.jpg](../../_images/verification-20261004/app-20261004-03-unit-test-applyto.jpg) | Raw切替とapplyToの適用範囲 | Rawの入口、ファイル名、冒頭のメタデータを残す。Rich textとの比較画像は追加しない。 |
| P09 | 3.3 | [03-issue-details.jpg](../../_images/verification-20261004/app-20261004-03-issue-details.jpg) | IssueからNew sessionを始める入口 | 対象リポジトリ、Issue #8、New sessionに絞る。以後のIssue開始操作は本文で参照する。 |
| P10 | 3.4 | [03-changes-instructions.jpg](../../_images/verification-20261004/app-20261004-03-changes-instructions.jpg) | コメント規則・書式・TSDocの差分 | 本章の共通指示の差分として使う。README・ESLintの差分を見た証拠にはしない。 |
| P11 | 4.2 | [04-plan-mode.jpg](../../_images/verification-20261004/app-20261004-04-plan-mode.jpg) | Planを選ぶ操作 | モードメニューとIssue #7に絞る。 |
| P12 | 4.3 | [04-plan-review.jpg](../../_images/verification-20261004/app-20261004-04-plan-review.jpg) | OR/AND条件を読んで計画を承認する判断 | 計画と承認欄に絞る。実走では承認項目の選択だけで実装へ移行した。 |
| P13 | 4.4 | [04-changes-filters-final.jpg](../../_images/verification-20261004/app-20261004-04-changes-filters-final.jpg) | TSDocとOR/AND処理の一致 | ファイル名、TSDoc、処理の全文を残す。PR #15作成後の撮影時点は検証記録で区別する。 |
| P14 | 4.4 | [04-filter-combined-final.jpg](../../_images/verification-20261004/app-20261004-04-filter-combined-final.jpg) | 複合条件と2タイトル、星評価の対応 | 条件・件数・カード名・星評価を残す。詳細リンクは画面外なので本文と実走記録で確認する。 |
| P15 | 5.2 | [05-mcp-installed.jpg](../../_images/verification-20261004/app-20261004-05-mcp-installed.jpg) | 現在のMCP設定の入口と既存登録 | Customize・Installed・Playwrightに絞り、過去のProjectsと個人用Skill一覧を除く。Connectedの文字は画像にない。 |
| P16 | 5.2 | [05-playwright-config.jpg](../../_images/verification-20261004/app-20261004-05-playwright-config.jpg) | 既存MCPのLocal設定と起動コマンド | ダイアログに絞る。既存設定の確認画面と説明し、新規追加や保存を実施した画像として使わない。 |
| P17 | 5.4 | [05-isolated-three.jpg](../../_images/verification-20261004/app-20261004-05-isolated-three.jpg) | 通常データと分けたテスト用3件 | Showing 3 gamesとテスト用カードを残す。URL・接続元は検証記録で照合する。 |
| P18 | 5.4 | [05-isolated-zero.jpg](../../_images/verification-20261004/app-20261004-05-isolated-zero.jpg) | 0件になる組み合わせと空状態の説明 | Puzzle・Nova Interactive、0件表示、Clear filtersを残す。 |
| P19 | 6.2 | [06-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-06-agent-merge-before.jpg) | CIを確認してから既存PRの自動マージへ渡す入口 | Ready to merge、対象PR、無効状態のAgent mergeスイッチに絞り、検証者の会話を除く。 |
| P20 | 6.3 | [06-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-06-pr-merged-github.jpg) | MergedとCI4ジョブの成功を分けて確認する結果 | PR #15、main、Merged、ジョブ名と成功状態を残す。上部のアカウントと不要なリポジトリ表示を除く。 |
| P21 | 7.1 | [07-canvas-readable.jpg](../../_images/verification-20261004/app-20261004-07-canvas-readable.jpg) | 優先3件と残り3件、理由、本文追加の完成例 | 最大化した暗色表示を使う。全6カードは画面内に収まらないため、掲載例と全件の実走確認を分ける。 |
| P22 | 7.2 | [07-changes-canvas-final.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas-final.jpg) | 一時的なCanvasと共有保存するファイルを区別する | 保存先の全パスとREADMEを含むファイルツリー、Commitsを残して切り取る。コード全文や合計556行追加・1行削除の証拠としては扱わない。 |
| P23 | 7.3 | [07-search-issue-receipt.jpg](../../_images/verification-20261004/app-20261004-07-search-issue-receipt.jpg) | 別セッションへ本文を渡し、受領だけを確認する区切り | 左側のIssue #1本文全文と受領応答へ切り取る。通知の冒頭と設定欄は除く。1回ずつの送信・受領は実走記録で照合する。 |
| P24 | 7.4 | [07-search-plan-review.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-review.jpg) | 検索の正規化、OR/AND、解除条件を計画で読む | Plan本文を使う。Review planの承認選択肢は映らないため、第4章の承認操作を参照する。固有の承認画面が必要なら追加撮影する。 |
| P25 | 7.5 | [07-search-combined.jpg](../../_images/verification-20261004/app-20261004-07-search-combined.jpg) | 検索・カテゴリ・出版社の併用と星評価の維持 | sErVeR、Strategy、GitHub Games、1件、Server Siege、評価3.3を残す。上端の説明文と下端の浮いた操作表示を除く。詳細リンクは画面外。 |
| P26 | 7.5 | [07-search-zero.jpg](../../_images/verification-20261004/app-20261004-07-search-zero.jpg) | 複合条件で0件になる場合の説明 | no-such-title、Strategy、GitHub Games、0件と空状態の全文を残す。不要な歓迎文と下端の操作表示を除く。解除を操作した証拠にはしない。 |
| P27 | 7.5 | [07-canvas-after-search-merge.jpg](../../_images/verification-20261004/app-20261004-07-canvas-after-search-merge.jpg) | マージとOpen一覧の手動更新を区別する | 右側のリポジトリ・Refresh issues・Open5件・先頭カードへ切り取る。全5カードの#1除外は実走記録で照合する。 |
| P28 | 8.1 | [08-automation-create-and-run.jpg](../../_images/verification-20261004/app-20261004-08-automation-create-and-run.jpg) | 実行タイミングと場所、読み取り専用の範囲を設定する | Manual、クラウド実行オフ、プロンプト、Create and runの案内を残してダイアログへ切り取る。プロジェクト名末尾は省略されているため実走記録で照合する。終了結果の画像としては扱わない。 |
| P29 | 8.2 | [08-automation-succeeded.jpg](../../_images/verification-20261004/app-20261004-08-automation-succeeded.jpg) | 実行場所と今回の成功状態を確認する | 今回のRecent runs行と見出しへ切り取り、Local・対象リポジトリ・53秒・緑の成功アイコンを残す。過去の実行を除く。Succeededの文字は画像内にない。 |
| P30 | 8.2 | [08-automation-result-issues.jpg](../../_images/verification-20261004/app-20261004-08-automation-result-issues.jpg) | 成功状態とは別に、期間・件数・一覧の内容を読む | JSTの取得時点と対象期間、PR5件とOpen Issue5件の表、読み取り専用の終了報告へ切り取る。対象リポジトリとURL・日時は実走記録で照合する。 |

## 補足候補と検証専用の画像

次の22枚は主候補へ一律に追加しません。授業で取り上げる判断を補う場合だけ、切り取りと掲載位置を検討します。

| 補足する場面 | 取得画像 | 判断 |
| :--- | :--- | :--- |
| Jumpstartを空欄にする確認 | `00-template-form.jpg` | 第0章の本文だけで追えるなら省略する。 |
| 実装とテストの差分 | `02-changes-game-card.jpg`、`02-changes-render-tests.jpg` | コードレビューの演習を厚くする場合に使う。 |
| Filesの入口と検索 | `03-add-tab-files.jpg`、`03-file-search.jpg` | 操作名とCtrl+Pの説明で追えるなら省略する。 |
| 指示を反映したコード例 | `03-code-example.jpg` | 会話と個人の作業パスを切り取る。コード例を本文に示す方法も選べる。 |
| スキルの内容とビルド結果 | `04-quality-skill.jpg`、`04-build-complete.jpg` | スキル画像のdescription末尾は切れている。ビルド画像の会話は検査結果の補助証拠として扱う。 |
| 初期状態、Issue開始、設計質問 | `04-filter-default-final.jpg`、`04-issue-details.jpg`、`04-plan-question.jpg` | 初期21件や設計判断を比較する必要がある場合に使う。 |
| AppのMerged表示 | `06-pr-merged-app.jpg` | 第6章のGitHub画像で結果を確認できるため、App側を補う場合だけ使う。 |
| 共有拡張の承認 | `07-canvas-trust.jpg` | priority-kanbanとdatabase-explorerの保存先、Accept for new sessionsを残してダイアログへ切り取る。 |
| 別セッションのCanvasと対象カード | `07-canvas-reopened.jpg`、`07-canvas-search-card.jpg` | 再表示画像はOpen6件と有効な#5・#6のボタンを示す。対象カード画像は左側のIssue #1へ切り取り、本文・優先理由・追加ボタンを示す。全6カードの照合は実走記録で確認する。 |
| 検索の設計質問 | `07-search-plan-question.jpg` | 質問・推奨回答・Continueへ切り取る。回答や計画承認を済ませた画像としては扱わない。 |
| 検索入力と空状態の差分 | `07-changes-search.jpg` | ラベル・aria-controls・data-testidの差分を読む場合に使う。正規化とAND判定の処理全体は画面外。 |
| 初期21件と大小文字を混ぜた2件検索 | `07-search-default.jpg`、`07-search-two.jpg` | 検索条件・件数・2タイトルへ切り取る。カード下部と星は画面外なので星の維持を示す用途には使わない。 |
| Automation報告の対象と取得時点 | `08-automation-result-prs.jpg` | 対象リポジトリ、JSTの取得時点・期間、PR5件の表へ切り取る。主候補の一覧画像と重なるため必要な場合だけ使う。 |
| 指示ファイル内の参照リンク | `03-drizzle-links-final.jpg` | Rich textのTestingとunit-tests.instructions.mdのリンク名全文へ切り取る。相対リンクの記法やリンク遷移を再確認した画像ではない。 |
| 保存後のCanvasの再利用説明 | `07-changes-canvas-readme.jpg` | READMEの保存先と再利用手順1〜3を読む場合に使う。末尾の状態保存説明は画面外。 |

初回404、薄い文字のCanvas、修正前のフィルター、CI実行中、停止ログ、環境出力、重複するCI・Mergedの画像は検証記録へ残します。失敗例を最終画面の操作例と混同させないための構成案です。

`00-template-menu.jpg`はPrivate templateと保護警告が大きく、公開テンプレートの入口としては再撮影が必要です。`00-template-form-top.jpg`と`00-template-form.jpg`もPrivateを選んだ例なので、公開範囲の必須値として見せないようにします。

共有CanvasのPR #17はマージ済みで、別セッションでの再表示と本文受領を撮影しました。新しい受領画像を主候補にしたため、`07-canvas-receipt.jpg`は記録のみへ変更しています。共有PRと検索PRのAgent merge・Mergedの6枚は第6章と重複するため、検証記録に残します。Automationの設定画像08-automation-settings.jpgも、主候補の設定・実行入口と重複するため記録のみです。

`07-search-mcp-result.jpg`は呼び出し一覧とAIの結果表を示す画像で、個別ツールのResultは展開されていません。手動画像の0件検索語no-such-titleと、MCPの報告にあるnothing-matches-this-titleは別の入力です。前後の空白処理、キーボード解除、詳細リンク、終了確認は実走記録で照合し、静止画像だけで独立して確認できたとは扱いません。

## 全コースの公開枚数

現時点ではスクリーンショット31枚と、既存の概念図4点を残す案です。現在の主候補30枚に、公開テンプレートの入口1枚を加えます。第8章は実走完了の報告を受け、成功状態とレポートを確認しました。Succeededという状態名の確認とAPI照合は実走記録を根拠とし、画像だけで独立して確認できたとは扱いません。

| 追加する場面 | 枚数の目安 | 現在の状態 |
| :--- | ---: | :--- |
| 公開テンプレートのUse this templateの入口 | 1 | 公開後に再撮影 |
| 追加の合計 | 1 | 30枚と合わせて31枚の案 |

第7章のPlan選択メニューとReview planの承認選択肢は未撮影です。検索の計画本文を読む画像と、第4章の操作説明への参照で追えることを採用条件にしました。固有の承認画面が必要なら追加撮影し、公開枚数を見直します。

既存の29掲載箇所は、原稿の行、画像ファイル、意味を再確認しました。重複掲載の削除候補はE17・E25・E26の3件です。E17は第3章で説明済みのFiles入口を繰り返すため、スキルの内容に置き換える候補です。E25・E26は第6章と同じAgent mergeの操作なので、第6章への参照と共有保存先の確認で追える場合に省略します。

既存の概念図は、学習の流れ、計画承認、MCPの検証段階、worktreeの引き継ぎの4点です。これらは操作画面と役割が異なるため維持します。

画像を省く箇所でも、受講者が行う操作と意図を本文に残す方針です。画像数を減らすために説明を薄める変更は提案していません。

## 掲載箇所ごとの対応

作成日：2026年10月4日。演習0〜8の3つの事前監査表を統合し、最新原稿の画像掲載箇所で章節とファイル名を補いました。全章の取得画像を確認し、撮影状況とファイル列へ進捗を反映しています。未取得・未確認の項目は未撮影または未確認のまま残しています。本表は画像の内容と掲載候補を整理するもので、ハンズオンの成功は別の実走記録で確認します。

参照した監査表は`audit-0-2.md`、`audit-3-5.md`、`audit-6-8.md`です。本表の「削除候補」は原稿内の重複掲載に対する提案であり、画像ファイルそのものの削除を指しません。受講者原稿と掲載画像の参照は変更していません。

## 既存画像

掲載箇所ごとに29件あります。共用されている画像も、課題に合う画面を撮るため個別に記載しました。第1章と第8章には現在、画像の掲載がありません。

| ID | 章節・原稿行 | 元画像（content/_images内） | 対応候補 |
| :--- | :--- | :--- | :--- |
| E01 | 0.2.2／0-prerequisites.md:87 | app-1.1.20-20260913-template-menu.png | 差し替え |
| E02 | 0.2.2／0-prerequisites.md:97 | app-1.1.20-20260913-template-form.png | 差し替え |
| E03 | 2.1／2-add-star-rating.md:44 | app-1.1.20-20260913-new-session.png | 差し替え |
| E04 | 2.3／2-add-star-rating.md:96 | app-1.1.20-20260913-changes.png | 差し替え |
| E05 | 2.4／2-add-star-rating.md:134 | app-1.1.20-20260913-star-rating.jpg | 差し替え |
| E06 | 2.4.1／2-add-star-rating.md:147 | app-1.1.20-20260913-run-menu.png | 差し替え |
| E07 | 3.2／3-custom-instructions.md:37 | app-1.1.20-20260913-add-tab.png | 差し替え |
| E08 | 3.2／3-custom-instructions.md:43 | app-1.1.20-20260913-file-search.png | 差し替え |
| E09 | 3.2／3-custom-instructions.md:51 | app-1.1.20-20260913-files-options.png | 差し替え |
| E10 | 3.3／3-custom-instructions.md:81 | app-1.1.20-20260913-issue-session.png | 差し替え |
| E11 | 3.4／3-custom-instructions.md:105 | app-1.1.20-20260913-changes.png | 差し替え |
| E12 | 4.2／4-build-filtering.md:39 | app-1.1.20-20260913-issue-session.png | 差し替え |
| E13 | 4.2／4-build-filtering.md:43 | app-1.1.20-20260913-plan-mode.png | 差し替え |
| E14 | 4.3／4-build-filtering.md:75 | app-1.1.20-20260913-plan-review.png | 差し替え |
| E15 | 4.4／4-build-filtering.md:94 | app-1.1.20-20260913-changes.png | 差し替え |
| E16 | 4.4／4-build-filtering.md:100 | app-1.1.20-20260913-run-menu.png | 差し替え |
| E17 | 4.5.1／4-build-filtering.md:124 | app-1.1.20-20260913-add-tab.png | 掲載の削除候補 |
| E18 | 4.7.3／4-build-filtering.md:228 | app-plan-approval.png | 維持 |
| E19 | 第5章導入／5-mcp-playwright.md:21 | app-mcp-evidence.png | 維持 |
| E20 | 5.2.3／5-mcp-playwright.md:74 | app-1.1.20-20260913-mcp-catalog.jpg | 差し替え |
| E21 | 5.2.3／5-mcp-playwright.md:76 | app-1.1.20-20260913-mcp-config.jpg | 差し替え |
| E22 | 6.2／6-agent-merge.md:60 | app-1.1.20-20260913-agent-merge-menu.png | 差し替え |
| E23 | 6.2／6-agent-merge.md:70 | app-1.1.20-20260913-agent-merge-permissions.png | 差し替え |
| E24 | 6.3／6-agent-merge.md:83 | app-worktree-handoff.png | 維持 |
| E25 | 7.2／7-canvases.md:87 | app-1.1.20-20260913-agent-merge-menu.png | 掲載の削除候補 |
| E26 | 7.2／7-canvases.md:93 | app-1.1.20-20260913-agent-merge-permissions.png | 掲載の削除候補 |
| E27 | 7.4／7-canvases.md:130 | app-1.1.20-20260913-plan-mode.png | 差し替え |
| E28 | 7.4／7-canvases.md:134 | app-1.1.20-20260913-plan-review.png | 差し替え |
| E29 | 導入／README.md:24 | app-learning-flow.png | 維持候補 |

| ID | 役割 | 理由 |
| :--- | :--- | :--- |
| E01 | 教材用コピーの作成入口 | 既存画像の取得先はgithub-samples/tailspin-toysで、本文の教材用テンプレートと異なる。 |
| E02 | コピー作成時の入力・設定 | 元テンプレートの表示を合わせ、作成前に確認する項目を示す。 |
| E03 | セッションの開始条件 | 現在のコピー名と作業条件を同時に読めるようにする。 |
| E04 | 差分レビューの入口と対象 | 既存画像はタイトル検索の差分で、AutopilotとAgent mergeも有効。本章の対象と異なる。 |
| E05 | 星評価の完成例 | 評価値と既存リンクが読める完成画面として残す。掲載位置は起動手順の後を検討。 |
| E06 | 開発サーバーの起動入口 | 既存画像のタイトル検索PRと利用枠警告は本節に関係しない。 |
| E07 | Filesの入口 | 既存画像の会話は後続のタイトル検索。本章の指示ファイル確認に合わせる。 |
| E08 | ファイル検索 | 本章のセッションで探すファイルが分かる画像にする。 |
| E09 | 隠しファイルの表示 | 指示ファイルを読むための表示設定として役割がある。 |
| E10 | Issueからのセッション開始 | 既存画像は並べ替えIssue。本章の規約更新Issueと異なる。 |
| E11 | 規約更新のレビュー | 既存画像はタイトル検索テストの差分。 |
| E12 | フィルターIssueからの開始 | 既存画像は並べ替えIssue。第3章とも対象が違うため別画像にする。 |
| E13 | Planへの切り替え | 既存画像はタイトル検索IssueとCanvas。 |
| E14 | 実装前の計画承認 | 既存画像の計画はタイトル検索。現在の承認操作も実走で確認する。 |
| E15 | 実装と規約の照合 | 既存画像はタイトル検索テスト。本章のTSDocと条件の組み合わせを示す。 |
| E16 | 実装後の画面確認の入口 | タイトル検索PR、Agent merge状態、利用枠警告は本節に関係しない。 |
| E17 | スキルファイルを開く入口 | Filesの開き方は第3章で確認済み。再掲よりSKILL.mdの内容を示す方が学習目的に合う。 |
| E18 | 計画から承認・実装へ進む関係 | 操作前に人が判断する理由を示す概念図。削除理由はない。 |
| E19 | 接続・呼び出し・動作・終了の違い | MCPのConnectedだけで検証済みと判断しない理由を示す概念図。 |
| E20 | 必要な場合の新規MCP登録入口 | 登録入口を示す意味はあるが、標準経路は既存設定。新規登録を実施したと誤認させない。 |
| E21 | 新規登録時の入力値 | 必要な場合の登録手順として残す。追加登録しない実走で登録済みとは報告しない。 |
| E22 | Agent Mergeの開始入口 | 既存画像は検索検証の会話や利用枠警告を含み、フィルターのマージと合わない。 |
| E23 | 任せる4操作とマージ権限 | 既存画像はタイトル検索PR。現在のフィルターPRで権限を示す。 |
| E24 | 前章の変更を次の作業へ継承 | main→worktree→PR→マージ後mainの関係と、次章の開始元を示す概念図。 |
| E25 | Canvas共有PRのマージ入口 | 第6章と同じ画像で新しい操作を説明しない。第6章への参照と手順で追える。 |
| E26 | Canvas共有PRのマージ権限 | 第6章と同じ画像。Canvas固有の共有操作を示す画像の方が役立つ。 |
| E27 | 本文追加後のPlanへの切り替え | Canvasの受領状態と計画への切り替えを同時に示す役割がある。 |
| E28 | 検索計画のレビューと承認 | 実データに基づく現在の計画で承認と実装開始の関係を示す。 |
| E29 | 開発の流れと人が判断すること | 3監査表の対象外。原稿の掲載箇所を補完して記載。学習全体を俯瞰する概念図として役割がある。 |

| ID | 撮影対象 | 撮影状況 | 撮影ファイル |
| :--- | :--- | :--- | :--- |
| E01 | 教材用テンプレートのUse this template → Create a new repository。 | 撮影済み・検証用。作成入口は読めるが、Private templateとブランチ保護警告が大きく、公開配布向けには再撮影を推奨。 | [00-template-menu.jpg](../../_images/verification-20261004/app-20261004-00-template-menu.jpg) |
| E02 | Owner、名前、公開範囲、Include all branchesオフ、Jumpstartの空欄。 | 撮影済み・切り取りを条件とする掲載候補。対象テンプレート・コピー名・Include all branchesと、Jumpstartの空欄が読める。公開範囲はPrivateが選択された例なので、本文で選択を説明し、掲載の中心はテンプレートと上部入力欄にする。具体的な公開範囲を画像で案内する場合は再撮影する。 | 主候補：[00-template-form-top.jpg](../../_images/verification-20261004/app-20261004-00-template-form-top.jpg)。Jumpstartを示す補足候補：[00-template-form.jpg](../../_images/verification-20261004/app-20261004-00-template-form.jpg) |
| E03 | 星評価のNew画面。入力欄、プロジェクト、New worktree、main、Interactive。 | 撮影済み・掲載候補。新コピー、New worktree・main、Interactiveが読める。全画面は過去のProjectsを多く含むため、入力欄を中心にした構図を推奨。 | [02-new-session.jpg](../../_images/verification-20261004/app-20261004-02-new-session.jpg) |
| E04 | 星評価セッションのChangesとGameCardの星評価・レンダリングテストの差分。 | 撮影済み・掲載候補。最大化したChangesの2枚で、GameCardの再利用・未評価表示と、4.2・0・5・nullの実レンダリング検査およびリンク検査が読める。過去のProjectsや利用枠警告は映らない。 | [02-changes-game-card.jpg](../../_images/verification-20261004/app-20261004-02-changes-game-card.jpg)、[02-changes-render-tests.jpg](../../_images/verification-20261004/app-20261004-02-changes-render-tests.jpg) |
| E05 | Browserのゲームカード。星評価、数値、タイトル、説明、詳細リンク。 | 撮影済み・掲載候補。ゲームカードの1段目3枚で、星評価・数値・タイトル・説明・View detailsが読める。詳細画面はリンク先を確認した補助証拠。 | [02-star-rating.jpg](../../_images/verification-20261004/app-20261004-02-star-rating.jpg)。補助証拠：[02-game-detail.jpg](../../_images/verification-20261004/app-20261004-02-game-detail.jpg) |
| E06 | 星評価セッションのRun → Run development site。 | 撮影済み・掲載候補。Run development siteなどのRunメニューと星評価の結果報告が読める。過去のProjectsを多く含むため、掲載は現在のセッションとメニューを中心にする。 | [02-run-menu.jpg](../../_images/verification-20261004/app-20261004-02-run-menu.jpg) |
| E07 | 指示ファイル確認中のAdd tab。Files、Browser、Terminalの入口。 | 撮影済み・掲載候補。Add tabのFiles・Browser・Terminalが読める。背景は前章の星評価PRなので、掲載はタブ列とメニューを中心にする。 | [03-add-tab-files.jpg](../../_images/verification-20261004/app-20261004-03-add-tab-files.jpg) |
| E08 | Go to fileとcopilot-instructions.mdの検索結果。 | 撮影済み・掲載候補。copilot-instructions.mdの検索欄と.github内の検索結果が読める。過去のProjectsと前章の会話を避け、検索ダイアログを中心にした掲載を推奨。 | [03-file-search.jpg](../../_images/verification-20261004/app-20261004-03-file-search.jpg) |
| E09 | View optionsのShow hidden filesと指示ファイル。 | 撮影済み・掲載候補。現行項目はShow all hidden filesとShow tracked hidden files。新コピーの指示ファイルと設定メニューが読める。原稿のShow hidden filesとは項目名が異なる。 | [03-files-options.jpg](../../_images/verification-20261004/app-20261004-03-files-options.jpg) |
| E10 | Update our repository coding standardsのタイトル、本文、New session。 | 撮影済み・掲載候補。新コピーの規約更新Issue #8、タイトル・本文・New sessionが読める。過去のProjectsを避け、対象リポジトリ・課題・開始ボタンを中心にした掲載を推奨。 | [03-issue-details.jpg](../../_images/verification-20261004/app-20261004-03-issue-details.jpg) |
| E11 | 指示、README、ESLintの更新が分かるChanges。 | 部分撮影・掲載候補。最大化したChangesで、共通のコメント規則、TypeScriptの書式、TSDoc、AstroのPropsへの適用が読める。本章の差分画像として使用でき、過去のProjectsや利用枠警告は映らない。READMEとESLint設定の個別差分は未取得。 | [03-changes-instructions.jpg](../../_images/verification-20261004/app-20261004-03-changes-instructions.jpg) |
| E12 | Allow users to filter games by category and publisherのタイトル、本文、New session。 | 撮影済み・掲載候補。新コピーのフィルターIssue #7、タイトル・本文・New sessionが読める。過去のProjectsを避け、対象リポジトリ・課題・開始ボタンを中心にした掲載を推奨。 | [04-issue-details.jpg](../../_images/verification-20261004/app-20261004-04-issue-details.jpg) |
| E13 | フィルターセッションのInteractive、Plan、Autopilotの選択肢。 | 撮影済み・掲載候補。フィルターセッションのInteractive、Plan、AutopilotのメニューとIssue #7が読める。過去のProjectsを避け、モードメニューと対象課題を中心にした掲載を推奨。 | [04-plan-mode.jpg](../../_images/verification-20261004/app-20261004-04-plan-mode.jpg) |
| E14 | フィルター計画とReview planのApprove and implement this plan。 | 撮影済み・掲載候補。更新後の計画でカテゴリOR・出版社AND、星評価と詳細リンクの維持、承認項目が読める。掲載は計画とReview planを中心にする。画面にはContinueもあるが、実走では承認項目を選ぶだけで実装へ移行した。 | 主候補：[04-plan-review.jpg](../../_images/verification-20261004/app-20261004-04-plan-review.jpg)。計画更新前の補助証拠：[04-plan-review-initial.jpg](../../_images/verification-20261004/app-20261004-04-plan-review-initial.jpg) |
| E15 | フィルターのTSDoc、カテゴリOR・出版社AND処理が読めるChanges。 | 最終差分を撮影済み・掲載候補。games.tsのTSDoc、db・filtersの引数、戻り値、カテゴリOR・出版社AND処理の全文が読める。PR #15作成直後の撮影で、ChangesはCommits 1を表示している。第4章のPR作成前のレビュー時点とは撮影タイミングが異なるため、掲載時の説明で混同しない。 | 主候補：[04-changes-filters-final.jpg](../../_images/verification-20261004/app-20261004-04-changes-filters-final.jpg)。修正前の証拠：[04-changes-filters.jpg](../../_images/verification-20261004/app-20261004-04-changes-filters.jpg) |
| E16 | フィルター実装直後のRunメニュー。 | 撮影済み・掲載候補。フィルターセッションのRun development siteとBuild static siteが読める。過去のProjectsと会話の修正依頼を避け、Runメニューを中心にした掲載を推奨。 | [04-run-menu.jpg](../../_images/verification-20261004/app-20261004-04-run-menu.jpg) |
| E17 | 再撮影は不要。A11のSKILL.md表示で補う。 | 入口の再撮影は不要。代替候補A11のSKILL.md表示を取得済み。descriptionの全文を示す画像は未達。 | 代替候補：[04-quality-skill.jpg](../../_images/verification-20261004/app-20261004-04-quality-skill.jpg) |
| E18 | 再撮影不要。概念図を維持。 | 未判定 | — |
| E19 | 再撮影不要。概念図を維持。 | 未判定 | — |
| E20 | 現行のMCP登録一覧でPlaywrightとAdd server。撮影のみなら保存しない。 | カタログの新規登録入口は未撮影。取得したInstalledの既存設定一覧はA15に記載し、MCPカタログやAdd serverの代わりにはしない。 | — |
| E21 | Local、npx、-y @playwright/mcp@latestの保存前フォーム。保存せず閉じる。 | 部分撮影・設定例の掲載候補。既存Playwrightの詳細でplaywright、Local、npx、-y @playwright/mcp@latestとSave・Cancelが読める。新規登録の保存前フォームとしては未撮影。設定の変更・保存は実施していない。既存設定の確認に説明を合わせる場合は、ダイアログを中心に掲載できる。 | 既存設定の詳細：[05-playwright-config.jpg](../../_images/verification-20261004/app-20261004-05-playwright-config.jpg) |
| E22 | 現在のフィルター実装セッションでAgent merge、Create PR、Create draft PRのメニュー。 | 部分撮影・既存PR経路の掲載候補。今回のPR #15では、Ready to mergeのメニューに無効状態のAgent mergeスイッチを確認できる。新規PR作成前のAgent merge・Create PR・Create draft PRのメニューは未撮影。既存PRでの現行操作はA30へ追加。 | 既存PR経路の代替候補：[06-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-06-agent-merge-before.jpg) |
| E23 | Address reviews、Fix CI failures、Resolve conflicts、Merge pull requestのチェック状態。 | 未撮影・表示未確認。今回は既存PRでAgent mergeを有効にすると即Mergedへ移行し、4項目の権限メニューは表示を確認できていない。A30のスイッチ画像は、各権限のチェック状態を示す画像の代わりにはならない。 | — |
| E24 | 再撮影不要。概念図を維持。 | 未判定 | — |
| E25 | 再撮影は不要。A19の共有保存先・差分を優先。 | 入口の追加掲載は不要。共有PR #17のAgent merge OffとMergedを撮影済みだが、第6章と同じ操作なので検証記録へ残す。共有保存先の差分はA19で別に確認する。 | 検証証拠：[07-canvas-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-07-canvas-agent-merge-before.jpg)、[07-canvas-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-app.jpg)、[07-canvas-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-github.jpg) |
| E26 | 再撮影は不要。第6章の権限確認へ参照。 | 4項目の権限画面は未取得・表示未確認。共有PRのマージ完了はA33で記録する。重複掲載の削除候補を維持し、権限画面を取得したことにはしない。 | — |
| E27 | 最新の共有Canvas、Issue本文の受領1回、モード選択。 | 部分撮影・掲載候補。Issue #1の本文全文と受領応答、右側のカードを読める。Planの設計質問と計画本文も取得したが、モード選択の画面は未取得。受領は実装開始や計画承認とは分けて扱い、本文の操作説明と第4章のPlan選択を参照する。 | 本文受領：[07-search-issue-receipt.jpg](../../_images/verification-20261004/app-20261004-07-search-issue-receipt.jpg)。設計質問：[07-search-plan-question.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-question.jpg)。計画本文：[07-search-plan-review.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-review.jpg) |
| E28 | 検索計画、Review plan、承認選択肢。 | 部分撮影・掲載候補。最大化したPlanにIssue #1の計画名、検索の正規化、カテゴリ内ORと検索・カテゴリ・出版社間AND、Clear filtersの方針が読める。Review planと承認選択肢は画面内にない。計画を読む画像として使い、第4章の承認操作を参照する条件で採用できる。承認固有の画面が必要なら追加撮影する。 | 計画本文：[07-search-plan-review.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-review.jpg) |
| E29 | 再撮影不要。主担当が掲載の妥当性を最終確認。 | 未判定 | — |


## 追加画像と検証証拠

「追加候補」は受講者向け本文への掲載を検討する画像です。「検証証拠」は実走結果の記録に使う画像で、すべてを本文へ掲載する必要はありません。「条件付き」は実際に画面が表示された場合だけ取得します。複数状態を記載した行は、1枚に詰め込まず、読むべき文字や結果が分かる枚数で取得してください。

| ID | 章節 | 役割 | 対応候補 |
| :--- | :--- | :--- | :--- |
| A01 | 0.2.2／1.3 | Bootstrapの完了と8件のIssue | 追加候補・検証証拠 |
| A02 | 1.1 | 初期接続・認証後の設定 | 条件付きの検証証拠 |
| A03 | 1.2 | プロジェクト接続の入口 | 追加候補 |
| A04 | 1.2 | 設定のレビューと信頼の承認 | 追加候補 |
| A05 | 1.3 | 空一覧からの表示条件変更 | 条件付きの検証証拠 |
| A06 | 1.4 | ChatとInteractiveの選択 | 追加候補 |
| A07 | 1.4／2.1〜2.3 | 会話・環境確認・実装・テスト結果 | 検証証拠 |
| A08 | 2.4.1 | 開発サーバーの停止 | 検証証拠 |
| A09 | 2.5 | 手動PR作成とマージ | 追加候補 |
| A10 | 2.5／3.5 | CI全成功とMerged | 検証証拠 |
| A11 | 4.5.1 | quality-checksのSKILL.md | 追加候補 |
| A12 | 4.5 | quality-checksの結果 | 追加候補・検証証拠 |
| A13 | 4.4／5.4 | 通常データの複合フィルター | 追加候補 |
| A14 | 5.4 | 隔離データの0件と解除 | 追加候補・検証証拠 |
| A15 | 5.2 | 既存MCP定義と信頼状態 | 追加候補 |
| A16 | 5.4〜5.5 | Playwright実操作と終了 | 追加候補・検証証拠 |
| A17 | 6.3 | 自動マージの完了 | 追加候補・検証証拠 |
| A18 | 7.1 | Canvasの完成形と確認する操作 | 追加候補 |
| A19 | 7.2 | Canvasの共有保存先と差分 | 追加候補 |
| A20 | 7.3 | 別セッションでの再利用と受領 | 追加候補・検証証拠 |
| A21 | 7.3 | 拡張の承認 | 条件付きの追加候補・検証証拠 |
| A22 | 7.5 | 検索と既存機能の組み合わせ | 追加候補 |
| A23 | 7.5 | Canvasの手動更新 | 追加候補 |
| A24 | 8.1 | 読み取り専用Automationの設定 | 追加候補 |
| A25 | 8.2 | Automationの終了状態とレポート | 追加候補・検証証拠 |
| A26 | 3.2 | 指示ファイルのRaw表示 | 追加候補・検証証拠 |
| A27 | 3.4 | 指示を反映したコード生成例 | 追加候補・検証証拠 |
| A28 | 4.2 | Planでの設計質問への回答 | 条件付きの追加候補・検証証拠 |
| A29 | 4.4 | フィルターの開発サーバー停止 | 検証証拠 |
| A30 | 6.2 | 既存PRでのAgent merge開始 | 追加候補・検証証拠 |
| A31 | 7.1 | Canvas初回の失敗と追加レビュー | 検証証拠 |
| A32 | 7.1.1／7.2 | 本文追加と重複送信の防止 | 検証証拠 |
| A33 | 7.2 | 共有CanvasのCI全成功とマージ | 検証証拠 |
| A34 | 7.4 | 検索計画の設計質問 | 条件付きの検証証拠 |
| A35 | 7.5 | 検索UIと空状態の差分 | 補足候補・検証証拠 |
| A36 | 7.5 | 検索MCPの結果報告と確認範囲 | 検証証拠 |
| A37 | 7.5 | 検索PRのCI全成功とマージ | 検証証拠 |

| ID | 理由 | 撮影対象 |
| :--- | :--- | :--- |
| A01 | コピー直後に課題が準備されたことと、読むべき一覧を示す。 | 自分のowner/repo、Openの8件、規約・フィルター・検索のタイトル。1.3の画像と共用可。 |
| A02 | 再実行では初回設定が出ないことがある。実際に表示された場合だけ記録する。 | 初期接続のContinueやテーマ選択。認証情報は写さない。 |
| A03 | 自分の演習コピーを追加する入口が現原稿にない。 | Projectsの＋、Add GitHub repository、自分のコピーの検索結果。 |
| A04 | 何を確認して接続するか、操作の区切りを示す。 | Review repository contentの設定内容、Repository trustの承認前画面。 |
| A05 | 未割り当てIssueが表示されない場合の実際の復旧操作を残す。 | Open、未割り当ての表示条件、必要ならNew view。参加者掲載は実走結果で判断。 |
| A06 | リポジトリ実装セッションと会話の開始方法の違いを示す。 | Chats → New chat、Chat、Interactiveが読める画面。 |
| A07 | 終了報告だけでなく、実行場所、対象、実行結果を確認する。 | Chatの日本語回答とIdle。別worktreeのNode.js・作業ディレクトリ・ブランチ。星評価の依頼と結果。GameCard実レンダリングと各検査の結果。 |
| A08 | 確認後にサーバーが停止したことを記録する。 | 該当ターミナルの終了表示。 |
| A09 | 第6章の自動化と比較する前に、自分で確認する操作を示す。 | Agent mergeがOffのPR画面、Merge pull request。自分のコピーのmainを確認。 |
| A10 | Ready to mergeだけを成功の根拠にしない。各課題のPRで照合する。 | 最新コミットのCI全ジョブ成功と、App・GitHub双方の同一PRのMerged。参加者掲載はA17との重複を検討。 |
| A11 | 入口の再掲より、スキルの役割と実際の検査項目を示す。 | SKILL.mdのname、description、検査項目。E17の代わりに掲載する候補。 |
| A12 | スキルを呼んだことと各検査の成功を区別できる。 | 単体、E2E、lint、型検査の結果一覧とBuild static siteの成功。 |
| A13 | カテゴリORと出版社ANDを、選択欄・件数・一覧の対応で示す。 | Strategy＋Puzzle＋GitHub Gamesの2件。選択状態、ゲーム名、星評価、詳細リンク。 |
| A14 | 通常データを変更せず空状態を検査する理由と、解除後の復帰を示す。 | 隔離3件の環境でPuzzle＋Nova Interactiveの0件、解除後3件。通常環境とのURL・接続元の違いも記録。 |
| A15 | 標準経路の画面が現原稿にない。既存playwrightの二重登録を防ぐ。 | Settings → MCP serversでgithub、playwright、astro-docsとConnected。Trust repositoryが出た場合は承認前も取得。 |
| A16 | 接続表示だけでなく、ツール呼び出し・実際の結果・終了を確かめる。 | Playwrightの操作と結果を開いた状態。browser_close、今回のサーバー停止と該当ポートの待受なしは検証証拠。 |
| A17 | Ready to merge、CI成功、マージ完了を別々に確認する方法を示す。 | AppのMerged、GitHubの最新コミットのCI全ジョブ成功・Merged。ジョブ名と状態が読める画像。 |
| A18 | 何を生成させ、どこをレビューするかを具体的に示す。 | 上位3件と残り、優先理由、Refresh、本文追加ボタン。 |
| A19 | 一時的なCanvasとリポジトリへ保存する共有アセットの違いを示す。 | ChangesまたはFilesの.github/extensions/priority-kanban/extension.mjsとREADME。 |
| A20 | 保存後の再利用と、本文追加が実装開始とは別の操作であることを示す。 | マージ後mainからの新worktreeで開いたCanvasと、本文1回の受領応答。 |
| A21 | 新しい拡張の承認画面が出た場合に、レビュー済みファイルを確認する入口を示す。 | 実際に表示された拡張承認画面。保存先と対象を確認できる範囲。 |
| A22 | 検索だけの確認に偏らず、カテゴリ・出版社・星評価の維持を示す。 | 検索・カテゴリ・出版社の併用結果と星評価、検索結果0件。期待するタイトル・件数は実データで決める。 |
| A23 | マージ通知とOpen一覧の再取得を区別する。 | 検索IssueがClosedになった後、Refreshでカードが除外されたCanvas。 |
| A24 | 実行タイミングと実行場所が別設定であること、対象の選択を示す。 | Manual、Run in the cloudオフ、選択プロジェクト、読み取り専用プロンプト。 |
| A25 | Succeededと内容の正しさを別に確認する方法を示す。 | Recent runsのLocal・Succeeded、対象期間・実行時点、PR・Issueの一覧。GitHubとの件数・状態照合値も記録。 |
| A26 | Rich textでは冒頭のメタデータが隠れ、applyToを確認するにはRawへの切り替えが必要。相対リンクの記法もRawで確認できる。 | unit-tests.instructions.mdのRaw切替とapplyTo全体。Drizzle指示の相対リンクとリンク先全体。 |
| A27 | 指示を更新する操作と、その指示が生成例へ反映されたかを読む操作を分けて示す。 | Publishersを返すコード例の関数、db引数、戻り値と、TSDocの@param・@returns。 |
| A28 | カテゴリを増やす条件を判断し、計画へ反映する受講者の役割を示す。質問が出た場合だけ掲載を検討する。 | カテゴリOR・ANDの選択肢とContinue、対象のフィルターIssue。 |
| A29 | 手動確認後の停止を、実装や検査の成功とは分けて記録する。 | 今回のRunターミナルの開発URLと終了表示。 |
| A30 | 通常のPR作成後、CIの全成功を人が確認してから自動マージへ渡す経路の操作を示す。 | フィルターPRのReady to mergeのメニュー、Agent mergeスイッチ、対象PR。 |
| A31 | 初回生成、自動修正、受講者による追加レビューを分け、最終版の成功と混同しない。 | 初回APIエラー、自動修正後の表示、可読性と通知方式の追加レビュー後の最終画面。 |
| A32 | カードの本文を渡す操作が、実装開始や繰り返し通知にならないことを確かめる。第7.3節の別セッションでの再利用とは分けて記録する。 | Issue本文の送信と受領応答が各1回の会話、送信後の無効なボタン、Refresh後も無効な状態。 |
| A33 | 保存した拡張を別セッションで使う前に、mainへの取り込みを確認する。第6章と重複するため本文への追加掲載は必要性を検討する。 | PR #17のCI全ジョブ成功、Agent merge Off、AppとGitHub双方のMerged。 |
| A34 | 検索と既存フィルターの解除条件を判断し、計画へ反映する受講者の役割を示す。 | Clear filtersで検索語も解除する回答候補と、推奨選択の状態。 |
| A35 | 計画で求めたラベル・操作対象・空状態が実装へ反映されたかを読む。 | index.astroの検索入力、aria-controls、data-testid、空状態文の差分。 |
| A36 | 終了報告と実際の操作結果を区別し、未確認の操作も記録する。 | Playwright呼び出し、検索条件別の件数とタイトル、キーボード操作・終了の結果。 |
| A37 | 検索の確認を終えた変更がmainへ取り込まれたことを、Canvas更新と分けて確認する。 | PR #18のAgent merge Off、App・GitHub双方のMerged、最新コミットのCI全成功。 |

| ID | 撮影状況 | 撮影ファイル |
| :--- | :--- | :--- |
| A01 | 一覧を撮影済み・検証用。GitHubのOpen 8件と、Appの新コピー・8件・対象3タイトルが読める。掲載候補は保存後の一覧を中心にする。Bootstrapの実行画面は未取得。 | [00-bootstrap-issues.jpg](../../_images/verification-20261004/app-20261004-00-bootstrap-issues.jpg)、[01-issues-open-saved.jpg](../../_images/verification-20261004/app-20261004-01-issues-open-saved.jpg)。Issue本文の補助：[01-issues-open.jpg](../../_images/verification-20261004/app-20261004-01-issues-open.jpg)。作成直後の補助証拠：[00-repository-created.jpg](../../_images/verification-20261004/app-20261004-00-repository-created.jpg) |
| A02 | 初回設定は未撮影。一般設定のバージョン画像は別用途の検証証拠であり、Continueや初回テーマ選択の代わりにはしない。 | 別用途：[01-app-version.jpg](../../_images/verification-20261004/app-20261004-01-app-version.jpg) |
| A03 | 部分撮影・検証用。Add GitHub repositoryは読めるが、新コピーの検索結果は未取得。旧PRの読込失敗と過去のProjectsが大きく、全画面の掲載は不採用。 | [01-add-repository-menu.jpg](../../_images/verification-20261004/app-20261004-01-add-repository-menu.jpg) |
| A04 | 部分撮影・掲載候補。承認前の設定一覧とAccept for new sessionsが読める。スクリプトの展開内容は未取得。掲載は承認ダイアログを中心にし、過去のProjectsを避ける。 | [01-repository-trust.jpg](../../_images/verification-20261004/app-20261004-01-repository-trust.jpg) |
| A05 | 撮影済み・検証用／掲載候補。Assigned to meの空一覧、State Open・検索空・Save、保存後8件が読める。詳細ペインを閉じた後の画面には＋が見える。掲載は操作部と一覧を中心にし、過去のProjectsを避ける。 | [01-issues-assigned-empty.jpg](../../_images/verification-20261004/app-20261004-01-issues-assigned-empty.jpg)、[01-issues-new-view.jpg](../../_images/verification-20261004/app-20261004-01-issues-new-view.jpg)、[01-issues-open-saved.jpg](../../_images/verification-20261004/app-20261004-01-issues-open-saved.jpg) |
| A06 | 部分撮影・検証用。ChatsとInteractiveは読めるが、New chatとChatの開始条件画面は未取得。回答画面には過去のProjectsと本演習外のJustRight履歴があり、そのままの掲載は非推奨。 | [01-quick-chat-complete.jpg](../../_images/verification-20261004/app-20261004-01-quick-chat-complete.jpg) |
| A07 | 部分撮影・検証用。日本語応答、Node.js・作業場所・ブランチ、GameCardの4条件とリンク検査、E2E22件などの終了報告が読める。星評価依頼の全文、各コマンドの展開出力、ChatのIdleの文字表示は未取得。環境出力の本文掲載は非推奨。 | [01-quick-chat-complete.jpg](../../_images/verification-20261004/app-20261004-01-quick-chat-complete.jpg)、[02-environment-output.jpg](../../_images/verification-20261004/app-20261004-02-environment-output.jpg)、[02-changes-game-card.jpg](../../_images/verification-20261004/app-20261004-02-changes-game-card.jpg)、[02-changes-render-tests.jpg](../../_images/verification-20261004/app-20261004-02-changes-render-tests.jpg)、[02-run-menu.jpg](../../_images/verification-20261004/app-20261004-02-run-menu.jpg) |
| A08 | 撮影済み・検証用。今回のRunターミナルに開発URLとShell session endedが読める。サーバーの終了証拠として保存し、本文への追加掲載は不要。 | [02-run-stopped.jpg](../../_images/verification-20261004/app-20261004-02-run-stopped.jpg) |
| A09 | 撮影済み・掲載候補。Agent merge Off、CI4件成功、手動のMerge pull request、マージ先mainを複数画像で確認できる。成功後のダイアログを優先し、CI実行中の画像はReady to mergeだけでは完了しないことの補助証拠とする。過去のProjectsを避けた構図を推奨。 | 主候補：[02-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-passed.jpg)。操作・待機の補助：[02-pr-ci-running.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-running.jpg)。マージ先の証拠：[02-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-02-pr-merged-app.jpg) |
| A10 | 章2・章3を撮影済み・検証用。星評価PR #13のコミット2038d40と規約更新PR #14のコミットd0899d2について、CI4ジョブの成功とGitHubのMergedが読める。章3のApp画像は紫色のPR #14と終了後の会話で、PRパネルのMerged文字は画面内にない。最新コミットの完全なSHAとAppの状態は実走記録で照合する。 | 章2：[02-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-ci-passed.jpg)、[02-pr-checks-passed.jpg](../../_images/verification-20261004/app-20261004-02-pr-checks-passed.jpg)、[02-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-02-pr-merged-app.jpg)、[02-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-02-pr-merged-github.jpg)。章3：[03-pr-ci-passed.jpg](../../_images/verification-20261004/app-20261004-03-pr-ci-passed.jpg)、[03-pr-checks-passed.jpg](../../_images/verification-20261004/app-20261004-03-pr-checks-passed.jpg)、[03-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-03-pr-merged-app.jpg)、[03-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-03-pr-merged-github.jpg) |
| A11 | 部分撮影・掲載候補。Raw表示のSKILL.mdでnameと単体・E2E・lint・型検査のコマンド表が読める。descriptionの末尾が右端で切れるため、全文を示す画像は未達。この画像はスキルの実行結果ではない。 | [04-quality-skill.jpg](../../_images/verification-20261004/app-20261004-04-quality-skill.jpg) |
| A12 | 部分撮影・掲載候補／検証用。Appのビルド出力で24 page(s) builtとComplete!が読める。会話にはunit38件・E2E26件・lint・typecheckの結果報告と、その後の修正内容が映る。各検査の展開出力は未取得。掲載はビルド結果を中心にし、過去のProjects・個人の作業パス・修正依頼を避ける。 | ビルド結果の主候補：[04-build-complete.jpg](../../_images/verification-20261004/app-20261004-04-build-complete.jpg)。起動・ビルドの入口：[04-run-menu.jpg](../../_images/verification-20261004/app-20261004-04-run-menu.jpg) |
| A13 | 修正後を撮影済み・掲載候補。未選択の21件と、Strategy・Puzzle・GitHub Gamesの2件、Bug Buster BrainteaserとServer Siegeの星評価が読める。Clear filtersはPublisherの下に配置されている。詳細リンクは画面外なので、リンク維持とキーボード移動は実走記録で照合する。過去のProjectsや会話は映らない。 | 主候補：[04-filter-default-final.jpg](../../_images/verification-20261004/app-20261004-04-filter-default-final.jpg)、[04-filter-combined-final.jpg](../../_images/verification-20261004/app-20261004-04-filter-combined-final.jpg)。修正前の証拠：[04-filter-default.jpg](../../_images/verification-20261004/app-20261004-04-filter-default.jpg)、[04-filter-combined.jpg](../../_images/verification-20261004/app-20261004-04-filter-combined.jpg) |
| A14 | 部分撮影・掲載候補。隔離データの未選択3件と、Puzzle・Nova Interactiveの0件、0件の説明とClear filtersが読める。画像にURLや接続元は映らないため、独立した隔離環境であることと解除後の3件への復帰は実走記録で照合する。 | 3件：[05-isolated-three.jpg](../../_images/verification-20261004/app-20261004-05-isolated-three.jpg)。0件：[05-isolated-zero.jpg](../../_images/verification-20261004/app-20261004-05-isolated-zero.jpg) |
| A15 | 部分撮影・掲載候補。Customize → InstalledのMCP Serversに既存Playwright、有効なスイッチ、緑の状態アイコンが読める。詳細でLocalと起動コマンドを確認できる。Connectedの文字は画像に映らない。実走ではProject settingsにMCP serversがなく、SettingsのCustomize → Go to Customizeから既存のグローバル設定を確認した。設定変更・保存なし。Settingsからの入口画像は未取得。リポジトリ定義のgithub・astro-docsの接続状態とTrust repository画面は未取得。掲載は設定部分を中心にし、過去のProjectsと個人用Skill一覧を避ける。 | 一覧：[05-mcp-installed.jpg](../../_images/verification-20261004/app-20261004-05-mcp-installed.jpg)。設定値：[05-playwright-config.jpg](../../_images/verification-20261004/app-20261004-05-playwright-config.jpg) |
| A16 | 部分撮影・検証用。PlaywrightのEvaluate JavaScriptを開いた実際のResultに、Showing 2 games、cardCount 2、Bug Buster BrainteaserとServer Siegeが読める。過去のProjects、検証者の依頼、個人の作業パスが映るため、全画面の本文掲載は不採用。掲載する場合はツール名と結果を中心に切り取る。browser_close、サーバー停止、ポートの待受なしを示す画像は未取得。 | ツール呼び出しと結果：[05-mcp-result-combined.jpg](../../_images/verification-20261004/app-20261004-05-mcp-result-combined.jpg) |
| A17 | 撮影済み・掲載候補／検証用。AppとGitHubの同一PR #15がmainへMergedになり、GitHub側でコミット20d5daaのfrontend-lint・type-check・unit-tests・frontend-testsの4ジョブ成功が読める。完全なSHAと、開始前に全CIの成功を確認した時点は実走記録で照合する。Appの掲載はPRパネルを中心にして検証者の会話を避ける。 | App：[06-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-06-pr-merged-app.jpg)。GitHub・CI：[06-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-06-pr-merged-github.jpg) |
| A18 | 修正後を撮影済み・掲載候補。暗色表示でOpen6件、上位3件と残り3件の区分、Refresh、先頭のIssue #5・#6の本文と優先理由が読める。#5は送信済みの表示になっている。全6カードは画面に収まらないため、順序と本文の全件照合は実走記録で確認する。共有保存後のマージ、拡張の承認、別セッションでの再利用はA20・A21・A33へ分けて記録した。 | 主候補：[07-canvas-readable.jpg](../../_images/verification-20261004/app-20261004-07-canvas-readable.jpg)。追加レビュー前の証拠：[07-canvas-initial-layout.jpg](../../_images/verification-20261004/app-20261004-07-canvas-initial-layout.jpg) |
| A19 | 最終版を撮影済み・掲載候補。PR #17のコミット差分で保存先extension.mjsの全パス、543行の追加、READMEを含む2ファイルのツリーが読める。別画像でREADMEの再利用手順1〜3と13行追加・1行削除を取得済み。画像内に合計556行追加・1行削除は表示されていないため、合計は実走記録で照合する。コード全文とREADME末尾の状態保存説明は画面に収まらない。本文は保存先と構成を示す範囲へ切り取る。初回PRのlint修正前の差分は記録のみへ変更した。 | 保存先の主候補：[07-changes-canvas-final.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas-final.jpg)。READMEの補足：[07-changes-canvas-readme.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas-readme.jpg)。修正前の証拠：[07-changes-canvas.jpg](../../_images/verification-20261004/app-20261004-07-changes-canvas.jpg) |
| A20 | 部分撮影・掲載候補。再表示したCanvasでOpen6件と#5・#6の有効な追加ボタンを読める。全カードの有効状態は撮影者の実走記録で確認する。Issue #1のカードは本文・優先理由・追加ボタンの全体を別画像で取得済み。受領画像では左に本文全文と受領のみの応答、右に#1のタイトルと優先理由が映るが、通知の冒頭は上端で切れている。受講者向けには会話と対象カードを残し、上部のセッション名と下部の入力設定を切り取る。mainからの新worktreeという開始条件と各1回の送信・受領は実走記録で照合する。 | 本文受領の主候補：[07-search-issue-receipt.jpg](../../_images/verification-20261004/app-20261004-07-search-issue-receipt.jpg)。再表示の補足：[07-canvas-reopened.jpg](../../_images/verification-20261004/app-20261004-07-canvas-reopened.jpg)。対象カードの補足：[07-canvas-search-card.jpg](../../_images/verification-20261004/app-20261004-07-canvas-search-card.jpg) |
| A21 | 撮影済み・補足候補。Repository trustに.github/github-app.yml、database-explorerとpriority-kanbanの保存先、Accept for new sessionsが読める。撮影者の報告ではReview repository contentを開いて内容を確認してから承認した。受講者向けに使う場合はダイアログへ切り取り、背景の会話とPRを除く。 | 承認前：[07-canvas-trust.jpg](../../_images/verification-20261004/app-20261004-07-canvas-trust.jpg) |
| A22 | 撮影済み・掲載候補。検索sErVeRだけの2件、Strategy・GitHub Gamesとの併用で1件のServer Siegeと評価3.3、no-such-titleによる0件と空状態メッセージが読める。空の検索欄・未選択の21件も取得済み。主候補は併用1件と0件、初期状態と2件は補足にする。画像は詳細リンクが画面外で、解除操作や前後の空白処理は静止画だけでは確認できない。MCPの0件確認は別の検索語なので、同じ入力の連続画面として扱わない。下端の浮いた操作表示を避けて切り取る。 | 主候補：[07-search-combined.jpg](../../_images/verification-20261004/app-20261004-07-search-combined.jpg)、[07-search-zero.jpg](../../_images/verification-20261004/app-20261004-07-search-zero.jpg)。補足：[07-search-default.jpg](../../_images/verification-20261004/app-20261004-07-search-default.jpg)、[07-search-two.jpg](../../_images/verification-20261004/app-20261004-07-search-two.jpg) |
| A23 | 部分撮影・掲載候補。検索PR #18のマージ後のCanvasで同じリポジトリ、Refresh issues、Open5件と先頭のIssue #5を読める。全5カードは画面内に収まらないため、#1の除外は実走記録で照合する。更新前後の件数は6件と5件の画像で比較できる。掲載は右側の見出し・Refresh・件数・先頭カードに絞り、左側のMCP報告を除く。 | 更新後：[07-canvas-after-search-merge.jpg](../../_images/verification-20261004/app-20261004-07-canvas-after-search-merge.jpg)。6件の比較：[07-canvas-reopened.jpg](../../_images/verification-20261004/app-20261004-07-canvas-reopened.jpg) |
| A24 | 部分撮影・掲載候補。New automationのManual、Run in the cloudの無効なスイッチ、読み取り専用プロンプト、New worktree、Create and runの案内が読める。プロジェクト名の末尾は省略されているため、正しいコピーの選択は実走記録で照合する。ダイアログと実行の案内へ切り取り、過去のProjectsを除く。設定画像自体は実行開始やSucceededの証拠にはしない。 | 主候補：[08-automation-create-and-run.jpg](../../_images/verification-20261004/app-20261004-08-automation-create-and-run.jpg)。設定前段階の記録：[08-automation-settings.jpg](../../_images/verification-20261004/app-20261004-08-automation-settings.jpg) |
| A25 | 撮影済み・掲載候補／検証用。Recent runsに今回のAutomation、Local、53秒、緑の成功アイコンと対象リポジトリが読める。Succeededの文字は画像内になく、状態名は撮影者の実走確認で照合する。報告ではJSTの取得時点と対象期間、マージ済みPR #13・#14・#15・#17・#18の5件、Open Issue #2〜#6の5件を読める。URLのリンク先と日時のGitHub API照合は実走記録で確認済みという撮影者の報告を根拠とする。成功状態は今回の行へ、報告内容は表へ切り取り、過去の実行を除く。 | 主候補：[08-automation-succeeded.jpg](../../_images/verification-20261004/app-20261004-08-automation-succeeded.jpg)、[08-automation-result-issues.jpg](../../_images/verification-20261004/app-20261004-08-automation-result-issues.jpg)。対象と取得時点の補足：[08-automation-result-prs.jpg](../../_images/verification-20261004/app-20261004-08-automation-result-prs.jpg) |
| A26 | 撮影済み・掲載候補／補足候補。RawのapplyToと対象ファイルは読め、Rich textで冒頭のメタデータが隠れる状態も取得済み。Drizzleを再撮影し、Rich textのTestingにunit-tests.instructions.mdのリンク名全文が読める。相対リンクの記法そのものをRawで示す画像とリンク遷移の再操作は未取得で、表示証拠として扱う。Drizzleの補足画像はTestingの見出しとリンク部分へ切り取り、無関係なNode.jsや型検査の説明を除く。 | 主候補：[03-unit-test-applyto.jpg](../../_images/verification-20261004/app-20261004-03-unit-test-applyto.jpg)。リンク表示の補足：[03-drizzle-links-final.jpg](../../_images/verification-20261004/app-20261004-03-drizzle-links-final.jpg)。表示状態の比較：[03-unit-test-instructions.jpg](../../_images/verification-20261004/app-20261004-03-unit-test-instructions.jpg)。右端が切れた旧証拠：[03-drizzle-links.jpg](../../_images/verification-20261004/app-20261004-03-drizzle-links.jpg) |
| A27 | 撮影済み・掲載候補。Publisherを返す関数のdb引数、戻り値、TSDocの説明全文が読める。過去のProjectsや個人の作業パスを避け、規約更新セッションのコード例を中心にした掲載を推奨。ファイルを変更していないことは実走記録で確認する。 | [03-code-example.jpg](../../_images/verification-20261004/app-20261004-03-code-example.jpg) |
| A28 | 撮影済み・掲載候補。Issue #7の計画中の質問、ORの回答候補、Continueが読める。実走では既定のOR選択を維持してContinueで回答した。過去のProjectsを避け、質問と回答操作を中心にする。 | [04-plan-question.jpg](../../_images/verification-20261004/app-20261004-04-plan-question.jpg) |
| A29 | 撮影済み・検証用。開発URLとShell session endedが読める。過去のProjectsとAIの結果説明を含むため、画面全体の本文掲載は不要。ポートの待受状態や全検査の成功は、別の実走記録で確認する。 | [04-run-stopped.jpg](../../_images/verification-20261004/app-20261004-04-run-stopped.jpg) |
| A30 | 撮影済み・掲載候補。PR #15のReady to mergeのメニューと無効状態のAgent mergeスイッチが読める。実走では最新コミットのCI全成功を確認してからスイッチを選ぶと、即Mergedへ移行した。4項目の権限メニューは未確認。掲載は対象PRとメニューを中心にし、検証者の会話を避ける。 | [06-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-06-agent-merge-before.jpg) |
| A31 | 初回失敗、自動修正後、追加レビュー後を撮影済み。初回404と自動修正後の薄い文字は検証用で、受講者向け掲載は不採用。コントラストと通知文の追加レビュー後の掲載候補はA18に記載。実走で上位 #5・#2・#1、残り #6・#3・#4を確認済み。共有PR #17のCI全成功・Merged、最終保存差分、別セッションでの再利用はA19・A20・A33へ分けて記録した。 | 初回失敗：[07-canvas-initial-error.jpg](../../_images/verification-20261004/app-20261004-07-canvas-initial-error.jpg)。追加レビュー前：[07-canvas-initial-layout.jpg](../../_images/verification-20261004/app-20261004-07-canvas-initial-layout.jpg)。追加レビュー後：[07-canvas-readable.jpg](../../_images/verification-20261004/app-20261004-07-canvas-readable.jpg) |
| A32 | 修正後を部分撮影・検証用。Issue #6の本文・受け入れ条件と受領のみの応答が読める。共有保存前の実走では事実を伝える通知から1クリックで本文全文1回・受領1回となり、Refresh後も#5・#6のボタンが無効なまま、Gitの差分なしを確認済み。画像は通知の冒頭が画面外で、右側はFetching途中、左側には旧コピーが映る。受講者向けに使う場合は会話部分へ切り取る。両カードの無効状態を同時に示す画像は未取得。 | 本文と受領の証拠：[07-canvas-receipt.jpg](../../_images/verification-20261004/app-20261004-07-canvas-receipt.jpg) |
| A33 | 撮影済み・検証用。共有PR #17のAgent merge Off、App・GitHub双方のMergedが読める。GitHub画像ではコミットf5a8a2eとfrontend-lint・type-check・unit-tests・frontend-testsの4ジョブ成功を確認できる。開始前のCI全成功と完全なSHAの照合は実走記録で確認する。第6章と同じ操作を繰り返すため本文の主候補には追加しない。 | マージ前：[07-canvas-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-07-canvas-agent-merge-before.jpg)。App：[07-canvas-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-app.jpg)。GitHub：[07-canvas-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-07-canvas-pr-merged-github.jpg) |
| A34 | 撮影済み・補足候補。Clear filtersで検索語も解除する質問、推奨選択肢A、Continueが読める。受講者向けに使う場合は質問と回答操作へ切り取り、ツール履歴を除く。質問画像自体は回答送信や計画承認の証拠にはしない。検索のMCP確認は終了したという撮影者の報告があり、結果はA36で別に記録する。 | 設計質問：[07-search-plan-question.jpg](../../_images/verification-20261004/app-20261004-07-search-plan-question.jpg) |
| A35 | 部分撮影・補足候補。Uncommitted 5とindex.astroの差分に、検索ラベル、入力のid、aria-controls、data-testid、空状態文の変更を読める。正規化ヘルパーとAND判定の実装全体は画面外なので、計画どおりの処理をすべて確認した証拠にはしない。PR作成前の撮影時点は実走記録で区別する。 | [07-changes-search.jpg](../../_images/verification-20261004/app-20261004-07-changes-search.jpg) |
| A36 | 部分撮影・検証用。Playwrightの呼び出し一覧とAIの結果表に2件・1件・0件・解除後21件の報告、評価、詳細URLが読める。個別ツールのResultは展開されておらず、解除や停止の実行をこの画像だけでは独立して確認できない。詳細リンクは手動MCPでクリックしていないという記載も読める。技術情報と未コミットの差分が多いため本文への掲載は不要。 | [07-search-mcp-result.jpg](../../_images/verification-20261004/app-20261004-07-search-mcp-result.jpg) |
| A37 | 撮影済み・検証用。検索PR #18のAgent merge Off、App・GitHub双方のMerged、GitHubのコミットf516e73とCI4ジョブ成功が読める。開始前のCI全成功と完全なSHAは実走記録で照合する。第6章と同じ操作なので、本文の主候補には追加しない。 | マージ前：[07-search-agent-merge-before.jpg](../../_images/verification-20261004/app-20261004-07-search-agent-merge-before.jpg)。App：[07-search-pr-merged-app.jpg](../../_images/verification-20261004/app-20261004-07-search-pr-merged-app.jpg)。GitHub：[07-search-pr-merged-github.jpg](../../_images/verification-20261004/app-20261004-07-search-pr-merged-github.jpg) |


## 現時点の掲載案

全章の実走と不足画像の再取得を終え、取得済み95枚を確認しました。本文の主候補30枚と補足候補22枚を合わせた掲載可は52枚、要再撮影は1枚、記録のみは42枚です。主候補30枚のうち23枚は切り取りを条件とし、7枚は元画像をそのまま使える候補です。画像の加工や受講者原稿への挿入は行っていません。

全95枚はJPEGとして正常に読み込め、拡張子の不一致もありません。寸法・容量・ハッシュと掲載判定は[image-inventory.json](../../_images/verification-20261004/app-20261004-image-inventory.json)、掲載位置と条件は本書の掲載選定案に記載しています。要再撮影として残るのは公開テンプレートの入口1枚です。Drizzleのリンク表示とCanvasの最終差分は取得済みで、以前の部分画像は記録のみへ変更しました。

共有PR #17と検索PR #18のマージ、別セッションでのCanvas再利用と更新、第8章の設定・成功状態・報告内容を撮影済みです。Succeededという状態名とGitHub APIとの照合は撮影者の実走記録を根拠とし、画像だけで独立して確認できたとは扱いません。Plan選択メニューとReview planの承認選択肢は未撮影のまま残しています。

全コースの公開案は、現在の30枚に公開テンプレートの入口1枚を加えたスクリーンショット31枚と、既存の概念図4点です。第7章のPlan選択と承認は第4章の操作説明を参照する条件で画像の重複を避けます。固有の承認画面が必要なら追加撮影し、枚数も見直します。

既存の画像掲載29箇所は、原稿の行・画像ファイル・役割と一致することを再確認しました。E17・E25・E26の重複掲載の削除候補3件を維持します。概念図4点は操作画面と役割が異なるため維持候補です。画像を省く箇所でも操作と意図の説明は残します。


## 撮影と掲載の確認

- 課題のセッション、Issue、PR、コピー先のリポジトリが確認できる画面を使用します。同じファイル名だったChangesやIssue画面も、別の課題の画面を流用しません。
- 必要な操作と結果が読める範囲を残します。関係のない利用枠警告、別課題の会話、指示ファイルを中心にした画像にはしません。認証情報は写しません。
- 旧版との比較説明を受講者本文へ追加せず、どこを見て何を判断するかを画像と説明で示します。
- サーバーやブラウザーを閉じる前に結果画面を取得し、その後の終了は検証証拠として記録します。
- CIやAutomationは表示だけで正しさを判定せず、PR番号、最新コミット、実行結果、対象期間、一覧・件数の照合値も実走記録に残します。
- E17、E25、E26の掲載を外すかは、代わりの画像と参照先で手順を追えることを確認してから決めます。概念図は、操作を説明する実画面とは別の役割を保ちます。
