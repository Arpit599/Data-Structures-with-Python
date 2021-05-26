def countPairs(arr, n):
    
    if n == 1:
        return 0
        
    minEle, maxEle = 100000, -100000

    for i in range(n):
        minEle = min(arr[i], minEle)
        maxEle = max(arr[i], maxEle)
    
    minCount, maxCount = 0, 0
    for i in range(n):
        if arr[i] == minEle:
            minCount += 1
        elif arr[i] == maxEle:
            maxCount += 1
    
    # If the elements are equal
    if minEle == maxEle:
        return (n * (n - 1) // 2)
    # If the elements are not equal
    return minCount * maxCount

#  Driver Code Starts
t = int(input("Enter the number of test cases: "))
for _ in range(0, t):
    n = int(input("Enter the value of n: "))
    a = list(map(int, input("Enter the array: ").split()))
    ans = countPairs(a, n)
    print("Number of pairs with max absolute difference:", ans)