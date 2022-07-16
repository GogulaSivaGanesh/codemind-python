def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
z=list(map(int,input().split()))
a=[]
for i in z:
    if i not in a:
        a.append(i)

for i in range(0,n):
    if max(a)==a[i]:
        b=i
    if min(a)==a[i]:
        c=i
d=0
if b>c:
    for i in range(c,b+1):
        if prime(a[i]):
            d+=1
    print(d)
else:
    for i in range(b,c+1):
        if prime(a[i]):
            d+=1
    print(d)


