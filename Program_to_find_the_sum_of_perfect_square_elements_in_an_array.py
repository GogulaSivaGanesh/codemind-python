def per(n):
    t=n
    if t==int(n**0.5)**2:
        return 1
    else:
        return 0
a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    if per(i):
        s+=i
print(s)
