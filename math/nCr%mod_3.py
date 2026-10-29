# 1<=k<=n<=5000 で pが素数でなくても良い

mx=5000  #nの取り得る最大値
p=998244353

Comb=[]
for i in range(mx+1):
    Comb.append([0]*(mx+1))

Comb[0][0]=1

for i in range(1,mx+1):
    Comb[i][0]=1
    for j in range(1,mx+1):
        Comb[i][j]=(Comb[i-1][j-1]+Comb[i-1][j])%p