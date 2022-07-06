n=int(input())
temp=n
l=len(str(n))
s=0
while(n):
    if l==0:
        break
    rem=n%10
    s=s+rem**l
    n//=10
    l-=1
if temp==s:
    print(True)
else:
    print(False)
    
    