# App シナリオを主軸とする日本語教材セット

受講者は、[参加者の入口](../../website/ja/index.html) → [Appの演習目次](../../website/ja/workshops/index.html) → 第1〜9章の順序で進めます。操作中に UI の表示が教材と異なるなどして進行が止まった場合は、自己判断で進めず、講師とともに現行 App の操作経路を確認してください。

## ディレクトリ構成と各原稿の役割

本教材では既存のファイルを再編集する形で保守しており、既存リンクを壊さないよう参考コースの配置や URL も維持しています。なお、スライド、動画、画面キャプチャ画像などの一部素材は原本の言語（英語）を保っています。

| 原稿パス | 役割と位置づけ | 留意点 |
| :--- | :--- | :--- |
| `entry.md`<br>`preparation.md` | 参加者の入口と事前準備 | `website/ja/index.html` と `handson-guide.html` の生成元 |
| [`disclaimer.md`](disclaimer.md) | 利用上の注意と免責事項 | Web版と両PDFの演習前に共通原稿を掲載 |
| `app/` | **本編**（上流の日本語 App シナリオ） | 画像と現行 UI の突き合わせ確認が必要 |
| `material/instructor.md` | 講師ガイド | 講師の事前準備、180分の時間配分、当日の対処手順 |
| `material/ui-check.md` | UI 確認表 | メニューや右クリック等の現行操作経路と確認対象画像 |
| `material/verification.md` | 章別検証記録 | App 現行 UI の実走結果と緊急対応の検証状況 |
| `material/emergency-cli.md`<br>`material/continuation.md` | **講師専用の緊急対応手順** | 作業保全用であり、App 演習の完了には数えない |
| `cli/`<br>`mona-mayhem/` | 独立した参考コース | 補講用の資料であり、本編の必須経路には含めない |
| `verification-2026-09-08.md` | 過去の CLI 独立コース実走記録 | CLI 単体での実走結果であり、App 完走の証拠ではない |

## 出典と更新方針

本教材の開催資料は[github/dev-days](https://github.com/github/dev-days)、演習の主軸は[github-samples/copilot-workshops](https://github.com/github-samples/copilot-workshops)のApp版に基づいています。演習用テンプレートは[iwizsophy/dev-days-tailspin-template](https://github.com/iwizsophy/dev-days-tailspin-template)で配布し、[github-samples/tailspin-toys](https://github.com/github-samples/tailspin-toys)を基に作成・改訂しています。App教材とテンプレートの出典、各リポジトリのライセンスと著作権表示は[出典とライセンス](credits.md)にまとめました。

参照コミット、対象ファイル、および独自追加の範囲は[sources.json](sources.json)に記録しています。[Dev Days](licenses/dev-days.txt)、[Copilot Workshops](licenses/copilot-workshops.txt)、[Tailspin Toys](licenses/tailspin-toys.txt)のライセンス原文を保持しています。独立した参考コースの[Mona Mayhem](licenses/mona-mayhem.txt)のライセンス原文も保持しています。

画像の撮影条件や検証履歴は `sources.json` の `ui_captures` に保持します。受講者向けに表示する補足は `ui_captions` に記載し、操作に必要な画面差や対象の違いだけを簡潔に説明します。

### 参照元の取り扱い原則
参照元リポジトリには、push、Pull Request、Issue、コメントを一切送信しません。また、上流の履歴を merge せず、本リポジトリを独立して保守します。

### 更新手順
1. **差分の確認**：前回参照したコミットと更新候補の差分を読みます。比較は閲覧または一時的な clone で行い、本教材の追跡先には設定しません。
2. **原稿への反映**：必要な差分だけを原稿へ反映し、講師向け緊急対応との整合性も確認します。
3. **メタデータの記録**：参照ファイルとコミットを `sources.json` に記録します。その際、原文確認日と実際の実走日を区別して記載します。
4. **生成と検査**：HTML を再生成して内部リンクやアンカーを検査し、実走結果を章別に記録します。
5. **コミットの分離**：原稿・構成の変更と、再生成による HTML の変更は、必ず別々のコミットに分離します。Issue を用いる場合も `iwizsophy/dev-days-jp` のみを対象とします。

## 教材の再生成と品質検査

本教材では、Web サイトだけでなく、画像込みの参加者用 PDF および講師用別冊も同じ原稿から一元生成できます（詳細は [PDF 教材の作成と配布](../../docs/pdf-distribution.md) を参照）。Web サイトと PDF をまとめて更新する場合は `python scripts/build_distribution.py` を実行します。

Web サイトの HTML のみを更新する場合は、次のコマンドを実行します。

```sh
python -m pip install --target .workshop-tools -r scripts/requirements-workshops.txt
python scripts/build_workshops.py
```

- 原稿のみの変更であれば、2行目の `build_workshops.py` のみ実行すれば足ります。
- 演習と補助資料の生成先は `website/ja/workshops/` です。入口と事前準備は `website/ja/index.html` と `website/ja/handson-guide.html` へ生成します。ビルド処理は外部ネットワークへ接続せず、内部リンク、アンカー、画像パスの存在を検査します。
- 生成された HTML を直接手作業で編集することは避けてください。
- 画像は原稿用と配布サイト用に保持し、不要な再保存による無用な差分を発生させないようにします。
