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
a,b=map(int,input().split())
l=list(map(int,input().split()))
k=[]

for i in range(len(l)):
    j=dig(l[i])
    k.append(j)
c=0
for i in k:
    if(i==b):
        c+=1
print(c)
        