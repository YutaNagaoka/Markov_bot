# Markov_bot

## 実行フロー

dialogue.pyを実行

↓

Bot2_neoをインスタンス化

↓

exec_julius.shを実行してjuliusを起動

↓

呼びかけを解析して"ラピロ"と言っていたらcall_jtalk.shを通してopenjtalkから発話

"終わり"と言っていたらプロセスを終了

↓

Finish

## 参考文献

マルコフ連鎖によるbot: https://github.com/BcRikko/markovchain_python3

JuliusをPythonから利用:http://blog.livedoor.jp/sce_info3-craft/archives/9248622.html

OpenJtalkの利用: http://www.raspberrypirulo.net/entry/2017/08/29/%E9%9F%B3%E5%A3%B0%E5%90%88%E6%88%90%E3%82%92%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%28Open_JTalk%29

Python3.6.4ドキュメント: https://docs.python.jp/3/index.html#

このプロジェクトのリポジトリ: https://github.com/YutaNagaoka/Markov_bot
