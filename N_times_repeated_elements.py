a=int(input())
b=list(map(int,input().split()))
c=[]
e=int(input())
for i in b:
    if b.count(i)==e:
        c.append(i)
        
d=[]
if len(c)==0:
    print('-1')
else:
    for i in c:
        if i not in d:
            d.append(i)
    print(*d)
            