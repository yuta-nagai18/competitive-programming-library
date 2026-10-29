# 木上のimos法

import sys
sys.setrecursionlimit(10**6)
N,Q=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

cnt=[0]*N

for i in range(Q):
    p,x=map(int,input().split())
    p-=1
    cnt[p]+=x

visited=[False]*N

def dfs(i):
    visited[i]=True
    for j in graph[i]:
        if not visited[j]:
            cnt[j]+=cnt[i]
            dfs(j)        

dfs(0)

print(*cnt)

# ABC138-D クエリ: 頂点pを根とする部分木に含まれる全頂点の
# cntの値にxを足す　　全操作後の全頂点のcntの値を求めよ
# いもす法の右側が常に配列の右端になっている
# 終点で-x[j]とする必要がない