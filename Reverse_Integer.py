n=int(input())
t=n
if n<0:
    n=n*(-1)
s=0
while(n):
    r=n%10
    s=s*10+r
    n//=10
if t<0:
    print((-1)*s)
else:
    print(s)