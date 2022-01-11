l=[12,3,5,6]
n=len(l)
number=15
for i in range (0,n):
    for j in range (0,i):
        if l[i]+l[j]==number:
            print(i,j)
