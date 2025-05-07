import numpy as np


def matrix_power(mat:np.ndarray, n:int, mod=None)->np.ndarray:
    """
    累積行列。log(n)で処理できる。
    mat: 累乗する対象となるベースの行列。
    n: n累乗
    mod: mod(法)を指定できる。
    """
    result = np.identity(len(mat), dtype=object)
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, mat)
            if(mod):result %= mod
        mat = np.dot(mat, mat)
        if(mod):mat %= mod
        n //= 2
    return result

def fibonacci(n: int, mod=None) -> int:
    """
    フィボナッチ数を取得する。
    n: n番目のフィボナッチ
    mod: mod(法)を指定できる。
    """
    # nは1以上にする。
    if n <= 0:
        return 0
    
    base = np.array([[1, 1], [1, 0]], dtype=object) # フィボナッチ数を求めるベースの行列
    
    result = matrix_power(base, n - 1, mod=mod) # n-1累乗する。

    return int(result[0][0]) # フィボナッチ数を返す。


if __name__ == "__main__":
    MOD = 10**9 + 7
    print(fibonacci(10, mod=MOD))