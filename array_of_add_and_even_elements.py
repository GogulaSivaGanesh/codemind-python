n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
for i in c+b:
    print(i,end=' ')