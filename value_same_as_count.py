a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if b.count(i)==i:
        c.append(i)
print(len(set(c)))
            