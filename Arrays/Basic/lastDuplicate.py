def dupLastIndex (arr, n) : 
    for i in range(n - 1, -1, -1):
        if(arr[i] == arr[i-1]):
            return [i, arr[i]]
    return [-1]

#  Driver Code Starts
for _ in range(0, int(input("Enter the number of test cases: "))):
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the array: ").strip().split()))
    ans = dupLastIndex(arr, n)
    print("The index and last duplicate element are: ", *ans)
    
