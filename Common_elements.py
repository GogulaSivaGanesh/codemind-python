a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
g=[]
for i in c:
    for j in d:
        if i==j:
            e.append(i)
for i in e:
    if i not in g:
        g.append(i)
        print(i,end=' ')

        

