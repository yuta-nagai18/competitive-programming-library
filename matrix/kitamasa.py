# きたまさ法
# https://tjkendev.github.io/procon-library/python/series/kitamasa.html
# a_{n+k} = c_0*a_n + c_1*a_{n+1} + .. + c_{k-1}*a_{n+k-1}
# が与えられたとき、a_n を計算する

def kitamasa(m, k, C, A):
    # m: 求めたい項は何番目か　a_nのnに該当
    # k: 漸化式の項数　kに該当
    # C: [c_0, c_1, .. ,c_{k-1}]
    # A: [a_0, a_1, .. ,a_{k-1}]
    MOD = 10**9 + 7

    C0 = [0]*k; C1 = [0]*k
    if m == 0:
        return A[0]
    C0[1] = 1

    p = 60
    while (m >> p) & 1 == 0:
        p -= 1

    D0 = [0]*k; D1 = [0]*k
    while p:
        p -= 1

        #dbl(k, C0, C1)
        D0[:] = C0[:]
        for j in range(k):
            C1[j] = C0[0] * C0[j] % MOD
        for i in range(1, k):
            #inc(k, D0, D1)
            D1[0] = D0[k-1] * C[0] % MOD
            for j in range(k-1):
                D1[j+1] = (D0[j] + D0[k-1]*C[j+1]) % MOD

            for j in range(k):
                C1[j] += C0[i] * D1[j] % MOD
            D0, D1 = D1, D0
        for i in range(k):
            C1[i] %= MOD
        C0, C1 = C1, C0

        if (m >> p) & 1:
            #inc(k, C0, C1)
            C1[0] = C0[k-1] * C[0] % MOD
            for i in range(k-1):
                C1[i+1] = (C0[i] + C0[k-1]*C[i+1]) % MOD
            C0, C1 = C1, C0

    return sum(C0[i] * A[i] for i in range(k)) % MOD

K,N=map(int,input().split())
print(kitamasa(N-1,K,[1]*K,[1]*K))


# TDPC-T フィボナッチ