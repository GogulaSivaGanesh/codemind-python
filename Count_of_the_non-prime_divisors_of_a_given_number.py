n=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
b=[]
c=0
for k in a:
    for j in range(2,k//2+1):
       
        if k%j==0:
            
            c+=1
            break
print(c+1)