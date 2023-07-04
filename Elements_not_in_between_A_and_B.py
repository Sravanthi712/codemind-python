n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=[]
f=0
for i in range (len(l)):
    if(l[i]<x or l[i]>y):
        f=1
        s.append(l[i])
if(f==1):
    print(*s)
else:
    print("-1")