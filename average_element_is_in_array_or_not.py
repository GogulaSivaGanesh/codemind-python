n=int(input())
a=list(map(int,input().split()))
b=int(sum(a)/7)
for i in a:
    if b==i:
        print(True)
        break
else:
    print(False)