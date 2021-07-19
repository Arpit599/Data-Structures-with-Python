class Solution:
    def areElementsContiguous (self,arr, n) : 
        #Complete the function
        hash = [0] * 100000
        for i in range(n):
            if(arr[i] == "END"):
                hash = [0] * 100000
            else:
                hash[int(arr[i])] += 1
        
        count = 0
        for i in range(100000):
            count += hash[i] % 2
        return count
            
#  Driver Code Starts

for tc in range(0, int(input())):
    n = int(input())
    arr = list(map(str, input().strip().split()))
    ob = Solution()
    res = ob.areElementsContiguous(arr, n)
    print(res)
