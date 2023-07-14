s=input()
s=s.split()
k=[]
for i in s:
    v=i[::-1]
    k.append(v)

print(*k)