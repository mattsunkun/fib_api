# How To
## Access
### Fibonacci
- URI: `https://lie-detecting-backend-mattsunkun.onrender.com/fib`
  - PROTOCOL: `http`
  - PATH: `/fib`
- QUERY PARAMETER: `n`
  - `1 <= n <= 100`


## Create Local
```Shell
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

## Test
```Shell
$ pip install -r requirements.txt
$ python test/test_main.py
```


# Why Python
- `int` が巨大な数字に対しても可変に対応しているため。
- `numpy` を用いて高速な行列処理ができるため。
- `FastAPI` を用いた理由。
  - `/docs` の自動生成により、ドキュメント生成の手間が省け、フロントエンドなどとの連携がしやすいため。
  - `async` を用いて負荷分散ができるため。


# Python File
## functions/fibonacci.py
- フィボナッチ数を計算する。
- 対数累積行列を用いて、対数時間で処理。

## main.py
- エンドポイントが格納されている。
- リテラル値はここに外出しされている。

## test/test_main.py
- テストケースが入っている。
  - フィボナッチ数列のテスト。
  - 限界値テスト。
  - メソッドテスト。
  - エンドポイントテスト。
  - パラメータテスト。

## timeout_middleware.py
- `FastAPI` での処理にタイムアウトを設定するためのクラス。