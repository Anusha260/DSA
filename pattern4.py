n=int(input("enter the number"))
 
for i in range(0,n):
    for j in range(0,i):
        print("",end=" ")
    for x in range(0,n-i):
        print("*",end=" ")
    
    print()
    
for k in range(0,n-1):
    for y in range(0,n-2-k):
        print("",end=" ")
    for z in range(0,k+2):
        print("*",end=" ")
    print()
    


