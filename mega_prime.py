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
st=len(str(n))
t=n
if prime(n):
    a=0
    s=0
    while(n):
        r=n%10
        n//=10
        if prime(r):
            a+=1
    if a==st:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
        
    