class Solution:
    def sumOfDependencies(self, adj, V):
        sum = 0
        for i in range(V):
            edges = a[i]
            sum += len(edges)
        return sum
            
#  Driver Code Starts
import math

if __name__=='__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        N, M = map(int,input().strip("Enter number of vertices and edges: ").split())
        a = [[] for i in range(N)]
        s = list(map(int,input("Enter the list: ").strip().split()))
        for i in range(0, 2 * M, 2):
            x = s[i]
            y = s[i + 1]
            a[x].append(y)
        ob = Solution()
        print(ob.sumOfDependencies(a, N))