l=[12,3,5,6]
n=len(l)
for i in range (1,n):
    for j in range (1,i):
        if l[i-1]+l[j]==15:
            print(i-1,j)

