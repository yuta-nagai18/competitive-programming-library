# 誤差を小数まで見るときの二分探索  (+答えで二分探索)

N,K=map(int,input().split())
L=list(map(int,input().split()))

ok=0
ng=10**5+1
while abs(ok-ng)>0.000001:
    mid=(ok+ng)/2
    cnt=0
    for i in range(N):
        cnt+=L[i]//mid
    if cnt>=K:
        ok=mid
    else:
        ng=mid

print(ok)

# https://algo-method.com/tasks/369/editorial