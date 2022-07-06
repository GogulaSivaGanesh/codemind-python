n=int(input())
a=0
b=1
temp=0
for i in range(n):
    if(n>a):
        x=a
        y=b
    temp=a+b
    a=b
    b=temp
if((n-x)>(y-n)):
    print(y)
elif (n-x)<(y-n):
    print(x)
else:
    print(x,y)