# Bellman Ford法

N,M,s=map(int,input().split())
edges=[]
for i in range(M):
    u,v,w=map(int,input().split())
    edges.append([u,v,w])

dist=[10**20]*N
dist[s]=0
prev=[None]*N
for i in range(N-1):
    for u,v,w in edges:
        if dist[u]!=10**20 and dist[v]>dist[u]+w:
            dist[v]=dist[u]+w
            prev[v]=u

# 負の閉路検出
for u,v,w in edges:
    if dist[u]!=10**20 and dist[v]>dist[u]+w:
        print("NEGATIVE CYCLE")
        exit()

# 到達不能のところはINFで出力
for i in range(N):
    if dist[i]==10**20:
        dist[i]="INF"

for i in range(N):
    print(dist[i])

# スタート点sからゴール点N-1までの経路復元
path=[]
pos=N-1 
while True:
    path.append(pos)
    if pos==s:
        break
    pos=prev[pos]
path.reverse()
print(len(path))
print(*path)