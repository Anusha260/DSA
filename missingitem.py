l=[[9,8,-1],[7,5,6],[3,2,1]]
a=[]
for i in l:
    for j in i:
        a.append(j)
# print(a)

n=len(l)
sqruare=n**2
for k in range(1,sqruare+1):
    if k not in a:
        print(k)

