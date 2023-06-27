def count(n):
    c=0
    while n>0:
        d=n%10
        c+=1
        n=n//10
    return c
n=int(input())
b=count(n)
s=0
v=n
while n>0:
    r=n%10
    s=s+(r**b)
    b-=1
    n=n//10
if s==v:
    print("True")
else:
    print("False")