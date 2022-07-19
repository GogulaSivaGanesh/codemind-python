n=input()
s=''
k=''
for i in n:
    if i in'aeiou':
        if i not in s:
            s+=i
for i in n:
    if i in 'AEIOU':
        if i not in k:
            k+=i

if len(k)==5 or len(s)==5:
    print(True)
else:
    print(False)



        
