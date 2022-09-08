def fact(n):
    if n==int(str(n)[::-1]):
        print(n)
    else:
        n+=int(str(n)[::-1])
        fact(n)
n=int(input())
fact(n+int(str(n)[::-1]))
