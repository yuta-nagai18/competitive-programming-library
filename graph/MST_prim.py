# プリム法

import heapq
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    u,v,c=map(int,input().split())
    graph[u].append((v,c))
    graph[v].append((u,c)) 

used=[False]*N
used[0]=True

q=[]
for j,c in graph[0]:
    heapq.heappush(q,(c,j))

ans=0
while len(q)>0:
    c,i=heapq.heappop(q)
    if used[i]:
        continue
    used[i]=True
    ans+=c
    for j,c in graph[i]:
        if used[j]:
            continue
        heapq.heappush(q,(c,j))

print(ans)


# 典型アルゴリズム問題集F-最小全域木問題 verify
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f