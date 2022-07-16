a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    for j in d:
        if i==j:
            e.append(i)
for i in c:
    if i not in e:
        print(i,end=' ')
for i in d:
    if i not in e:
        print(i,end=' ')