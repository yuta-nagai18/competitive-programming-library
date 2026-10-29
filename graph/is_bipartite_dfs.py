# 二部グラフ判定　(DFS)

import sys
sys.setrecursionlimit(10**6)

N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    a,b=list(map(int,input().split()))  
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

color=[0]*N

def dfs(i,c):
    global flag
    color[i]=c
    for j in graph[i]:
        if color[j]==c:   # 隣の頂点が同じ値を与えられている際Falseに
            flag=False
        if color[j]==0:   # 探索済みでなければ再帰する
            dfs(j,-c) # 引数に-cとすることで,cが1=>-1=>1を繰り返す

for i in range(N):
    if color[i]==0:
        flag=True
        dfs(i,1)
        if not flag:
            print("No")
            exit()
print("Yes")

# 各連結成分について二部グラフ判定が可能
# 各連結成分について全頂点を訪問するため頂点数・辺数も取得可能