n=int(input())
m=int(input())
s=m+n
k=1
while(k>0):
    t=k+s
    c=0
    for i in range(1,t+1):
        if t%i==0 or i==1:
            c+=1
    if c==2:
        print(k)
        break
    k+=1

