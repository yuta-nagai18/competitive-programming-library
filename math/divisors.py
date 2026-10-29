# 約数列挙

def divisors(n):
    a=[]
    i=1
    while i*i<=n:
        if n%i==0:
            a.append(i)
            if i!=n//i:
                a.append(n//i)
        i+=1
    a.sort()
    return a

# O(N^(1/2))