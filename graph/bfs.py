#BFS

#最短距離の経路の数も数える　ABC211-D
from collections import deque
N,M=map(int,input().split())
m=10**9+7
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

Q=deque()
Q.append(0)
dist=[-1]*N
dist[0]=0
cnt=[0]*N
cnt[0]=1
while len(Q)>0:
    i=Q.popleft()
    for j in graph[i]:
        if dist[j]==-1:
            dist[j]=dist[i]+1
            # +=でなくて=のほうがいいかも(BFSの場合はこのままでok)
            cnt[j]+=cnt[i]
            cnt[j]%=m
            Q.append(j)
        else:
            if dist[j]==dist[i]+1:
                cnt[j]+=cnt[i]
                cnt[j]%=m

print(cnt[-1]%m)