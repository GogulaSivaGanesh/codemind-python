def add(n):
    sum=0
    while(n):
        rem=n%10
        sum=sum+rem
        n//=10
    if sum>9:
        add(sum)
    else:
        print(sum)
    
n=int(input())
add(n)
    
        