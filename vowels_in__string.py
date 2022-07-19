n=input()
s=' '
k=' '
for i in n:
    if i in 'aeiouAEIOU':
        s+=i
for j in s:
    if j not in k:
        k+=j
        print(j,end=' ')
if s==0:
    print('-1')


        
        