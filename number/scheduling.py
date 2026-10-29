# 区間スケジューリング問題

N=int(input())
st=[]
for i in range(N):
    s,t=map(int,input().split())
    st.append([s,t])

st=sorted(st,key=lambda x:x[1])

ans=0
last_time=0 # -inf のほうがよいか？ 
for s,t in st:
    # <=: 開始時刻と終了時刻が被る予定は共に参加可能
    if last_time<=s:
        last_time=t
        ans+=1

print(ans)



# 終了時刻が早い予定を優先的に選んでいく
# すでに選んだ予定のうち最も遅い予定の終了時刻をlast_time
# としたとき、開始時刻がlast_time以降である予定のうち
# 終了時刻が最も早いものを次に選ぶ (開始時刻は遅くても関係ない)

# あとにより多くの選択肢を残せるようにする


