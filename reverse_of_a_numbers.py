n=int(input())
sum=0
while n:
    rem=n%10
    sum=sum*10+rem
    n//=10
print(sum)