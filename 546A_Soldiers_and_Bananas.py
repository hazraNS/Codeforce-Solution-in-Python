#https://codeforces.com/problemset/problem/546/A

def sab(k,n,w):
    res=0
    #for i in range(1,w+1):
    #a=i*k
    res=sum([i*k for i in range(1,w+1)])
    if n>=res:
        print(0)
    else:
        print(res-n)
k,n,w=(input().split(' '))
k=int(k)
n=int(n)
w=int(w)
sab(k,n,w)