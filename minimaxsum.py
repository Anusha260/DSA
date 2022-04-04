
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    s = sum(arr)
    maxsum = s-arr[0]
    minsum = s-arr[len(arr)-1]
    
    print(minsum, maxsum)

arr = list(map(int,input("enter the elements:").split()))
miniMaxSum(arr)
