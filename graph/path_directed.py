# 有向グラフのある点Xから点Yへのパスを出力 (閉路あってもok)

# 解法1: 経路の復元で求める方法　(BFSを使うため、最短パスとなる)
from collections import deque
N,M,X,Y=map(int,input().split())
graph=[]
graph_2=[]
for i in range(N):
    graph.append([])
    graph_2.append([])

for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph_2[v].append(u)

Q=deque()
Q.append(X)
dist=[-1]*N
dist[X]=0
while len(Q)>0:
    i=Q.popleft()
    for j in graph[i]:
        if dist[j]==-1:
            dist[j]=dist[i]+1
            Q.append(j)

#頂点Xから頂点Yまでの最短経路の復元
ans=[]
pos=Y
while True:
    ans.append(pos)
    if pos==X:
        break
    for i in graph_2[pos]:
        if dist[pos]==dist[i]+1:
            pos=i

ans.reverse()
print(len(ans))
print(*ans)


# 解法2: 木上のパスを求めるのと同じ方法
import sys
sys.setrecursionlimit(10**6)
from collections import deque
N,M,X,Y=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)

def dfs(i):
    ans.append(i)
    if i==Y:
        print(len(ans))
        print(*ans)
        return
    visited[i]=True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
    ans.pop()

visited=[False]*N
ans=deque()
dfs(X)

# アルゴ式 high_graph_search/有向グラフのパス