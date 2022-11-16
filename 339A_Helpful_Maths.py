#URL=https://codeforces.com/problemset/problem/339/A

s=input()
a=b=c=0
for i in range(0,len(s),2):
    if s[i]=='1':
        a+=1
    if s[i]=='2':
        b+=1
    if s[i]=='3':
        c+=1
res='1+'*a+'2+'*b+'3+'*c
print(res[:-1])