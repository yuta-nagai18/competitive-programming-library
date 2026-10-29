import math

def build_segment_sieve(l,r):
    # 区間[l,r)の前計算を行い、必要なテーブル群を返す
    sr=math.isqrt(r)+1
    small=list(range(sr))
    small[0]=-1
    small[1]=-1
    large=[None]*(r-l)
    aux=[1]*(r-l)
    
    for p in range(2,sr):
        if small[p]==p:
            for q in range(p*p,sr,p):
                small[q]=p
            
            start=max((l+p-1)//p,2)*p
            for q in range(start,r,p):
                idx=q-l
                tmp=q
                while aux[idx]*aux[idx]<r and tmp%p==0:
                    if large[idx] is None:
                        large[idx]={}
                    large[idx][p]=large[idx].get(p,0)+1
                    aux[idx]*=p
                    tmp//=p
                    
    return sr,small,large,aux

def is_prime(n,l,large):
    # O(1)での素数判定
    return large[n-l] is None

def prime_factorize(n,l,sr,small,large,aux):
    # 高速素因数分解
    if large[n-l] is None:
        res={}
    else:
        res=large[n-l].copy()
    rem=n//aux[n-l]
    
    if rem>=sr:
        res[rem]=res.get(rem,0)+1
        return res
    
    while rem>1:
        p=small[rem]
        res[p]=res.get(p,0)+1
        rem//=p
        
    return res


L=999999999989
R=1000000000010

sr,small,large,aux=build_segment_sieve(L,R)

for i in range(L,R):
    # if is_prime(i,L,large):
    #     print(f"{i}は素数")
    factors=prime_factorize(i,L,sr,small,large,aux)
    pf=sorted(factors.items())
    print(pf)