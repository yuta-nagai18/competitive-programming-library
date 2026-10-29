# 強連結成分分解

from atcoder.scc import SCCGraph

N,M=map(int,input().split())

graph=SCCGraph(N)

for i in range(M):
    u,v=map(int,input().split())
    graph.add_edge(u,v)

SCC=graph.scc()

print(len(SCC))
for i in range(len(SCC)):
    print(len(SCC[i]),*SCC[i])

    
# https://atcoder.jp/contests/practice2/tasks/practice2_g