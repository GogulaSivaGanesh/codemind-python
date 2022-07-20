a=input()
b='qwertyuioopasdfghjklzxcvbnm'
c=0
for i in a:
    if i in b:
        c+=1
print(c)