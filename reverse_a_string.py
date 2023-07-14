s=input()
s=s.split()
d=s[::-1]

p=[]
for i in d:
    v=i[::-1]
    p.append(v)
print(*p)