#ダブリング ABC167-D
N,K=map(int,input().split())
A=list(map(int,input().split()))

#doubing[i][j]: jの2^i個先の町
doubling=[]
for i in range(64):
    doubling.append([-1]*N)

for i in range(N):
    doubling[0][i]=A[i]-1

for i in range(1,64):
    for j in range(N):
        doubling[i][j]=doubling[i-1][doubling[i-1][j]]

now=0
for i in range(64):
    if (K >> i) & 1:
        now=doubling[i][now]

print(now+1)

# 同じ操作を繰り返したK回目の状態を求めるとき、
# 愚直にやるとO(K)だが、O(logK)に短縮できる
# 要素の個数N個に対してK回操作したときはO(NlogK)

# 配列doublingの要素数はlog2(K)+1
# K=10^18のとき、10^18=2^xのxが要素数

# 集合sに都市uが含まれるか　(2^uの桁のビットは立ってるか）
# 　if (s >> u) & 1
