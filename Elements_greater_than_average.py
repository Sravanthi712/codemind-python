n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
c=0
for i in range(len(l)):
    if(l[i]>=a):
        c+=1
print(c)