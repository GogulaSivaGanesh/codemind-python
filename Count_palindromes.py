def pal(n):
    t=n
    if int(str(n)[::-1])==t:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pal(i):
        c+=1
print(c)