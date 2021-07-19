def game_with_number (arr,  n) : 
    for i in range(n - 1):
        arr[i] = arr[i] ^ arr[i + 1]
    return arr

#  Driver Code Starts

for tc in range(0, int(input("Enter the number of test cases: "))):
    
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the array: ").strip().split()))
    res = game_with_number(arr, n);
    print(*res)
