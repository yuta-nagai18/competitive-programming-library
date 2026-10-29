# エラトステネスの篩
import math
def eratosthenes(n):
    for i in range(2,int(n**0.5)+1):
	    if prime[i]:
		    for j in range(2*i,n+1,i):
			    prime[j]=False

n=10**6
prime=[True]*(n+1)
eratosthenes(n)
prime[0]=False
prime[1]=False
list_prime=[]
for j in range(2,n+1):
    if prime[j]:
        list_prime.append(j)



# 素数の個数の累積和
cnt_cum=[0]
for i in range(1,n+1):
    if prime[i]:
        cnt_cum.append(cnt_cum[-1]+1)
    else:
        cnt_cum.append(cnt_cum[-1])

# n=8のとき
# prime = [False, False, True, True, False, True, False, True, False]
# list_prime = [2, 3, 5, 7]
# cnt_cum = [0, 0, 1, 2, 2, 3, 3, 4, 4]


# O(NloglogN)でN以下の素数を列挙できる