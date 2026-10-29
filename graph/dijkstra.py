#Dijkstra法　O(MlogM)　鉄則A64 
import heapq
N,M=map(int,input().split())

graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    A,B,C=map(int,input().split())
    A-=1
    B-=1
    graph[A].append([B,C])
    graph[B].append([A,C])

dist=[10**20]*N
dist[0]=0

q=[]
heapq.heappush(q,(0,0))
done=[False]*N
while len(q)>0:
    d,i=heapq.heappop(q)
    if done[i]:
        continue
    done[i]=True
    for j,c in graph[i]:
        if dist[j]>dist[i]+c:
            dist[j]=dist[i]+c
            heapq.heappush(q,(dist[j],j))

#1つの頂点(ここでは1)から各頂点までの最短距離
for i in range(N):
    if dist[i]==10**20:
        print(-1)
    else:
        print(dist[i])

#頂点1から頂点Nまでの最短経路の復元
ans=[]
pos=N-1
while True:
    ans.append(pos+1)
    if pos==0:
        break
    for i,j in graph[pos]:
        if dist[pos]==dist[i]+j:
            pos=i

ans.reverse()
print(*ans)


# ➀初期化：スタートノードの値（最小コスト候補）を0，
# 他のノードの値を未定義（または∞）に設定。
# ➁確定ノードをピックアップすることができなくなるまで
# （＝変化がなくなるまで）以下のループを繰り返す：
# (i)まだ確定されていないノードのうち，最小の値を持つノードを見つけ，
# 確定ノードとする（確定フラグを立てる）。
# (ii)確定ノードからの伸びているエッジをそれぞれチェックし，
# 「確定ノードまでのコスト＋エッジのコスト」を計算し，
# そのノードの現在値よりも小さければ更新し、その頂点を探索候補に加える
# （経路情報も必要であれば，「どこから来たのか」を表す変数が確定ノードを指すようにする）。

#ある1つの頂点から各頂点までの最短経路長とその経路を求められる。