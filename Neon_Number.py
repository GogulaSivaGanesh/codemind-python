a=int(input())
b=a*a
t=b
s=0
while(b):
    r=b%10
    s+=r
    b//=10
if a==s:
    print('Neon Number')
else:
    print('Not Neon Number')
    
    