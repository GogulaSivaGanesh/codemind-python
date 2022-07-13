n=int(input())
a=list(map(int,input().split()))
l=len(a)
for i in range(l-1,0,-1):
    if a[i]%2==1:
        print(i)
        break
    