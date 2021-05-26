def pendulumArrangement(arr, n):
    
    arr.sort()
    tempArr = arr.copy()

    #Starting index for left part
    indexL = 0    
    #Starting index for right part
    indexR = 1

    #For making left part 
    for i in range(int((n-1)/2), -1 , -1):
        arr[i] = tempArr[indexL]
        indexL += 2

    #For making right part 
    for i in range(int((n-1)/2) + 1, n):
        arr[i] = tempArr[indexR]
        indexR += 2
    
    return arr

n = 5
arr = [11, 12, 31, 14, 5]
print(pendulumArrangement(arr, n))