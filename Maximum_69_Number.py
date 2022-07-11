n=int(input())
a=[]
while(n):
    r=n%10
    a.append(r)
    n//=10
a=a[::-1]
for i in range(len(a)):
    if a[i]==6:
        a[i]=9
        break

for i in a:
    print(i,end='')