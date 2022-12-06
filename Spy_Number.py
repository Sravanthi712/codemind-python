n=int(input())
pro=1
sum=0
while n:
     r=n%10
     pro=pro*r
     sum=sum+r
     n=n//10
if(pro==sum):
    print("Spy Number")
else:
    print("Not Spy Number")
