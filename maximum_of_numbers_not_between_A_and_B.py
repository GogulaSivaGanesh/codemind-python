n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
s=0
for i in a:
    if i<b or i>c:
        d.append(i)
        s+=1
if s>0:
    print(max(d))
else:
    print('-1')