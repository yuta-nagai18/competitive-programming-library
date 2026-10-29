#メモ化再帰 ABC275-D, ABC340-C
#まずは素直に実装してから@cacheを追加
import sys
sys.setrecursionlimit(10**6)
from functools import cache
@cache
def f(n):
    if n==0:
        return 1
    else:
        return f(n//2)+f(n//3)