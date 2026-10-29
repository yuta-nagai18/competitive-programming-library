# k<=10^7, n<=10^9 で pが素数のとき

mx=10**6  #kの取り得る最大値
p=10**9+7

finv=[None]*mx
inv=[None]*mx
finv[0],finv[1]=1,1
inv[0],inv[1]=0,1

for i in range(2,mx):
    inv[i]=p-inv[p%i]*(p//i)%p
    finv[i]=finv[i-1]*inv[i]%p

# nCk mod p
def comb(n,k):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    ans=1
    for i in range(k):
        ans*=(n-i)
        ans%=p
    return ans*finv[k]%p

# https://algo-logic.info/combination/#