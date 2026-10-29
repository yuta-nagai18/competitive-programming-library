# 最長共通部分列問題(LCS)

S=input()
T=input()

# dp[i][j]: Sのi文字目,Tのj文字目までの最長の共通部分列の長さ
dp=[]
for i in range(len(S)+1):
    dp.append([-10**20]*(len(T)+1))

for i in range(len(S)):
    dp[i][0]=0
for i in range(len(T)):
    dp[0][i]=0

for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i][j-1])
        if S[i-1]==T[j-1]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)

print(dp[-1][-1])

# 鉄則A20