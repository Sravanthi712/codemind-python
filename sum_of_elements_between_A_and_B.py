n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=[]
f=0
for i in range(len(l)):
    if(l[i]>=x and l[i]<=y):
        s.append(l[i])
    
print(sum(s))