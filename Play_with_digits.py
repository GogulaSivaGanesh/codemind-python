def su(n):
    s=0
    while(n):
        r=n%10
        s+=r
        n//=10
    return s


a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    s+=su(i)
print(s)