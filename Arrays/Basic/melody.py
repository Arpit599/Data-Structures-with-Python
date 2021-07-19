def max_adjacent_sum (arr, n) : 
    arr.sort()
    maxVal = 0
    for i in range(n-1):
        maxVal = max(maxVal, arr[i] + arr[i + 1])
    return (arr[n - 1] + arr[n - 2])

#  Driver Code Starts
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = max_adjacent_sum(arr, n)
    print(ans)