# この教材リポジトリでの作業

- `iwizsophy/dev-days-jp` は App シナリオを主軸とする独立した教材セットです。
- 参照元の `github/dev-days`、`github-samples/copilot-workshops`、`github-samples/tailspin-toys`、`copilot-dev-days/mona-mayhem` は閲覧専用です。push、PR、Issue、コメント、設定変更を送ってはいけません。
- 参照元の履歴を merge しません。`content/ja/sources.json` の固定コミットとの差分を読み、必要な箇所だけ日本語原稿へ反映します。
- 更新元は `content/ja/` の Markdown です。`website/ja/workshops/` の HTML は `python scripts/build_workshops.py` で生成します。原稿編集と大量の生成差分は別コミットにします。
- 実走済みの CLI 独立コースと、未検証の App シナリオ・CLI 代替経路を混同しません。章別の状況は `content/ja/material/verification.md` に記録します。
- コミットの Author・Committer は `Tetsuji Kato <6571039+iwizsophy@users.noreply.github.com>` を確認します。作業ブランチを `origin/main` に追跡させません。push の依頼がある場合は送信先と同名ブランチを明示します。
