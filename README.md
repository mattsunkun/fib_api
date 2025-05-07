# Why Python
- `int` が巨大な数字に対しても可変に対応しているから。
- `numpy` を用いて高速な行列処理ができるから。
- `FastAPI` を用いた理由。
  - `doc` の自動生成により、フロントエンドなどとの連携がしやすいため。
  - `async` を用いて負荷分散ができるため。

# How To
## Use
Console↓
```Shell
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```
Access↓
- PROTOCOL: `http`
- ENDPOINT: `/fib`
- QUERY PARAMETER: `n`
  - `1 <= n`

## Test
```Shell
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