a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(0,a):
    if c[i]%b==0:
        d+=1
print(a-d)
        