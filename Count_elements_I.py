n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
i=len(set(l)&set(l1))
print(i)