class Solution:
    def maxPoint(self, n, k, a, b):
        maxPoint = 0
        for i in range(n):
            readCount = int(k/a[i])
            readPoints = readCount * b[i]
            if(readPoints >= maxPoint):
                maxPoint = readPoints        
        return maxPoint
            
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        N, K = [int(x) for x in input("Enter the number of books and reading time alloted: ").split()]
        A = list(map(int, input("Enter the individual book reading time: ").split()))
        B = list(map(int, input("Enter the corresponding point of the book: ").split()))
        ob = Solution()
        print("Maxpoints: " + str(ob.maxPoint(N, K, A, B)))
