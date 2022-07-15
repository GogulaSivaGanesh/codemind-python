n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
e=0
for i in a:
    if i>=b and i<=c:
        print(i,end=' ')
        e+=1
if e==0:
    print('-1')

