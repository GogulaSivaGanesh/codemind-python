n=int(input())
b=n*n
c=len(str(n))
d=b%pow(10,c)
if(d==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
