#順列と逆順列のswap ABC250-C

from collections import defaultdict
N,Q=map(int,input().split())
value=list(range(1,N+1))
pos=defaultdict(int)
for i in range(1,N+1):
    pos[i]=i-1

#value: 実際に動かす配列
#pos[v]: valueにおいて要素vがどの位置にあるか 


# pos       ......p1    p2 .......
#            ➁(pos[v1]) ➂(p1+1) 
# value     ......v1    v2 .......
#             ➀(input)  ➃(value[p2]) 

for i in range(Q):
    v1=int(input())
    if pos[v1]<N-1:
        p1=pos[v1]
        p2=p1+1
        v2=value[p2]
        value[p1],value[p2]=value[p2],value[p1]
        pos[v1],pos[v2]=pos[v2],pos[v1]
    else:
        p1=pos[v1]
        p2=p1-1
        v2=value[p2]
        value[p1],value[p2]=value[p2],value[p1]
        pos[v1],pos[v2]=pos[v2],pos[v1]
        
print(*value)