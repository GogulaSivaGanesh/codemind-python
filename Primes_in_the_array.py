def prime(n):
    c=0
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if prime(i):
        c+=1
print(c)
        
    