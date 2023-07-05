x=int(input())
y=int(input())
s=0
s1=0
for i in range(1,x):
    if(x%i==0):
        s=s+i
for j in range(1,y):
    if(y%j==0):
        s1=s1+j
if(s==y and s1==x):
    print("Amicable")
else:
    print("Not Amicable")
    