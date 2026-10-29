# 木上で、ある点からある点までのパスを挙げる (dfs + stack)

import sys
sys.setrecursionlimit(10**6)
from collections import deque
N,X,Y=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(N-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

def dfs(i):
    ans.append(i+1)
    if i==Y-1:
        print(*ans)
        return
    visited[i]=True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
    ans.pop()


visited=[False]*N
ans=deque()
dfs(X-1)

# ABC270-C