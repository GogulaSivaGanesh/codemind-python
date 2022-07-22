a=int(input())
b=list(map(int,input().split()))
c=[]
for j in range(len(b)-1,a//2-1,-1):
    c.append(b[j])
for i in range(0,a//2):
    c.append(b[i])
print(*c)
    
    
    
    

