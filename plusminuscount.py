def plusMinus(arr):
    positive=0
    negative=0
    z=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            positive+=1
        elif arr[i<0]:
            negative+=1
        else:
            z=z+1
    print(positive/len(arr))  
    print(negative/len(arr))
    print(z/len(arr)) 

arr=[1,-3,4,-5,0,0,9]
plusMinus(arr)