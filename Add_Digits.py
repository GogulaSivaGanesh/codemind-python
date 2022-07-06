def addd(n):
    s=0
    while(n):
        
        rem=n%10
        s=s+rem
        n//=10
    return s
        
        
        
n=int(input())
while 1:
    if addd(n)<=10:
        print(addd(n))
        break
    n=addd(n)
