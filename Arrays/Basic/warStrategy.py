def min_soldiers (arr, n, K) : 
    #For calculating the number of soldiers required in each troop
    for i in range(n):
        if(arr[i] % K == 0):
            arr[i] = 0
        else:
            nearestMultiple = int(arr[i]/K) + 1
            arr[i] = nearestMultiple * K - arr[i]
            
    requiredCount = 0
    if(n % 2 == 0):
        requiredCount = int(n/2)
    else:
        requiredCount = int(n/2) + 1

    luckyTroopsCount = 0
    minSoldiersCount = 0
    arr.sort()   #Sorting so that smaller elements are included for calculating min soldiers required
    for i in range(n):
        minSoldiersCount += arr[i]
        luckyTroopsCount += 1
        if(luckyTroopsCount == requiredCount):
            return minSoldiersCount

n, K = map(int, input("Enter the number of troops and lucky number: ").split())
arr = list(map(int, input("Enter the troops: ").strip().split()))
ans = min_soldiers(arr, n, K)
print("Minimum number of soldiers required to win the war: " + str(ans))