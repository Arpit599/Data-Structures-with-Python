class Solution:
    def firstElementKTime(self,  a, n, k):
        maxVal = max(a)
        tempArr = [0] * (maxVal + 1)
        for i in range(n):
            tempArr[a[i]] += 1
            if(tempArr[a[i]] == k):
                return a[i]
        return -1
    
#  Driver Code Starts
def main():

    T = int(input("Enter the number of test cases: "))
    while(T > 0):
        sz = [int(x) for x in input("Enter n and k: ").strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input("Enter the array: ").strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))
        T -= 1

if __name__ == "__main__":
    main()