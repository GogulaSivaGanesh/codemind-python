def pal(n):
    sum1=0
    temp=n
    while(n):
        rem=n%10
        sum1=sum1*10+rem
        n//=10
    if sum1==temp:
        return 1
    else:
        return 0
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
s=n+1
while(n<s):
    if pal(s):
        if prime(s):
            print(s)
            break
    s+=1
  








