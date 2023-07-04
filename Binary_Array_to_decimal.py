n=int(input())
l=list(map(int,input().split()))
s1=l[::-1]
c=0
for i in range(len(s1)):
    c+=(2**i)*(s1[i])
print(c)
    
    