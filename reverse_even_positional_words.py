s=input()
s=s.split()
k=[]
for i in range(len(s)):
    y=s[i]
    if i%2==0:
        x=s[i]
        y=x[::-1]
    k.append(y)
'''v=[]
for i in k:
    x=v[::-1]
    v.append(x)'''
print(*k)
    