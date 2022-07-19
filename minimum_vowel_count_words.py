n=input()
n=n.lower()
a=n.split()
b='aeiou'
c=[]
for i in a:
    e=0
    for j in i:
        if j in b:
            e+=1
    c.append(e)
m=min(c)
print(c.count(m))
        