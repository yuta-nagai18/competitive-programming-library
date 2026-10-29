# 木のEuler Tour (探索された順に頂点を出力)

import sys
sys.setrecursionlimit(10**6)
N=int(input())
graph=[]
for i in range(N):
    graph.append([])

for i in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

# 複数の分岐があるときは番号の小さい順に
for i in range(N):
    graph[i].sort()

def dfs(now,pre):
    ans.append(now+1)
    for to in graph[now]:
        if to!=pre:
            dfs(to,now)
            ans.append(now+1)

ans=[]
dfs(0,-1)
print(*ans)

# -------別解----------------------------

def dfs(i):
    ans.append(i+1)
    visited[i]=True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            ans.append(i+1)

visited=[False]*N
ans=[]
dfs(0)
print(*ans)
# ---------------------------------------

# ABC213-D
# N個の頂点に対してN-1個の辺のときのみ
# ➂ー➀ー➁ー➃　を➀から探索する (分岐では番号の小さい方を優先)
# 1 > 2 > 4 > 2 > 1 > 3 > 1