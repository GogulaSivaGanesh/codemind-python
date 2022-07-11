n=int(input())
t=n
for i in range(int(n**0.5),n):
    if i*(i+1)==t:
        print('YES')
        break
else:
    print('NO')