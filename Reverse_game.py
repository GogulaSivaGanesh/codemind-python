a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    i=int(str(i)[::-1])
    c.append(i)
print(*c)