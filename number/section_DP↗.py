# 区間DP (左下から右上に向かって更新していく)

N=int(input())
S=list(input())

# dp[i][j]: i番目からj番目までの区間における最長回分の長さ

dp=[]
for i in range(N):
    dp.append([-10**20]*N)

for i in range(N):
    dp[i][i]=1

for i in range(N-1):
    if S[i]==S[i+1]:
        dp[i][i+1]=2
    else:
        dp[i][i+1]=1

for LEN in range(N):
    for l in range(N-LEN):
        r=l+LEN
        if l>=r:
            continue
        if l<N-1:
            dp[l][r]=max(dp[l][r],dp[l+1][r])
        if r>0:
            dp[l][r]=max(dp[l][r],dp[l][r-1])
        if l<N-1 and r>0:
            if S[l]==S[r]:
                dp[l][r]=max(dp[l][r],dp[l+1][r-1]+2)


# for i in range(N):
#     for j in range(N):
#         if dp[i][j]==-10**20:
#             dp[i][j]="o"

# for i in range(N):
#     print(*dp[i])
    
print(dp[0][-1])

# 鉄則B21