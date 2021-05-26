def inversePermutation (arr, n) : 
    arr1 = [0] * n
    for i in range(n):
        arr1[arr[i] - 1] = i + 1
    return arr1

# Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    n = int(input("Enter n: "))
    arr = list(map(int, input("Enter the array: ").strip().split()))
    ans = inversePermutation(arr, n)
    print("The inverse permutation is", *ans)