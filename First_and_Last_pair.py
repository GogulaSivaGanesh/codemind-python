a=int(input())
b=list(map(int,input().split()))
n=a
for i in range(0,a//2):
    print(b[i],b[n-1],end=' ')
    n-=1
if a%2==1:
    print(b[a//2],'0')
    
       
        

            