# 六角形グリッドの場合

import sys
sys.setrecursionlimit(10**6)
N=int(input())
kuro=set()
for i in range(N):
    x,y=map(int,input().split())
    x+=1000
    y+=1000
    kuro.add((x,y))


def dfs(i,j):
    visited[i][j]=True
    for i1,j1 in [[i-1,j-1],[i-1,j],[i,j-1],[i,j+1],[i+1,j],[i+1,j+1]]:
        if not (0<=i1<2002 and 0<=j1<2002):
            continue
        if (i1,j1) not in kuro:
            continue
        if not visited[i1][j1]:
            dfs(i1,j1)

visited=[]
for i in range(2002):
    visited.append([False]*2002)

ans=0
for i in range(2002):
    for j in range(2002):
        if not visited[i][j] and (i,j) in kuro:
            dfs(i,j)
            ans+=1
print(ans)
