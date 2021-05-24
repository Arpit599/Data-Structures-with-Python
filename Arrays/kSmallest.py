class Solution:
    def kSmallestElements (self, arr, n, k) : 

        maxVal = max(arr)
        #To store the count of individual elements
        hash = [0] * (maxVal + 1)
        #To store the k value that each element should get starting from the smallest number
        kHash = [0] * (maxVal + 1)

        #Storing the count of each element
        for i in range(n):
            hash[arr[i]] += 1

        #Assigining k value that each element should get
        for i in range(1, len(hash)):
            if(hash[i] != 0):
                if(k > hash[i]):
                    kHash[i] = hash[i]
                    k -= hash[i]
                else:
                    kHash[i] = k
                    k = 0
                if(k == 0):
                    break

        index = -1
        arrayToReturn = []
        #Building the new array 
        for i in range(n):
            if(kHash[arr[i]] != 0):
                arrayToReturn.append(arr[i])
                kHash[arr[i]] -= 1
        
        return arrayToReturn  

#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    
    n, K = map(int, input("Enter the value of n and K: ").split())
    arr = list(map(int, input("Enter the array: ").strip().split()))
    res = Solution().kSmallestElements(arr, n, K)
    print(*res)