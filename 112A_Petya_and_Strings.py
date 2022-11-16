#URL=https://codeforces.com/problemset/problem/112/A

m = input().lower()
n = input().lower()
if m == n:
    print(0)
elif m > n :
    print(1)
else:
    print(-1)