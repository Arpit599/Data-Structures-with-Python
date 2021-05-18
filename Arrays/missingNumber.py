def missingNumber(A, N):
     # Your code goes here
     sumOfN = sum(A)
     sumActual = N*(N+1)/2
     return int(sumActual - sumOfN)

N = 5
A = [1, 4, 2, 3]
print(missingNumber(A, N))