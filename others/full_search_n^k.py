N,K,X=map(int,input().split())
s=[]
all=[]
for i in range(N):
    S=input()
    s.append(S)
    all.append(S)

for i in range(K-1):
    new_all=[]
    for j in range(len(all)):
        for k in range(N):
            new_all.append(all[j]+s[k])
    all=new_all.copy()

all.sort()
print(all[X-1])

# ABC416-C
# s1,s2,s3...,sNのN個の中から好きな要素を1つ選ぶのをK回
# このときの全通り(N^K) N<=10, K<=5を列挙
