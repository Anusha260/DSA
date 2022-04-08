# N=int(input("enter the number"))
# grid=[]
# for i in range(0,N):
#     list1=[int(i) for i in input("enter the number").split()]
#     grid.append(list1)
# count=0
# sum1=0
# sum2=0
# j1=0
# j2=N-1
# while(count<N):
#     sum1=sum1+grid[count][j1]
#     sum2=sum2+grid[count][j2]
#     count+=1
#     j1+=1
#     j2-=1
# print(sum1-sum2)

def diagonalDifference(arr):
    # Write your code here
    rightdiag=0
    leftdiag=0
    for i in range(n):
        leftdiag +=arr[i][i]
        rightdiag +=arr[i][n-1-i]
    return (abs(leftdiag-rightdiag))
n=int(input("enter the number"))


