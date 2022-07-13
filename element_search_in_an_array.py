n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in a:
    if i==b:
        print(True)
        break
else:
    print(False)