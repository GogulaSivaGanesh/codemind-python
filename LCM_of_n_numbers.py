def lcm(a,b):
    m=max(a,b)
    res=m
    while True:
        if res%a==0 and res%b==0:
            return res
        else:
            res+=m
a=int(input())
l=list(map(int,input().split()))
res=lcm(l[0],l[1])
for i in range(2,a):
    res=lcm(res,l[i])
print(res)