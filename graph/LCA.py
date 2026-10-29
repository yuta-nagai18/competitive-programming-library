# LCA (最近共通祖先)

from atcoder.segtree import SegTree
import sys
sys.setrecursionlimit(10**6)

N=int(input())
graph=[]
for i in range(N):
    graph.append([])

for i in range(N):
    l=list(map(int,input().split()))
    for j in range(l[0]):
        graph[i].append(l[j+1])
        graph[l[j+1]].append(i)

Euler=[]
depth=[]
first=[-1]*N

def dfs(v,p,d):
    first[v]=len(Euler)
    depth.append(d)
    Euler.append(v)
    for nv in graph[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)
        depth.append(d)
        Euler.append(v)

dfs(0,-1,0)

# (depth_i, Euler_i)を格納
li=[]
for i in range(len(Euler)):
    li.append((depth[i],Euler[i]))

seg=SegTree(min,(10**20,10**20),li)

Q=int(input())
ans=[]
for i in range(Q):
    u,v=map(int,input().split())
    mn=min(first[u],first[v])
    mx=max(first[u],first[v])
    d_mn,node=seg.prod(mn,mx+1)
    ans.append(node)

for i in range(len(ans)):
    print(ans[i])