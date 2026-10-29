# 多始点BFS ABC383-C

from collections import deque
H,W,D=map(int,input().split())
s=[]
for i in range(H):
    S=input()
    s.append(S)

dist=[]
for i in range(H):
    dist.append([-1]*W)

# 最初にqueueに始点の頂点を全て追加、距離を0にする
Q=deque()
for i in range(H):
    for j in range(W):
        if s[i][j]=="H":
            Q.append([i,j])
            dist[i][j]=0

while len(Q)>0:
    i,j=Q.popleft()
    for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not (0<=i1<H and 0<=j1<W):
            continue
        if s[i1][j1]=="#":
            continue
        if dist[i1][j1]==-1:
            dist[i1][j1]=dist[i][j]+1
            Q.append([i1,j1])

ans=0
for i in range(H):
    for j in range(W):
        if 0<=dist[i][j]<=D:
            ans+=1
print(ans)