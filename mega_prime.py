def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
def rev(n):
    while n>0:
        d=n%10
        n=n//10
    return d
n=int(input())
if prime(n)==1:
    a=rev(n)
    if prime(a)==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        
        