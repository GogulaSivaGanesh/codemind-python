n=int(input())
l=len(str(n))
t=n
s=0
while(n):
    if l==0:
        break
    r=n%10
    s+=r**l
    n//=10
    l-=1
if t==s:
    print(True)
else:
    print(False)
