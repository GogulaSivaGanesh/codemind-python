a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in range(0,a):
    if (b[i]<c):
        s+=b[i]
for i in range(a-1,0,-1):
    if (b[i]>d):
        s+=b[i]
print(s)

        
        

