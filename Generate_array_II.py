n=int(input())
a=list(map(int,input().split()))

for i in range(0,n,2):
    c=a[i+1]
    for j in range(0,c):
        print(a[i],end=' ')
  
        