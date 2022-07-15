n=int(input())
a=list(map(int,input().split()))
b=0
c=0
for i in range(0,n):
    if a[i]%2==1:
        if i%2==1:
            b+=1
        c+=1
if c==b:
    print(True)
else:
    print(False)