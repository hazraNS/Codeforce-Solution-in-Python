n=int(input())
view=0
for i in range(0,n):
    s=input()
    if s.count('1') >= 2:
        view += 1
print(view)