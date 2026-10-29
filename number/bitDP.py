N,M=map(int,input().split())
a=[]
for i in range(M):
    A=list(map(int,input().split()))
    a.append(A)

# dp[i][s]: クーポン1~iまでの中から何枚かを選び、無料で買える品物の集合がs
# であるとき、使用したクーポンの枚数の最小値
dp=[]
for i in range(M+1):
    dp.append([10**20]*(2**N))

dp[0][0]=0

for i in range(1,M+1):
    for s in range(2**N):
        dp[i][s]=min(dp[i][s],dp[i-1][s])
        new_s=s
        #クーポンiを選択する場合
        for j in range(N):
            #集合sに品物jが含まれていない、かつクーポンiで品物jが無料で買えるとき
            if not (new_s>>j & 1) and a[i-1][j]==1:
                #集合sにjを追加
                new_s = new_s | (1 << j)
        dp[i][new_s]=min(dp[i][new_s],dp[i-1][s]+1)

if dp[-1][-1]==10**20:
    print(-1)
else:
    print(dp[-1][-1])

# まとめ

# 集合sに都市uが含まれるか　if (s >> u) & 1 (bitが立ってるか))
# 集合sに都市uを追加　　s | (1 << u)
# 集合sから都市uを削除　s & ~(1 << u)

# 鉄則A23