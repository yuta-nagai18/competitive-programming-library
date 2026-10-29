# 行列(2×2)の積、繰り返し二乗法

def mat_mul(A,B,mod):
    C=[[0,0],[0,0]]
    C[0][0] = (A[0][0]*B[0][0]+A[0][1]*B[1][0])%mod
    C[0][1] = (A[0][0]*B[0][1]+A[0][1]*B[1][1])%mod
    C[1][0] = (A[1][0]*B[0][0]+A[1][1]*B[1][0])%mod
    C[1][1] = (A[1][0]*B[0][1]+A[1][1]*B[1][1])%mod
    return C

def mat_power(base,exp,mod):
    ans=[[1,0],[0,1]]
    while exp>0:
        if exp & 1:
            ans=mat_mul(ans,base,mod)
        base=mat_mul(base,base,mod)
        exp=exp >> 1
    return ans



