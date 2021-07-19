class Solution:
    def rearrangeArray(self, arr, n):
        arr.sort()
        arrTemp = []
            
        low = 0
        high = n - 1
        while(low <= high):
            if(low == high):
                arrTemp.append(arr[low])
                break
            arrTemp.append(arr[low])
            low += 1
            arrTemp.append(arr[high])
            high -= 1
        
        arr.clear()
        #In-place operation
        arr += arrTemp
        return arr

#  Driver Code Starts
if __name__ == '__main__':
    tc = int(input("Enter the number of test cases: "))
    while tc > 0:
        n = int(input("Enter n: ").strip())
        arr = list(map(int, input("Enter array: ").strip().split()))
        Solution().rearrangeArray(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
