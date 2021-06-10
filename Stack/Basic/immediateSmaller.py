class Solution:

	def immediateSmaller(self,arr,n):
		for i in range(n-1):
		    if arr[i] > arr[i+1]:
		        arr[i] = arr[i+1]
		    else:
		        arr[i] = -1
		arr[len(arr) - 1] = -1

#  Driver Code Starts
if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input("Enter the array: ").split()]
    ob = Solution()
    ob.immediateSmaller(arr, n)
    for x in arr:
        print(x, end = " ")
