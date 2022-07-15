n=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        c.append(i)
c=set(c)
s=sum(c)
l=len(c)
if s>0:
    print(format((s/l),'.2f'))
else:
    print('-1')