n=int(input())
pro=1
sum=0
while n:
    r=n%10
    pro=pro*r
    sum=sum+r
    n=n//10
print(pro-sum)