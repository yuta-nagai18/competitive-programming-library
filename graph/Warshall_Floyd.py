# Warshall Floyd法 

N,M=map(int,input().split())
dist=[]
for i in range(N):
    dist.append([10**20]*N)
for i in range(N):
    dist[i][i]=0

for i in range(M):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    dist[u][v]=min(dist[u][v],w)
    dist[v][u]=min(dist[v][u],w)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

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