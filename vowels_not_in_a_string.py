n=input()
s=' '
k='aeiou'
e=0
for i in n:
    if i in'aeiou':
        s+=i
for i in k:
    if i not in s:
        e+=1
        print(i,end=' ')
if e==0:
    print('0')



        
