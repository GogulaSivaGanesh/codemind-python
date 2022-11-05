a=int(input())
c=0
for i in range(a):
    b=input()
    if b=='++X' or b=='X++':
        c+=1
    else:
        c-=1
print(c)