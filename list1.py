num=int(input("enter the number"))
i=0
list=[]
while i<num:
    l=int(input("enter the number"))
    list.append(l)
    i=i+1
a=list[::-1]
print(a)