def rev(n):
    s=0
    t=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
u=[]
for i in range(len(l)):
    k=rev(l[i])
    u.append(k)
print(*u)