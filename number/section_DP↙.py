# 区間DP(右上から左下に向かって更新していく)

N=int(input())
p=[]
point=[]
for i in range(N):
    P,A=map(int,input().split())
    P-=1
    p.append(P)
    point.append(A)

# dp[i][j]: i番目からj番目までの区間のブロックが残っているとき
# の合計得点の最大値

dp=[]
for i in range(N):
    dp.append([-10**20]*N)

dp[0][N-1]=0
for LEN in reversed(range(N)):
    for l in range(N-LEN):
        r=l+LEN
        if l>0:
            if l<=p[l-1]<=r:
                dp[l][r]=max(dp[l][r],dp[l-1][r]+point[l-1])
            else:
                dp[l][r]=max(dp[l][r],dp[l-1][r])
        if r<N-1:
            if l<=p[r+1]<=r:
                dp[l][r]=max(dp[l][r],dp[l][r+1]+point[r+1])
            else:
                dp[l][r]=max(dp[l][r],dp[l][r+1])

ans=-10**20
for i in range(N):
    ans=max(ans,dp[i][i])
print(ans)

# 鉄則A21