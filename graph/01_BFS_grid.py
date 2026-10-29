from collections import deque
H,W=map(int,input().split())

c=[]
for i in range(H):
    C=list(input())
    for j in range(W):
        if C[j]=="s":
            sh=i
            sw=j
        elif C[j]=="g":
            gh=i
            gw=j
    c.append(C)

dist=[]
for i in range(H):
    dist.append([10**20]*W)
dist[sh][sw]=0

done=[]
for i in range(H):
    done.append([False]*W)

q=deque()
q.append((sh,sw))
while len(q)>0:
    i,j=q.popleft()
    if done[i][j]:
        continue
    done[i][j]=True
    for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not (0<=i1<H and 0<=j1<W):
            continue
        if c[i1][j1]=="#":
            if dist[i1][j1]>dist[i][j]+1:
                dist[i1][j1]=dist[i][j]+1
                q.append((i1,j1))
        elif c[i1][j1]==".":
            if dist[i1][j1]>dist[i][j]:
                dist[i1][j1]=dist[i][j]
                q.appendleft((i1,j1))
        elif c[i1][j1]=="g":
            if dist[i1][j1]>dist[i][j]:
                dist[i1][j1]=dist[i][j]
                q.appendleft((i1,j1))
                
if dist[gh][gw]<=2:
    print("YES")
else:
    print("NO")

# ABC5-C 
# 重みはグリッドが#かどうかで決まる
# そもそも0か1なので重みをキューにもたせる必要はない
# (BFSのように「全てが同じ値である」または
# 「ある値が前側に、それより1大きい値が後ろ側にそれぞれ固まっている」状態)

# ABC5-Cはdijkstraでも通った