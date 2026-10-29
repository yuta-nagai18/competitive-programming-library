# トポロジカルソート (BFS)

from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append([])

# 入次数を管理
in_num=[0]*N
for i in range(M):
    x,y=map(int,input().split())
    x-=1
    y-=1
    graph[x].append(y)
    in_num[y]+=1

Q=deque()
for i in range(N):
    if in_num[i]==0:
        Q.append(i)

ans=[]
while len(Q)>0:
    # 一意に決まるかはソートを行う全ステップで次に選べる点が1つか
    if len(Q)>1:
        print("一意に決まらない")
    i=Q.popleft()
    ans.append(i)
    for j in graph[i]:
        in_num[j]-=1
        if in_num[j]==0:
            Q.append(j)

print(ans)

# 閉路があるかの判定
if len(ans)==N:
    print("閉路なし")
else:
    print("閉路あり")

# アルゴ式の実装では逆から考えている
# グラフGは閉路の無い有向グラフDAGである ⇔ グラフ G はトポロジカルソート可



# トポロジカルソート (DFS)

# 深さ優先探索のコードではDAGであることを仮定したコードなので、
# 閉路があった場合でも動作する。閉路の検出には更に変更が必要。
















# ABC291-E