def missingNumber(A, N):

    #Sum of the given array
    sumOfN = sum(A)
    #Sum of the first N numbers
    sumActual = N*(N+1)/2
    
    return int(sumActual - sumOfN)

N = 5
A = [1, 4, 2, 3]
print(missingNumber(A, N))