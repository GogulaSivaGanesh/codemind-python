a=int(input())
b=list(map(int,input().split()))
c=sum(b)//a
d=0
for i in b:
    if i<=c:
        d+=1
print(d)