n=int(input())
m=int(input())
for i in range(n,m+1):
    l=len(str(i))
    c=0
    temp=i
    if i%10==0:
        continue
    else:
        while(i):
            r=i%10
            i=i//10
            if temp%r!=0:
                break
            c+=1
        if l==c:
            print(temp,end=' ')