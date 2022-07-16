a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(0,a-1):
    if b[i]>b[i+1]:
        c+=1
if a-1==c:
    print('yes')
else:
    print('no')