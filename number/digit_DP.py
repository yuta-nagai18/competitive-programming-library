# Typical DP Contest E

D=int(input())
N=input()
m=10**9+7
dp=[[[0]*D for _ in range(2)] for _ in range(len(N)+1)]
dp[0][0][0]=1

for i in range(len(N)):
    for j in range(D):
        for k in range(10):
            dp[i+1][1][(j+k)%D]+=dp[i][1][j]%m
        num=int(N[i])
        for k in range(num):
            dp[i+1][1][(j+k)%D]+=dp[i][0][j]%m
        dp[i+1][0][(j+num)%D]+=dp[i][0][j]%m

print((dp[-1][0][0]+dp[-1][1][0]-1)%m)


# dp[i][smaller] := i桁目まで決めた時の暫定の答え
# ただし smallerがTrue(1)ならNより小さい場合を考え、
#       smallerがFalse(0)ならNと同じ場合を考える

# 桁DPの遷移
# dp[i][True] からはdp[i+1][True]にのみ遷移
# (i桁目まででNより小さいなら i+1桁目をどのように選んでもNより小さい）
# Nと同じにはならないので、dp[i][True]からはdp[i+1][False]への遷移は起きない

# dp[i][False] からはdp[i+1][True]へ遷移
# (i桁目までNと同じで、i+1桁目はNより小さい数の時)

# dp[i][False] からdp[i+1][False]へ遷移
# (i桁目までNと同じで、i+1桁目もNと同じ数の時)

#####################################################
# 今回の問題
# N 以下の正整数で十進法表記したときの各桁の数の和がDの倍数であるものの個数

# dp[i][smaller][j]: i桁目までの各桁の数の和がmodDでjとなる数の個数　　　　
# ただし smallerがTrue(1)ならNより小さい場合を考え、
#       smallerがFalse(0)ならNと同じ場合を考える

# 遷移  (NiはNのi桁目の数)
# dp[i+1][True][(j+k)%D]+=dp[i][True][j] (k=0,1,2,…,9)
# dp[i+1][True][(j+k)%D]+=dp[i][False][j] (k=0,1,2,…,Ni-1)
# dp[i+1][False][(j+Ni)%D]+=dp[i][False][j]

# 答えは、　　　NがDの倍数か　　　 ：dp[n][0][0] (nはNの桁数)
# 　　　 N以下の数がいくつDの倍数か：dp[n][1][0]
# 　の和から1を引く (dp[n][1][0]に0のときが含まれている(今回は自然数なので除く))

# 初期化でdp[0][0][0]=1 としているのは、i=0(まだ数字を1つも選んでいない)、
# smaller=0(まだNを超える可能性も下回る可能性もなく、ぴったりNのルートにのっている)、
# j=0(まだ何も足していないので各桁の和%Dは0)
# 最初はNの上界を意識している状態から始め、途中でNのその桁の数字より小さい数
# を選んだ時に初めてsmaller=1の世界へ分岐していく



# 参考
# https://algo-logic.info/digit-dp/