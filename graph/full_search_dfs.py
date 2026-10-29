#O(NN!) 制約2<=N<=10 ABC317-C

import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])

# i: 今いる点、s: 今いる点までの距離
def dfs(i,s):
    global ans
    ans=max(ans,s)
    visited[i]=True
    for j,c in graph[i]:
        if not visited[j]:
            dfs(j,s+c)
    visited[i]=False

ans=0
for i in range(N):
    visited=[False]*N
    dfs(i,0)

print(ans)
