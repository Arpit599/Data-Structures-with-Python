def minOperations(arr, N):
    sumArr = sum(arr)
    if(sumArr % N != 0):
        return -1
    else:
        diff_sum = 0
        equalNum = int(sumArr / N)
        for i in range(N):
            diff_sum += abs(arr[i] - equalNum) 
        
        return int(diff_sum/2)  

# Driver code
arr = [5, 3, 2, 6]
n = len(arr) 
print(minOperations(arr, n))