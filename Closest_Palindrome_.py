def pal(n):
    t=n
    n=int(str(n)[::-1])
    if t==n:
        return 1
    else:
        return 0
n=int(input())
for i in range(n-1,0,-1):
    if pal(i):
        a=i
        break
for j in range(n+1,n**n):
    if pal(j):
        b=j
        break
if abs(n-a)==abs(b-n):
    print(a,b)
elif abs(n-a)<abs(b-n):
    print(a)
else:
    print(b)
