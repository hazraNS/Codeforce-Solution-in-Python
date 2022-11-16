#https://codeforces.com/problemset/problem/266/A

n=int(input())
s=input()
l=list(s)
count=0
for i in range(0,n-1):
    a=l[i]+l[i+1]
    if a=='RR' or a=='GG' or a=='BB':
        count=count+1
print(count)