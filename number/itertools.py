# itertools

# ランレングス圧縮
from itertools import groupby
def run_length(S):
    return [(k,len(list(g))) for k,g in groupby(S)]

import itertools
# 配列a（要素数n）の全要素を並び替えた順列　(nPn = n! 通り)
def permutations(a):
    return list(itertools.permutations(a))


# 配列aからc個の要素を選んで並べ替えた順列 (nPc通り)
def permutations_2(a,c):
    return list(itertools.permutations(a,c))

# 配列aからc個の要素を選ぶ組み合わせ (nCc通り)
def combinations(a,c):
    return list(itertools.combinations(a,c))

# 直積
# 配列aから1つ、配列bから1つ要素を選ぶ組み合わせ (na*nb通り)
def product_2(a,b):
    return list(itertools.product(a,b))

# 配列aから1つ、配列bから1つ、配列cから1つ (na*nb*nc通り)
def product_3(a,b,c):
    return list(itertools.product(a,b,c))

# 配列a (要素数n)から1つ要素を選ぶのをcnt回繰り返した組み合わせ
# 重複順列と同じ
def product_a(a,cnt):
    return list(itertools.product(a,repeat=cnt))

# 配列a (要素数n)から1つ要素を選ぶのをcnt回繰り返し、重複を消す
# 重複組み合わせ
def product_a_c(a,cnt):
    return list(itertools.combinations_with_replacement(a,cnt))   
