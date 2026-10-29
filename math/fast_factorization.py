# エラトステネスの篩を用いた高速素因数分解
def eratosthenes(N):
    isprime=[True]*(N+1)
    minfactor=[-1]*(N+1) # 整数iの最小の素因数
    isprime[1]=False
    minfactor[1]=1

    for p in range(2,N+1):
        # すでに素数でないと分かったものはスキップ
        if not isprime[p]:
            continue
        minfactor[p]=p

        # p以外のpの倍数は素数でない
        for q in range(p*2,N+1,p):
            isprime[q]=False
            # qはpで割り切れる
            if minfactor[q]==-1:
                minfactor[q]=p
                
    return minfactor

# 高速素因数分解
def factorize(n,minfactor):
    res=[]
    while n>1:
        p=minfactor[n]
        exp=0
        # pで割り切れる限り割る
        while minfactor[n]==p:
            n//=p
            exp+=1
        res.append((p,exp)) 
    return res

mx=1000
min_factor=eratosthenes(mx)

# mxまでの数を素因数分解
for i in range(2,mx+1):
    pf=factorize(i,min_factor)
    print(pf) # [(素因数, 指数), (素因数, 指数) ...]
    

# エラトステネスの篩でO(NloglogN),
# 1以上N以下の各整数iをそれぞれO(logN)で素因数分解(全部でO(NlogN))

# 1以上N以下の整数を全て素因数分解することをO(NlogN)でできる
# 愚直にそれぞれ素因数分解するとO(N*N**(1/2))