# 行列累乗

def mat_mul(A,B,mod):
    N=len(A)
    K=len(A[0])
    M=len(B[0])
    C=[[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j]+=A[i][k]*B[k][j]
            C[i][j]%=mod
    
    return C

def mat_power(base,exp,mod):
    n=len(base)
    ans=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    while exp>0:
        if exp%2==1:
            ans=mat_mul(ans,base,mod)
        base=mat_mul(base,base,mod)
        exp//=2
    return ans