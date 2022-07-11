n=int(input())
for i in range(n,n**n):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        a=i
        break
for u in range(n,0,-1):
    d=0
    for v in range(1,u+1):
        if u%v==0:
            d+=1
    if d==2:
        b=u
        break
if a-n<n-b:
    print(a-n)
else:
    print(n-b)