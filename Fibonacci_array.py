
b=int(input())
a=list(map(int,input().split()))
if b<=2:
    print('no')
else:
    for i in range(2,b-2):
        if a[i]!=a[i-1]+a[i-2]:
            print('no')
            break
    else:
        print('yes')