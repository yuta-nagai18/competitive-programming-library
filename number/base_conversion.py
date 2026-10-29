#a進数からb進数への変換 
def base(n,a,b):
    if n==0:
        return [0]
    l=[]
    n=int(str(n),base=a)
    while n>0:
        l.append(n%b)
        n//=b
    l.reverse()
    return "".join(map(str,l))


# 26進数で3桁で 25 10 3のように表したくても 25103となってしまうので
# returnで"".joinを消してただの return l とする必要あり

# また、先頭の0は消えるため、後から l=[0]*(必要な数)+l のように付足す