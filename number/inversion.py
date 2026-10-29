# 転倒数
from atcoder.segtree import SegTree

N=int(input())
a=list(map(int,input().split()))

cnt=[0]*(10**5+1)
for i in range(N):
    cnt[a[i]]+=1

seg=SegTree(lambda x,y:x+y,0,cnt)
ans=0

for i in range(N):
    ans+=seg.prod(0,a[i])
    seg.set(a[i],seg.get(a[i])-1)

print(ans)