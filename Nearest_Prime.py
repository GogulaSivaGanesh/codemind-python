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
for i in range(n):
    a=int(input())
    for j in range(a+1,a*a*a):
        if prime(j):
            b=j
            break
    for u in range(a,-1,-1):
        if prime(u):
            d=u
            break
    
    if b-a<a-d:
        print(b)
    else:
        print(d)
        
        