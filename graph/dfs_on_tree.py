# 木上のDFS (各頂点の根からの距離 (深さ)、各頂点を根とした部分木のサイズ)
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

def dfs(v,p,d):
    depth[v]=d
    for nv in graph[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)
    
    size[v]=1
    for nv in graph[v]:
        if nv==p:
            continue
        size[v]+=size[nv]

depth=[0]*N
size=[0]*N
dfs(0,-1,0)
print(*size)

# https://qiita.com/drken/items/a803d4fc4a727e02f7ba