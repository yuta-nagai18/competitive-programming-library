#累積和を用いたDP高速化 ABC248-C
N,M,K=map(int,input().split())
m=998244353
#dp[i][j] i番目まで決めたとき、総和がjになる場合の数
#O(NK)解法 (累積和で高速化)
dp=[]
for i in range(N+1):
    dp.append([0]*(K+1))

dp[0][0]=1

for i in range(1,N+1):
    #cum[j]:(i-1番目までについて）総和が0~jの場合の数の総和
    if i==1:
        cum=[1]
    else:
        cum=[0]
    for j in range(1,K+1):
        cum.append(cum[-1]+dp[i-1][j])
    for j in range(1,K+1):
        dp[i][j]+=cum[j-1]
        if j-M-1>=0:
            dp[i][j]-=cum[j-M-1]
        dp[i][j]%=m

ans=0
for i in range(K+1):
    ans+=(dp[-1][i])%m

print(ans%m)