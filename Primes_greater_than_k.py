def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0



n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if i>=b:
        if prime(i):
            c+=1
print(c)



