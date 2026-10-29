# N×N のグリッドについて、全ての点について始点として
# 上下左右斜めの8方向の全探索 (それぞれN個の点を通る)を行う

N=int(input())
a=[]
for i in range(N):
    A=list(input())
    a.append(A)

ans=-10**20
for sh in range(N):
    for sw in range(N):
        for d_h,d_w in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            num=[a[sh][sw]]
            posh=sh
            posw=sw
            for j in range(N-1):
                posh=(posh+d_h)%N
                posw=(posw+d_w)%N
                num.append(a[posh][posw])
            ans=max(ans,int("".join(map(str,num))))

print(ans)
