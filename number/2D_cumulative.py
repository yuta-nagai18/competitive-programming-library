H,W=map(int,input().split())

#各マスの数の入力
x=[]
for i in range(H):
    X=list(map(int,input().split()))
    x.append(X)

cum=[]
for i in range(H+1):
    cum.append([0]*(W+1))

#横方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]=cum[i][j-1]+x[i-1][j-1]

#縦方向
for i in range(1,H+1):
    for j in range(1,W+1):
        cum[i][j]+=cum[i-1][j]

Q=int(input())
for i in range(Q):
    u,l,d,r=map(int,input().split())
    #(u,l)を左上、(d,r)を右下とする長方形領域に書かれた数の総和
    print(cum[d][r]+cum[u-1][l-1]-cum[d][l-1]-cum[u-1][r])




