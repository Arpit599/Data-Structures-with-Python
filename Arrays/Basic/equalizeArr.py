# Here logic is to sort the array first 
# and then count based on differece of elements with the equal number
# The loop considers element one in the front and one in the end
# This requires O(n*logn) time.
def minOperations(arr, N):
        count = 0
        arr.sort()
        sumArr = sum(arr)
        if(sumArr % N != 0):
            return -1
        else:
            equalNum = int(sumArr / N)
            low = 0
            high = N - 1
            while(low < high):
                offset = 0
                if((arr[high] - equalNum) > (equalNum - arr[low])):
                    offset = equalNum - arr[low]
                    arr[low] +=  offset
                    arr[high] -= offset
                    low += 1
                elif((arr[high] - equalNum) < (equalNum - arr[low])):
                    offset = arr[high] - equalNum
                    arr[low] +=  offset
                    arr[high] -= offset
                    high -= 1
                else:
                    offset = arr[high] - equalNum
                    arr[low] +=  offset
                    arr[high] -= offset
                    low += 1
                    high -= 1
                count += offset
            return count    


# Driver code
arr = [5, 3, 2, 6]
n = len(arr) 
print(minOperations(arr, n))