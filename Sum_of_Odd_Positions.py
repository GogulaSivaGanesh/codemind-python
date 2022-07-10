n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n):
    if i%2==1:
        s1+=a[i]
    
print(s1)