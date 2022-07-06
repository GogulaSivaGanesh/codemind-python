n=int(input())
b=[]
while(n):
    rem=n%10
    b.append(rem)
    n//=10
b=b[::-1]
for i in range(len(b)):
    if b[i]==6:
        b[i]=9
        break
for i in b:
    print(i,end='')