#木上の2点間の距離

#木の適当な頂点を根として決める(ここでは頂点1)　ABC209-D
#2点間の経路について、適当な頂点を経由する距離とLCAを経由する距離の偶奇は一致
from collections import deque
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

q=deque()
dist=[-1]*N
q.append(0)
dist[0]=0
while len(q)>0:
    i=q.popleft()
    for j in graph[i]:
        if dist[j]==-1:
            dist[j]=dist[i]+1
            q.append(j)

for i in range(Q):
    c,d=map(int,input().split())
    c-=1
    d-=1
    if abs(dist[c]-dist[d])%2==0:
        print("Town")
    else:
        print("Road")

# 木上のパスの最短路を求めるクエリはLCAなども用いてできる
# ABC70-Dはクエリごとに共通なため使わないでできる