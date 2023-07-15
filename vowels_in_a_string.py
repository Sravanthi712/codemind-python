s=input()
v=input()
f=0
for i in range(len(s)):
    if s[i]==v:
        f=1
if(f==1):
    print("True")
    print(s.index(v))
else:
    print("False")
        