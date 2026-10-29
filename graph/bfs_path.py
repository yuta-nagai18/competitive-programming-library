#頂点1から頂点Nまでの最短経路の復元

from collections import deque

N,M=map(int,input().split())
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
while len(Q)>0:
    i=Q.popleft()
    for j in graph[i]:
        if dist[j]==-1:
            dist[j]=dist[i]+1
            Q.append(j)

#頂点1から頂点Nまでの最短経路の復元
path=[]
pos=N-1
while True:
    path.append(pos+1)
    if pos==0:
        break
    for i in graph[pos]:
        if dist[pos]==dist[i]+1:
            pos=i

path.reverse()
print(*path)

# 単純にdistの更新と同時にpre[j]=i (頂点jを更新したときの遷移元がi)
# とすれば、これが頂点jへの最短距離への遷移元を表している