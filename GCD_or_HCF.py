a,b=map(int,input().split())
c=b
while(1):
    if a%c==0 and b%c==0:
        break
    c-=1
print(c)