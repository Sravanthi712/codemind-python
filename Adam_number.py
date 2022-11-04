n=int(input())
sum=0
sum1=0
s1=n*n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
s2=sum*sum
while s2>0:
    r1=s2%10
    sum1=sum1*10+r1
    s2=s2//10
if(s1==sum1):
   print(True)
else:
   print(False)
    