n=int(input())
a=str(n)

for i in a:
    if a.count(i)>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')