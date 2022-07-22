a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    e=b.count(i)
    c.append(e)
for i in b:
    if b.count(i)==max(c):
        d.append(i)
print(min(d))
    