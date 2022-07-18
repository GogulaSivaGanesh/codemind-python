a=int(input())
d=list(map(int,input().split()))

b=[]
for i in d:
    if i<0:
        i=abs(i)
    else:
        if i not in b:
            b.append(i)
e=0
c=len(str(min(b)))


for i in b:
    if len(str(i))==c:
        e+=1
print(e)

  
