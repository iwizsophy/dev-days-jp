# 日本語の演習本文

[ブラウザー用の目次](../../website/ja/workshops/index.html)から、3コースの概要・本文・前後の章へ移動できます。

- [Copilot App](app/README.md)：概要＋演習0～8。上流の日本語版を取り込み。
- [Tailspin Toys CLI](cli/README.md)：概要＋演習0～8。上流の日本語版を取り込み。
- [Mona Mayhem](mona-mayhem/00-overview.md)：概要を含む全7章。VS Code・CLI 両トラックを英語から翻訳。

自然言語プロンプトは日本語化しています。実行コマンド、ファイル名、型名、サンプルコードの識別子は原形を保っています。スクリーンショットは元の英語 UI のままです。App・CLI の利用条件と組織ポリシーは2026年9月8日に確認した公式情報で補正しました。Mona Mayhem のコマンド等の補正は本文中に明記しています。

参照元・コミットは [sources.json](sources.json)、原本の利用条件は [Copilot Workshops の MIT ライセンス](licenses/copilot-workshops.txt)と [Mona Mayhem の MIT ライセンス](licenses/mona-mayhem.txt)に保存しています。このコピーは非公式です。

UI が教材と異なるときは [CLI の補助手順](../../website/ja/handson-guide.html)を使います。2026年9月8日に `iwizsophy` の専用非公開リポジトリで CLI の主要演習を実行し、2本の PR と CI 成功まで確認しました。実機で見つかった差分も本文に反映しています。[検証記録と未確認の範囲](verification-2026-09-08.md)を参照してください。Copilot App と Mona Mayhem の実アカウントでの完走は未検証です。

## 更新と再生成

Markdown をこのディレクトリで編集し、リポジトリのルートで次を実行します。

```sh
python -m pip install --target .workshop-tools -r scripts/requirements-workshops.txt
python scripts/build_workshops.py
```

HTML は `website/ja/workshops/` に生成されます。通常の閲覧時には Python の HTTP サーバー以外のビルドやネットワーク取得は不要です。再生成時に、サイト全体の内部リンク、アンカー、画像参照を確認します。

上流を更新するときは `sources.json` のコミットとの変更を確認し、本文・プロンプト・画像を更新してから参照コミットを変更してください。上流の取り込み直後にローカルの利用条件補正を失わないよう、差分をレビューします。新しい章を追加した場合も HTML を再生成してください。
