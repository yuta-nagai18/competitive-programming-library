import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    global cnt,cnt_road
    cnt+=1
    visited[i]=True
    for j in graph[i]:
        cnt_road+=1
        if not visited[j]:
            dfs(j)

visited=[False]*N
ans=0
for i in range(N):
    if not visited[i]:
        cnt,cnt_road=0,0
        dfs(i)
        #閉路の数=辺の数-頂点の数+1 (=閉路を無くすために削除する必要のある辺の最小数)
        ans+=cnt_road//2-cnt+1
        #連結している要素の全組をつなぐために追加する必要のある辺の数=全組数-辺の数
        ans+=cnt*(cnt-1)//2-cnt_road//2

print(ans)


#木: 無向グラフかつ連結かつ閉路がない(N個の頂点にN-1本の辺)

#単純無向グラフのパスグラフ判定 ABC287-C ➀辺の数がN-1、➁全頂点の次数が2以下、➂グラフが連結
# ABC231-Dも


