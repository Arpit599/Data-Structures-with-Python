def maxPerimeter (arr, n) : 
    arr.sort()
    for i in range(n - 2, 0, -1):
        prefixSum = arr[i] + arr[i - 1]
        if(prefixSum > arr[i + 1]):
            return prefixSum + arr[i + 1]
        else:
            prefixSum = 0
    return -1

#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the array: ").strip().split()))
    
    print(maxPerimeter(arr, n))