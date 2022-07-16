n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(0,n-2,2):
    if a[i+1]>a[i] and a[i+2]<a[i+1]:
        c+=1
    else:
        d+=1
        print('-1')
        break
if d==0:
    print(c)