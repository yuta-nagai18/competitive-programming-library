#再帰関数を用いたDFSによる全探索　ABC161-D, ABC165-C, ABC114-C, ABC119-C,ABC29-C

K=int(input())
ans=[]
def dfs(A):
    # 格納
    ans.append(int("".join(map(str,A))))
    # Aを数列のまま保存したいときは
    # ans.append(A.copy())

    # 打ち切り
    if len(A)==10:
        return
    
    # 再帰呼び出し
    if A[-1]==0:
        A.append(0)
        dfs(A)
        A.pop()

        A.append(1)
        dfs(A)
        A.pop()
    elif A[-1]==9:
        A.append(9)
        dfs(A)
        A.pop()

        A.append(8)
        dfs(A)
        A.pop()
    else:
        A.append(A[-1]-1)
        dfs(A)
        A.pop()

        A.append(A[-1])
        dfs(A)
        A.pop()

        A.append(A[-1]+1)
        dfs(A)
        A.pop()

for i in range(1,10):
    dfs([i])
ans.sort()
print(ans[K-1])

# ABC161-D　

# 樹形図のイメージ
# https://drken1215.hatenablog.com/entry/2020/04/05/150900



##########################################################################
N=int(input())
ans=0
# i,j,kはそれぞれ7,5,3の個数
def dfs(A,i,j,k):
    global ans
    # 格納
    if i>0 and j>0 and k>0 and int("".join(map(str,A)))<=N:
        ans+=1
    # 打ち切り
    if len(A)==len(str(N)):
        return
    # 再帰呼び出し
    A.append(7)
    dfs(A,i+1,j,k)
    A.pop()
    
    A.append(5)
    dfs(A,i,j+1,k)
    A.pop()

    A.append(3)
    dfs(A,i,j,k+1)
    A.pop()

dfs([7],1,0,0)
dfs([5],0,1,0)
dfs([3],0,0,1)

print(ans)

# ABC114-C 
# dfsの引数を工夫することもできる
