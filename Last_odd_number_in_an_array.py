n=int(input())
l=list(map(int,input().split()))
max=0
for i in range(n):
    if(l[i]%2!=0):
        max=l[i]
print(max)