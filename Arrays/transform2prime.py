#Making a big enough primeList boolean array
primeList = [True] * 100000
   
#Function to generate primeList
def sieveEratosthenes():
    p = 2
    while(p * p <= 100000):
        for i in range(p*p, 100000, p):
            primeList[i] = False
        p += 1

#Function to find the minimum number required in the question
def minNumber(arr,N):
    sum = 0
    for i in range(N):
        sum += arr[i]
    
    sieveEratosthenes()

    if(primeList[sum]):
        return 0
    else:
        for i in range(sum + 1, 100000):
            if(primeList[i]):
                return i - sum

arr = [ 2, 4, 6, 8, 12 ]
print (minNumber(arr, len(arr)))