#繰り返し二乗法 ( (base^exp)%mod を計算)

def power(base,exp,mod):
    ans=1
    base%=mod
    while exp>0:
        if exp & 1:
            ans=(ans*base)%mod
        base=(base*base)%mod
        exp=exp >> 1
    return ans

#指数expを2進数で表現し、O(log(exp))で計算可能
