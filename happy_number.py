def happy(n):
    s=0
    while(n):
        r=n%10
        s=s+r**2
        n//=10
    return s
a=int(input())
while a>=10:
    a=happy(a)
if a==1 or a==7:
    print(True)
else:
    print(False)