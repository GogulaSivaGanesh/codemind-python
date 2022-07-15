a=int(input())
b=list(map(int,input().split()))
c=0
b=set(b)
for i in b:
    if  i%2==1:
        c+=1
print(c)
    
       
        

            