# いもす法(1次元)

D=int(input())
N=int(input())
#前処理(+1,-1の加算)用の配列
p=[0]*(D+2)
for i in range(N):
    L,R=map(int,input().split())
    p[L]+=1
    p[R+1]-=1

ans=[0]*(D+2)
for i in range(1,D+1):
    ans[i]=ans[i-1]+p[i]
    
for i in range(1,D+1):
    print(ans[i])



# D (何日目)が 0から始まる場合はindex注意 B07
T=int(input())
N=int(input())
#前処理(+1,-1の加算)用の配列
# t=0~Tとする (出力はT-1だが)
p=[0]*(T+3)
for i in range(N):
    L,R=map(int,input().split())
    # p[R+1]はR日目を含まないから　含むならp[R+2]
    p[L+1]+=1
    p[R+1]-=1

ans=[0]*(T+3)
for i in range(1,T+2):
    ans[i]=ans[i-1]+p[i]
    
for i in range(1,T+1):
    print(ans[i])

# ABC183-Dも
