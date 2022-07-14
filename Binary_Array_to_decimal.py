n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(n-1,-1,-1):
    s+=a[i]*(2**p)
    p+=1
print(s)