n=input()
n=n.lower()
c=n.split()
a='aeiou'
b=[]
for i in c:
    e=0
    for j in i:
        if j in a:
            e+=1
    b.append(e)
m=max(b)
print(b.count(m))