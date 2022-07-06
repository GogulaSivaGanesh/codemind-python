def selfi(a,b):
    for n in range(a,b+1):
        temp=n
        co=0
        c=0
        if temp%10==0:
            continue
        else:
            while(n):
                co+=1
                rem=n%10
                if temp%rem==0:
                    c+=1
                n//=10
            if co==c:
                print(temp,end=' ')
n=int(input())
m=int(input())
selfi(n,m)
            
                
        
        