n=int(input())
s=0
p=1
while(n):
    r=n%10
    p=p*r
    s=s+r
    n//=10

if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')