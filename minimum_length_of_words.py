s=input()
s=s.split()
min=9999999
for i in s:
    if(len(i)<min):
        min=len(i)
print(min)