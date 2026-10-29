H,W,N=map(int,input().split())

#前処理(+1,-1の加算)用の配列
x=[]
for i in range(H+2):
    x.append([0]*(W+2))

cum=[]
for i in range(H+2):
    cum.append([0]*(W+2))
    
#前処理
for i in range(N):
    u,l,d,r=map(int,input().split())
    x[u][l]+=1
    x[d+1][r+1]+=1
    x[d+1][l]-=1
    x[u][r+1]-=1

#横方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]=cum[i][j-1]+x[i][j]

#縦方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]+=cum[i-1][j]


for i in range(1,H+1):
        print(*cum[i][1:W+1])


#座標のときは注意
N=int(input())
H=1500
W=1500

#前処理(+1,-1の加算)用の配列
x=[]
for i in range(H+2):
    x.append([0]*(W+2))

cum=[]
for i in range(H+2):
    cum.append([0]*(W+2))
    
#前処理
for i in range(N):
    u,l,d,r=map(int,input().split())
    x[u][l]+=1
    x[d][r]+=1
    x[d][l]-=1
    x[u][r]-=1

#横方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]=cum[i][j-1]+x[i-1][j-1]

#縦方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]+=cum[i-1][j]

ans=0
for i in range(H+1):
    for j in range(W+1):
        if cum[i][j]>0:
            ans+=1
print(ans)