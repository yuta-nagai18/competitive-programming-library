#累積和max (区間和の最大 (累積和において区間差の最大値))
A=list(map(int,input().split()))
cum=0
min_cum=0
ans=-10**20
for i in range(len(A)):
    cum+=A[i]
    min_cum=min(min_cum,cum)
    ans=max(ans,cum-min_cum)

#   a = [1, -2, -3, 4, 5, -10, 3, 7, -2, 9]
# cum = [1, -1, -4, 0, 5, -5, -2, 5, 3, 12]
#                         ^ここの差が最大 ^
# この差 17 を累積和maxとして求める 


#累積和min
cum=0
max_cum=0
ans=10**20
for i in range(len(A)):
    cum+=A[i]
    max_cum=max(max_cum,cum)
    ans=min(ans,cum-max_cum)

#ARC174-A, ABC182-D