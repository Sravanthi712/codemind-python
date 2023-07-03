n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
f=0
for i in l:
    if(a==i):
        f=1
        break
if(f==1):
    print("True")
else:
    print("False")
    