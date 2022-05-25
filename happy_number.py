def happy(n):
    temp=n
    sum=0
    while(n):
        rem=n%10
        sum=sum+rem**2
        n=n//10
    return sum
n=int(input())
b=happy(n)
c=happy(b)
f=happy(c)
g=happy(f)
if(g==1):
    print(True)
else:
    print(False)
