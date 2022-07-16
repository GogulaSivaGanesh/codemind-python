a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    for j in d:
        if i==j:
            e.append(i)
print(len(set(e)))