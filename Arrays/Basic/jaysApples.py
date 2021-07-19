def minimum_apple (arr, n) : 
    maxVal = max(arr)
    hashList = [0] * (maxVal + 1)
    
    count = 0
    for i in range(n):
        if(hashList[arr[i]] != 0):
            continue
        hashList[arr[i]] += 1
        count += 1
    return count

#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    n = int(input("Enter lenght of the queue: "))
    arr = list(map(int, input("Enter the ids: ").strip().split()))
    ans = minimum_apple(arr, n)
    print("Minimum kgs of apple required", ans)