def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if isprime(i):
        print(i)
        