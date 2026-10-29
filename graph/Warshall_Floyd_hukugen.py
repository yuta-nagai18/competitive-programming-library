# Warshall Floyd法 

N,M=map(int,input().split())
dist=[]
prev=[]
for i in range(N):
    dist.append([10**20]*N)
    prev.append([-1]*N)
for i in range(N):
    dist[i][i]=0

for i in range(M):
    u,v,w=map(int,input().split())
    dist[u][v]=w
    prev[u][v]=u

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            prev[i][j]=prev[k][j]

# 到達不能はINF, 加えて負の閉路の検出も
for i in range(N):
    for j in range(N):
        if i==j and dist[i][j]<0:
            print("NEGATIVE CYCLE")
            exit()
        if dist[i][j]>=10**18:
            dist[i][j]="INF"

# 最短距離出力
for i in range(N):
    print(*dist[i])

# 経路復元
s,g=map(int,input().split())
if dist[s][g]=="INF":
    print("復元不可")
    exit()
path=[]
pos=s
while True:
    path.append(pos)
    if pos==g:
        break
    pos=prev[pos][g]
path.reverse()
print(*path)

# #頂点1から頂点Nまでの最短経路の復元 (dijkstara)
# ans=[]
# pos=N-1
# while True:
#     ans.append(pos+1)
#     if pos==0:
#         break
#     for i,j in graph[pos]:
#         if dist[pos]==dist[i]+j:
#             pos=i

# ans.reverse()
# print(*ans)


# #頂点1から頂点Nまでの最短経路の復元 (bfs)
# path=[]
# pos=N-1
# while True:
#     path.append(pos+1)
#     if pos==0:
#         break
#     for i in graph[pos]:
#         if dist[pos]==dist[i]+1:
#             pos=i

# path.reverse()
# print(*path)