def check (arr,  brr, n) : 

    arrCount = [0] * 10

    for i in range(n):
        arrCount[arr[i]] += 1
    for j in range(n):
        arrCount[brr[j]] -= 1
    for k in range(10):
        if arrCount[k] != 0:
            return 0
    return 1
    
#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    
    n = int(input("Enter the value of n: "))
    arr = list(map(int, input("Enter array 1: ").strip().split()))
    brr = list(map(int, input("Enter array 2: ").strip().split()))
    
    if(check(arr, brr, n)):
        print("Identical")
    else:
        print("Not identical")