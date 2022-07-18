def le(n):
    if n<0:
        n=n*(-1)
    elif n==0:
        z=1
        return z
    s=0
    
    while(n):
        r=n%10
        s+=1
        n//=10
    return s
        
a,b=map(int,input().split())
c=list(map(int,input().split()))

n=0
for i in c:
    if le(i)==b:
        n+=1
print(n)
    

