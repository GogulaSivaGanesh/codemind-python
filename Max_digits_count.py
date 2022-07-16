a=int(input())
b=list(map(int,input().split()))
c=len(str(max(b)))
d=0
for i in b:
    if c==len(str(i)):
        d+=1
print(d)