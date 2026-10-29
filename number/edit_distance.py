# 編集距離(レーベンシュタイン距離)

S=list(input())
T=list(input())
S=[""]+S
T=[""]+T

dp=[]
for i in range(len(S)):
    dp.append([10**20]*(len(T)))

for i in range(len(S)):
    dp[i][0]=i
for i in range(len(T)):
    dp[0][i]=i

for i in range(1,len(S)):
    for j in range(1,len(T)):
        dp[i][j]=min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1)
        if S[i]==T[j]:
            dp[i][j]=min(dp[i][j],dp[i-1][j-1])
        else:
            dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1)

print(dp[-1][-1])

# 挿入、削除、置換という編集を最小で何回すればSがTに一致するか
# 鉄則B20