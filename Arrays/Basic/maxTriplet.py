class Solution:
    def maxTripletSum (self, arr,  n) : 
        first, second, third = -100000, -100000, -100000
        
        for i in range(n):
            if(arr[i] > third):
                first = second
                second = third
                third = arr[i]
            elif(arr[i] > second):
                first = second
                second = arr[i]
            elif(arr[i] > first):
                first = arr[i]
                
        return first + second + third

#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    
    n = int(input("Enter the value of n: "))
    arr = list(map(int, input("Enter the array: ").strip().split()))
    ob = Solution()
    res = ob.maxTripletSum(arr, n)
    print("The max triplet sum:", res)