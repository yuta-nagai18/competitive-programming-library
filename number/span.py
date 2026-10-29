# スパン 　(i日目 (i = 1 ~ N-1) について、
# 最後にその日よりも要素が小さかった日からi日目までの日数)

from collections import deque

N=int(input())
A=list(map(int,input().split()))

# (値, インデックス) 
s=deque()
# 左端よりも小さい(-1みたいな負の数を番兵とする)
s.append((-1,-1))

ans=[]
for i in range(N):
    while s[-1][0]>=A[i]:
        s.pop()
    ans.append(i-s[-1][1])
    s.append((A[i],i))

# 本問ではi=1~N-1なので最初は除く
for a in ans[1:]:
    print(a)