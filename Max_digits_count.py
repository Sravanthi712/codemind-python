def dig(n):
    if(n==0):
        return 1
    if n<0:
        n=abs(n)
    c=0
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    x=dig(l[i])
    k.append(x)
v=max(k)
p=0
for i in k:
    if i==v:
        p+=1
print(p)

    
    