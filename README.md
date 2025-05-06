# Why Python
- `int` が巨大な数字に対しても可変に対応しているから。
- `numpy` を用いて高速な行列処理ができるから。
- `FastAPI` を用いたのは、`Python` の中で一番活発なサーバーモジュールなので、メンテナンスされていると考えたため。

# How To
## Use
```

```
- ENDPOINT: `/fib`
- QUERY PARAMETER: `n`
  - `1 <= n`

## Test
```
$ pip install -r requirements.txt
$ python test_main.py
```

# Python File
## fibonacci.py
- フィボナッチ数を計算する。
- 対数累積行列を用いて、対数時間で処理。

## main.py
- エンドポイントが格納されている。
- リテラル値はここに外出しされている。

## test_main.py
- テストケースが入っている。
  - フィボナッチ数列のテスト。
  - 限界値テスト。
  - メソッドテスト。
  - エンドポイントテスト。

## timeout_middleware.py
- `FastAPI` での処理にタイムアウトを設定するためのクラス。