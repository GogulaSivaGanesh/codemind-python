def fact(a):
    sum=0
    for i in range(1,a+1):
        if a%i==0:
            sum+=i
    return sum
a=list(map(int,input().split(',')))
c=0
b=[]
for i in a:
    if fact(i) in a:
        b.append(i)
        c+=1
if c==0:
    print('-1')
else:
    print(*sorted(b))