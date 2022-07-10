n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in a:
    if i%2==1:
        s1+=i
print(s1)