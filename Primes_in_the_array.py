def primes(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        
        if n%i==0:
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if (primes(l[i])==1):
        c+=1
print(c)