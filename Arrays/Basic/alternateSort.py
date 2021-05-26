class Solution:
    def customSort(self, arr, n):
        arrLeft = []
        arrRight = []
        mid = int(n/2) 
        
        arrLeft = arrLeft + arr[0:mid]
        arrLeft.sort()
        # print(arrLeft)
        arrRight = arrRight + arr[mid:n]
        arrRight.sort(reverse = True)
        # print(arrRight)
        newArr = arrLeft + arrRight
        # print(newArr)
        arr.clear()
        # arr += newArr
        arr.extend(newArr)

#  Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))

        Solution().customSort(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1