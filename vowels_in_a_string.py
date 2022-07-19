n=input()
m=input()
for i in range(0,len(n)):
    if n[i]==m:
        print(True)
        print(i)
        break
else:
    print(False)