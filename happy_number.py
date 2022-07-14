def happy(n):
    s=0
    while(n):
        r=n%10
        s=s+r**2
        n//=10
    if s>9:
        return happy(s)
    elif s==1 or s==7:
        print(True)
    else:
        print(False)
     

n=int(input())
happy(n)
