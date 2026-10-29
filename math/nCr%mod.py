# 1<=k<=n<=10^7 で pが素数のとき (p>n)

mx=10**7  #nの取り得る最大値
p=10**9+7

fac=[None]*mx
finv=[None]*mx
inv=[None]*mx
fac[0],fac[1]=1,1
finv[0],finv[1]=1,1
inv[0],inv[1]=0,1

for i in range(2,mx):
    fac[i]=fac[i-1]*i%p
    inv[i]=p-inv[p%i]*(p//i)%p
    finv[i]=finv[i-1]*inv[i]%p

# nCk mod p
def comb(n,k):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    return fac[n]*(finv[k]*finv[n-k]%p)%p

# 前処理 O(n), 各nCk計算 O(1)

# https://drken1215.hatenablog.com/entry/2018/06/08/210000
# https://algo-logic.info/combination/

# python実装参考 ↓
# https://wakabame.hatenablog.com/entry/2021/04/16/152855