class Solution:
    def countArray (self, arr, n, x) : 
        countArr = [0] * n
        tempArr = arr.copy()
        tempArr.sort()
        for i in range(n):
            avg = int((arr[i] + x) / 2)
            low = 0
            high = n - 1
            count = 0
            for j in range(n):
                if(tempArr[j] == avg):
                    count += 1
                elif(tempArr[j] > avg):
                    break
            countArr[i] = count
        
        return countArr

for _ in range(0,int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ans = Solution().countArray(arr, n, x)
    print(*ans)
