# LISの別解 (in-place化 + セグ木)

from atcoder.segtree import SegTree

N=int(input())
a=list(map(int,input().split()))

# 座標圧縮 (jが大きい場合に備える)
a_se=sorted(set(a))
a_dic={v: i for i,v in enumerate(a_se)}
a=list(map(lambda v: a_dic[v],a))

# dp[j]: 最初のi項のみを考えた場合の単調増加な部分列であって
# 最後の要素がjであるようなもののうち、最長の長さ
dp=[0]*(N+1)
seg=SegTree(max,0,dp)

for i in range(N):
    mx=seg.prod(0,a[i])
    dp[a[i]]=max(dp[a[i]],mx+1)
    seg.set(a[i],dp[a[i]])

print(max(dp))