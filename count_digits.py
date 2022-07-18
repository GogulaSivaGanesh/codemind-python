a=int(input())
e=list(map(int,input().split()))
c=[]
b=[]
for i in e:
    if i<0:
        i=i*(-1)
        b.append(i)
    else:
        b.append(i)
for i in b:
        g=0
        g=len(str(i))
        c.append(g)
print(*c)

  
