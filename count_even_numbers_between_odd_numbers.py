n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if (a[i]%2==1 and a[i+2]%2==1):
        if a[i+1]%2==0:
            c+=1
print(c)