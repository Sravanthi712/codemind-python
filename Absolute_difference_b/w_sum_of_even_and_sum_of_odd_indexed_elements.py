n=int(input())
l=list(map(int,input().split()))
r=0
s1=0
for i in range(len(l)):
    if(i%2==0):
        r=r+l[i]
    else:
        s1=s1+l[i]
print(abs(r-s1))