a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        c.append(i)
        
if len(c)==0:
    print('-1')
else:
    print(min(c),max(c))