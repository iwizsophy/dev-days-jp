# App シナリオを主軸とする日本語教材セット

[参加者の入口](../../website/ja/index.html) → [App の演習目次](../../website/ja/workshops/index.html) → 演習0〜8の順に進めます。UI で止まった場合は各章の CLI 代替手順で同じ課題を続けます。

| 原稿 | 役割 |
| --- | --- |
| app/ | 本編。上流の日本語 App シナリオに CLI 代替手順と合流条件を併記 |
| material/continuation.md | 切り替え、PR・マージ、App への復帰 |
| material/instructor.md | 講師の準備、時間配分、対処手順 |
| material/verification.md | App の各章と CLI 代替経路の検証状況 |
| cli/、mona-mayhem/ | 独立した参考コース。必須経路には含めない |
| verification-2026-09-08.md | CLI 独立コースの実走記録。App 完走の証拠ではない |

既存ファイルを再編集し、参考コースも移動せず URL を保ちます。スライド、動画、画面画像は原本の言語です。

## 出典と更新方針

開催資料は `github/dev-days`、演習の主軸は `github-samples/copilot-workshops` の App 版です。[sources.json](sources.json) に参照コミット・対象ファイル・独自追加の範囲を記録します。[Copilot Workshops のライセンス](licenses/copilot-workshops.txt)と [Mona Mayhem のライセンス](licenses/mona-mayhem.txt)を保持しています。

参照元には push・PR・Issue・コメントを送信しません。上流履歴を merge せず、このコピーを独立して保守します。

1. 前回参照コミットと更新候補の差分を読みます。閲覧または一時的な clone で比較し、教材の追跡先にはしません。
2. 必要な差分だけ原稿へ反映し、CLI 代替手順との整合も確認します。
3. 参照ファイルとコミットを sources.json に記録します。原文確認日と実走日を区別します。
4. HTML を再生成してリンクを検査し、実走結果を章別に記録します。
5. 原稿・構成変更と、生成 HTML の変更を別コミットにします。Issue を使う場合は iwizsophy/dev-days-jp のみを対象にします。

## 再生成

```sh
python -m pip install --target .workshop-tools -r scripts/requirements-workshops.txt
python scripts/build_workshops.py
```

原稿の変更だけなら2行目を実行します。生成先は website/ja/workshops/ です。ビルド中は外部接続せず、内部リンク・アンカー・画像を検査します。生成 HTML の直接編集は避けてください。画像は原稿用と配布サイト用に保持し、不要な再保存による差分を作らないようにします。
