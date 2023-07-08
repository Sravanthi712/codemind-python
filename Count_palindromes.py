def pal(n):
    s=0
    t=n
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    if(t==s):
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if(pal(l[i])==1):
        c+=1
print(c)