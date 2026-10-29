# 各頂点の子孫の個数

import sys
sys.setrecursionlimit(10**6)
N=int(input())
# 頂点0以外の頂点の親の頂点番号 (要素数はN-1に注意)
a=list(map(int,input().split()))
# 子 → 親
graph=[]
# 子 ← 親
graph_2=[]
for i in range(N):
    graph.append([])
    graph_2.append([])

for i in range(N-1):
    graph[i+1].append(a[i])
    graph_2[a[i]].append(i+1)
    
visited=[False]*N
ans=[0]*N
def dfs(i):
    visited[i]=True
    for j in graph_2[i]:
        if not visited[j]:
            dfs(j)
            # 子jが終わったらその結果を親iに集計する
            # 子jの子孫の個数＋子j自身
            ans[i]+=ans[j]+1

dfs(0)

for a in ans:
    print(a)