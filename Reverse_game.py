n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    i=int(str(i)[::-1])
    b.append(i)
print(*b)
    