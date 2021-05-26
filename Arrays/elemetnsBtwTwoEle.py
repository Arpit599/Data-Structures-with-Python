class Solution:
    def getCount(self,arr, n, num1, num2): 
        num1Index, num2Index = -1, -1
        for i in range(n):
            if(arr[i] == num1 and num1Index == -1):
                num1Index = i
            if(arr[i] == num2 and num2Index < i):
                num2Index = i
        return (num2Index - num1Index - 1) if (num1Index != num2Index) else 0

#  Driver Code Starts
for tc in range(0, int(input("Enter the number of test cases: "))):
    n = int(input("Enter the size n: "))
    arr = list(map(int, input().strip("Enter the array: ").split()))
    num1, num2 = map(int, input("Enter the number1 and number2: ").strip().split())
    ob = Solution()
    v = ob.getCount(arr, n, num1, num2)
    print(v)
    