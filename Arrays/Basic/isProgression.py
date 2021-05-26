class Solution:
    def checkIsAP(self, arr, n):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(n - 1):
            if(arr[i + 1] - arr[i] != diff):
                return False
        return True
    

#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    n=int(input())

    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.checkIsAP(a,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")
