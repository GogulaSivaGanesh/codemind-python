def am(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
if am(n)==m and n==am(m):
    print('Amicable')
else:
    print('Not Amicable')