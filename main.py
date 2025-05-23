from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from functions.fibonacci import fibonacci
from timeout_middleware import TimeoutMiddleware

MIN_N = 1
MAX_N = 100
FIB_PATH = "/fib"

ALLOW_PATHS:set = {FIB_PATH}
ALLOW_METHOD:list = ["GET"]

TIMEOUT = 3

app = FastAPI(
    title="数列 API",
    description="この API は数列の第n項を返すものです。",
    version="1.0.0"
)

# フィボナッチ数列を返す時の型
class FibonacciReponse(BaseModel):
    result: int


# タイムアウト処理
app.add_middleware(TimeoutMiddleware, timeout=TIMEOUT)


# CORS設定（任意のオリジンを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=ALLOW_METHOD,
    allow_headers=["*"],
)

# フィボナッチ数列バックエンド
@app.get(
        FIB_PATH, 
        response_model=FibonacciReponse, 
        description=f"フィボナッチ数列の第n項（{MIN_N}〜{MAX_N}の範囲）を取得できる。"
        )
async def get_fibonacci(n: int = Query(..., description="フィボナッチ数列の第n項")):
    if not (MIN_N <= n <= MAX_N):
        raise HTTPException(status_code=400, detail=f"nは{MIN_N}〜{MAX_N}の範囲である必要があります")
    return {"result": fibonacci(n)}

# 405 Method Not Allowed 対応
@app.middleware("http")
async def handle_method_not_allowed(request: Request, call_next):
    if (request.url.path in ALLOW_PATHS) and (request.method not in ALLOW_METHOD):
        return JSONResponse(status_code=405, content={"error": "Method Not Allowed"})
    return await call_next(request)

# 404 Not Found
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={"error": "404 Not Found"})

