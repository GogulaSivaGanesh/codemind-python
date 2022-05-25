n=int(input())
temp=n
arr=[]
while(n>0):
    d=n%10
    arr.append(d)
    n=n//10
for ele in arr:
    if arr.count(ele)>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')
    
