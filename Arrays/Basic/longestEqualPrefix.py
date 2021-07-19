def findIndex(arr,X,Y,N):
    #Max index with equal number of X and Y
    prefIndex = -1
    countX = 0
    countY = 0
    
    #Index of number that is not X or Y
    lastOccIndex = -1
    
    for i in range(N):
        if(arr[i] == X or arr[i] == Y):
            if (arr[i] == X):
                countX += 1
            else:
                countY += 1
            if(countX == countY):
                prefIndex = i
        elif(countX != 0 or countY != 0) and (countX == countY):
            lastOccIndex = i
            
    if(lastOccIndex > prefIndex):
        prefIndex = lastOccIndex

    return prefIndex

N, X, Y = 11, 7, 42
arr = [ 7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7 ]
print(findIndex(arr, X, Y, N))