# LIS (最長増加部分列)の長さを求める

from bisect import bisect_left,bisect_right

N=int(input())
a=list(map(int,input().split()))

# dp[j]: 最初のi項のみを考えた場合の単調増加な部分列であって
# 長さがj+1であるようなもののうち、その最後の要素の最小値
dp=[10**20]*N
for i in range(N):
    pos=bisect_left(dp,a[i])
    dp[pos]=a[i]

ans=0
for i in range(N):
    if dp[i]!=10**20:
        ans=i+1
print(ans)    

# https://tech.aru-zakki.com/python-lis-how-to/