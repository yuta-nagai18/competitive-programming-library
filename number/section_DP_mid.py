N=int(input())
a=list(map(int,input().split()))
cum=[0]
for i in range(N):
    cum.append(cum[-1]+a[i])

# dp[i][j]: i番目からj番目までの区間のスライムを合体するコストの総和の最小値
dp=[]
for i in range(N):
    dp.append([10**20]*N)

for i in range(N):
    dp[i][i]=0

for LEN in range(N):
    for l in range(N-LEN):
        r=l+LEN
        for mid in range(l,r):
            dp[l][r]=min(dp[l][r],dp[l][mid]+dp[mid+1][r]+cum[r+1]-cum[l])

print(dp[0][-1])

# 区間DP
# dp[l][r]の更新でdp[l][mid], dp[mid+1][r] を全てのmidについて確認する

# ... 10 20 30 40 ... (ある区間[l,r]で考える)
# ある区間[l,r]のスライムを合体する直前はその区間は2つに分かれている (その2つの分け方は以下の通り)
# (10) (20 30 40)
# (10 20) (30 40)
# (10 20 30) (40)　　　　の3通りの分け方がある(3通りのmidを全て調べる)

# midは左のグループの一番右のものとする
# 例えば(10 20 30) (40) のときは mid は 30 のところのインデックス 
# この2つのグループを合体させるには、合体する前の2つのグループ ((10 20 30) と (40)) 
# それぞれを作るために必要なコスト dp[l][mid] + dp[mid+1][r] と
# 区間[l,r] のスライムの大きさの総和の合計 が必要 (コードの漸化式)

# https://atcoder.jp/contests/dp/tasks/dp_n


# 以下のように、[l,r]内での区切りに加え、区間 [l,r]も考えるものもある
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611
# https://atcoder.jp/contests/tdpc/tasks/tdpc_iwi  (区間DPを2回)