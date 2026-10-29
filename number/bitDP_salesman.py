#bitDP 典型アルゴリズム-C
N=int(input())
dist=[]
for i in range(N):
    A=list(map(int,input().split()))
    dist.append(A)

# dp[i][j]: すでに訪れた都市の集合がi(ビットで集合を表現)であって、
# 最後にいる都市がjであるときの、合計コストの最小値
dp=[]
for i in range(2**N):
    dp.append([10**20]*N)
#都市0をスタートとする
dp[1][0]=0

for s in range(2**N):
    for u in range(N):
        for v in range(N):
            #集合s (既に訪れた都市)のうちuを訪問済み、vを未訪問のとき
            if s>>u & 1 and not (s>>v & 1):
                #集合sにvを追加
                new_s=s | 1<<v
                dp[new_s][v]=min(dp[new_s][v],dp[s][u]+dist[u][v])

# dp[-1][i]は全ての都市を通って最後に都市iにいる最短距離
ans=10**20
for i in range(N):
    ans=min(ans,dp[-1][i]+dist[i][0])

print(ans)


# 集合sに都市uが含まれているかの判定
# s=5 (101) ({0,2}都市0,2)という集合に都市u=1が含まれているかの判定
# 最終的には、if (s >> u) & 1: 含まれる
# s >> u・・・sのビット列をu桁だけ右にシフト 
# (判定したいu桁目のビットを一番右の桁(0桁目)に移動)
#  101 >> 1 ⇒ 010　(元々1桁目だった0が0桁目(右端)に移動できた)
# & 1・・・右シフトで0桁目に来たビットが1か0か判定
# &(ビット論理積AND) 1&1=1, 0&1=0
# 010 & 001 (1) ⇒000(0)　(u=1は集合sに含まれない)
# 1のとき元のu桁目のビットが1だったので都市uは集合sに含まれる

# まとめ
# 集合sに都市uが含まれるか　if (s >> u) & 1 (bitが立ってるか))
# 集合sに都市uを追加　　s | (1 << u)
# 集合sから都市uを削除　s & ~(1 << u)

# ~ : NOT演算 0は1、1は0へとbitを反転させる

# i&(1<<j)
# https://algo-method.com/tasks/1145k6W5/editorial

