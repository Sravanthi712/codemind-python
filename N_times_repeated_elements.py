n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=0
s=[]
for i in range(len(l)):
    if(k==l.count(l[i])):
        s.append(l[i])
        f=1
if(f==1):
    print(*set(s))
else:
    print("-1")