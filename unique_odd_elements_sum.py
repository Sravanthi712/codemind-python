n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if(l[i]%2!=0):
        s.append(l[i])
u=set(s)
print(sum(u))
'''d=[]
so=0
for i in s:
    if i not in d:
        so=so+i
print(so)'''
    
    