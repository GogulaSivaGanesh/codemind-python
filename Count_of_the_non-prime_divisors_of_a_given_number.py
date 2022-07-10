n=int(input())
b=[]
c=0
d=0
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
for j in b:
    for u in range(1,j+1):
        if j%u==0:
            c+=1
    if c!=2:
        d+=1
    c=0
print(d)