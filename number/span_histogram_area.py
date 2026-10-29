# ヒストグラム内の最大長方形の面積

# スパン 　(i日目 (i = 1 ~ N-1) について、
# 最後にその日よりも要素が小さかった日からi日目までの日数)

from collections import deque

N=int(input())
A=list(map(int,input().split()))

# (値, インデックス) 
# 左側の個数を求める
l=deque()
l.append((-1,-1))
l_cnt=[]

# 右側の個数を求める
r=deque()
r.append((-1,N))
r_cnt=[]

for i in range(N):
    while l[-1][0]>=A[i]:
        l.pop()
    l_cnt.append(i-l[-1][1])
    # print(i-l[-1][1])
    l.append((A[i],i))

# print(10**20)

for i in reversed(range(N)):
    while r[-1][0]>=A[i]:
        r.pop()
    r_cnt.append(r[-1][1]-i)
    # print(r[-1][1]-i)
    r.append((A[i],i))

r_cnt.reverse()

ans=-10**20
for i in range(N):
    # print(A[i],l_cnt[i],r_cnt[i])
    ans=max(ans,A[i]*(l_cnt[i]+r_cnt[i]-1))

print(ans)

# アルゴ式の模範解答とは少し実装が違うので注意