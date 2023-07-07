x=input().lower()
y=input().lower()
x1=x.split()
y1=y.split()
c=0
for i in x1:
    for j in y1:
        if(i==j):
            c+=1
print(c)
        