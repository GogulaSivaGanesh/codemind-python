n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i%2==0:
        s+=1
if s==len(a):
    print(True)
else:
    print(False)