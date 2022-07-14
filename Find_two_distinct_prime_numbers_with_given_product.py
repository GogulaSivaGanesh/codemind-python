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
a=[]
for i in range(1,n):
    if n%i==0:
        if prime(i):
            a.append(i)
for j in a:
    print(j,end=' ')
if len(a)<2:
    print('-1')