def maxSum(arr,n):
    #Deep copy
    arrTemp = arr.copy()
    arrTemp.sort()

    oddIndex  = 0
    odd = 0
    while odd < n:
        arr[odd] = arrTemp[oddIndex]
        odd += 2
        oddIndex += 1

    evenIndex = n - 1
    even = 1
    while even < n:
        arr[even] = arrTemp[evenIndex]
        even += 2
        evenIndex -= 1

    sum = 0
    for i in range(1, n):
        sum += abs(arr[i - 1] - arr[i])
    
    return (sum + abs(arr[0] - arr[n - 1]))

    ##########Solution 2#############

def maxSum(arr,n):
    # code here
    arr.sort()
    sum = 0
    for i in range(0, int(n/2)):
        sum -= 2 * arr[i]
        sum += 2 * arr[n - i - 1]
        # print(sum)
    
    return sum

arr = [4, 2, 1, 8]
print(maxSum(arr, len(arr)))
        