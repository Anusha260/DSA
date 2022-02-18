size=int(input("enter size of the array"))
list=[]
for i in range(0,size):
    element=int(input("enter the number"))
    list.append(element)
print(list)
position=int(input("enter the position"))
if (position<=0 or position>size):
    print("invalid position")
else:
   
    ps=position-1
    a=list[0:ps]
    b=list[position:]
    print(a+b)
    