n=int(input())
l=list(map(int,input().split()))
f=0
m=0
for i in range(len(l)):
    if(l[i]%2==0):
        if(i%2==0):
            f=f+1
        m=m+1
if(m==f):
    print("True")
else:
    print("False")