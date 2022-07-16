n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c=set(c)
d=[]
for i in a:
    for j in b:
        if i==j:
            d.append(i)
e=0
for i in c:
    if i not in d:
        e+=1
print(e)

