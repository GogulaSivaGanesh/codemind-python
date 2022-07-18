n=input()
a=n.split()
b=[]
for i in a:
    b.append(len(i))
print(max(b))