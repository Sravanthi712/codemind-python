n=int(input())
l=list(map(int,input().split()))
a=sorted(l)
f=[]
for i in range(len(l)):
    for j in range(len(a)):
        if l[i]==a[j]:
            f.append(l[i])
            
if(a==f):
    print("yes")
else:
    print("no")