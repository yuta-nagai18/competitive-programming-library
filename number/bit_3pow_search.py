# bit全探索(3つの状態 (3^N通り))

from collections import defaultdict
N,M=map(int,input().split())
c=list(map(int,input().split()))

# see[i]: 動物iを見れる動物園の番号
see=defaultdict(set)
for i in range(M):
    l=list(map(int,input().split()))
    for j in range(1,len(l)):
        see[i].add(l[j]-1)

ans=10**20
for i in range(3**N):
    cost=0
    animal=[0]*M
    for j in range(N):
        # bitが1のとき
        if i//(3**j)%3==1:
            for k in range(M):
                if j in see[k]:
                    animal[k]+=1
            cost+=c[j]
        # bitが2のとき
        elif i//(3**j)%3==2:
            for k in range(M):
                if j in see[k]:
                    animal[k]+=2
            cost+=c[j]*2
    flag=True
    for n in range(M):
        if animal[n]<2:
            flag=False
    if flag:
        ans=min(ans,cost)

print(ans)

# abc404-D



