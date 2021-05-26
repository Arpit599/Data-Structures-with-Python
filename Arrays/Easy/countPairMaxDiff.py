def countPairs(arr, n):
    
    if n == 1:
        return 0
        
    minEle, maxEle = 100000, 0
    countArr = [0] * 100000

    for i in range(n):
        if(arr[i] < minEle):
            minEle = arr[i]
        if(arr[i] > maxEle):
            maxEle = arr[i]
        countArr[arr[i]] += 1
    
    return countArr[minEle] * countArr[maxEle]

#  Driver Code Starts
t = int(input("Enter the number of test cases: "))
for _ in range(0, t):
    n = int(input("Enter the value of n: "))
    a = list(map(int, input("Enter the array: ").split()))
    ans = countPairs(a, n)
    print("Number of pairs with max absolute difference:", ans)