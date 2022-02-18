# size=int(input("enter size of the array"))
# l=[]
# for i in range(0,size):
#     element=int(input("enter the number"))
#     l.append(element)
# print(l)
l=list(map(int,input("enter the elements:").split()))
inputIndex = int(input("enter the index"))
inputItem = int(input("enter the item"))
temp = 0

for i in range(len(l)):
    if(i == len(l) - 1):
        temp = l[i]
        l[i] = inputItem
        l.append(temp)
    elif(i >= inputIndex):
        temp = l[i]
        l[i] = inputItem
        inputItem = temp
print(l)
