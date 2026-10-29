#bit全探索
N=int(input())
for i in range(2**N):
    for j in range(N):
        if i&(1<<j):
            break

