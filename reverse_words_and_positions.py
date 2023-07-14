s=input()
s=s.split()
k=s[::-1]
x=[]
for i in k:
    v=i[::-1]
    x.append(v)
print(*x)
    