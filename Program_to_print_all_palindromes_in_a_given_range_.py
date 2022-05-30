def pal(n):
    sum=0
    temp=n
    while(n):
        rem=n%10
        sum=sum*10+rem
        n//=10
    return(temp==sum)
            
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(pal(i)):
        print(i,end=' ')