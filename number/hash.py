import string
alp=string.ascii_lowercase
N,Q=map(int,input().split())
mod=2147483647
S=input()

# 100のi乗
l_100=[1]
for i in range(1,N+1):
    l_100.append(l_100[i-1]*100%mod)

# ハッシュ値 (H[i]: i文字目までのハッシュ値)
H=[0]*(N+1)
for i in range(1,N+1):
    H[i]=100*H[i-1]+(alp.index(S[i-1])+1)
    H[i]%=mod

# l文字目からr文字目までのハッシュ値 (1-indexed)
def hash(l,r):
    return (H[r]-l_100[r-l+1]*H[l-1])%mod 

for i in range(Q):
    a,b,c,d=map(int,input().split())
    # S[a,b] のハッシュ値
    h1=hash(a,b) 
    # S[c,d] のハッシュ値
    h2=hash(c,d)
    if h1==h2:
        print("Yes")
    else:
        print("No")

# 鉄則A56
# S[a,b]とS[c,d]（Sのa文字目からb文字目と、Sのc文字目からd文字目は一致するか）