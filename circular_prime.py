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
a=str(n)[::-1]
a=int(a)
if prime(n):
    if prime(a):
        print("circular prime")
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
