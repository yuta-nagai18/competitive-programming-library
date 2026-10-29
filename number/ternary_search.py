# 三分探索

A,B=map(int,input().split())
l=0
r=A
while r-l>2:
    m1=l+(r-l)//3
    m2=r-(r-l)//3
    if A/((1+m1)**(1/2))+B*m1<A/((1+m2)**(1/2))+B*m2:
        r=m2
    else:
        l=m1

ans=10**20
for i in range(l,r+1):
    ans=min(ans,A/((1+i)**(1/2))+B*i)
print(ans)

# ABC279-D 

# 高々極値を1つしか持たない凸関数の最小値は三分探索で求められる

# 「f(n) が最小値をとる n は l≤n≤r の範囲に存在する」(＊) 
# ことが保証される l,r を設定し、条件 (＊) を満たしながら 
# l と r を少しずつ近づけていくことで、答えの n を見つける

