n=int(input())
a=list(map(int,input().split()))
s1=0
s=0
for i in range(0,n):
    if i<n//2:
        s+=a[i]
    else:
        s1+=a[i]
print(abs(s-s1))
    

