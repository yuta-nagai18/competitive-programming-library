# 素因数分解

def factorization(n):
    ans=[]
    x=n
    y=2
    while y*y<=x:
        while x%y==0:
            ans.append(y)
            x//=y
        y+=1
    if x>1:
        ans.append(x)
    return ans

print(factorization(24))


# O(N^(1/2))