N=int(input())
u,v=[],[]
for i in range(N):
    x,y=map(int,input().split())
    u.append(x+y)
    v.append(x-y)
print(max(max(u)-min(u),max(v)-min(v)))

# (x,y) を (u,v)=(x+y,x-y) に変換することを45度回転という

# (u,v) からマンハッタン距離を求められる
# 回転前のマンハッタン距離 = 回転後のチェビシェフ距離（座標の差の最大値）
# (u1,v1)=(x1+y1,x1-y1), (u2,v2)=(x2+y2,x2-y2) とすると
# マンハッタン距離 |x1-x2|+|y1-y2| = max(|u1-u2|,|v1-v2|) 

# ABC178-E 
# 異なる2点間のマンハッタン距離の最大値
