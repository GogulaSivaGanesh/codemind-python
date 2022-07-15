n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
e=0
d=[]
for i in a:
    if i<b or i>c:
        d.append(i)
        e+=1
if e==0:
    print('-1')
else:
    print(min(d))

