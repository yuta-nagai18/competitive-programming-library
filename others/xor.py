# 0^1^2^...^n の計算

def xor_calc(n):
    if n%2==0:
        cnt=n//2
        if cnt%2==0:
            return 0^n
        else:
            return 1^n
    else:
        cnt=(n+1)//2
        if cnt%2==0:
            return 0
        else:
            return 1