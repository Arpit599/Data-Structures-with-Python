class Solution:
    def firstElement(self, arr, n, k): 
        maxVal = max(arr)
        tempList = [0] * (maxVal + 1)
        
        for i in range(n):
            tempList[arr[i]] += 1
        
        for i in range(n):
            if(tempList[arr[i]] == k):
                return arr[i]

        return -1

t = int(input("Enter the number of test cases: "))
for _ in range(0, t):
    n, k = list(map(int, input("Enter n and k: ").split()))
    a = list(map(int, input("Enter the array: ").split()))
    ob = Solution()
    print("Given voucher to the user with ID: " + str(ob.firstElement(a, n, k)))
