def cou(n):
    if(n==0):
        return 1
    if(n<0):
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
for i in  range(len(l)):
    x=cou(l[i])
    k.append(x)
print(*k)
    
    