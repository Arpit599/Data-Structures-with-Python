class Solution:
    def findMissing(self,  a, b, n):
        sumA = sum(a)
        sumB = sum(b)
        return sumA - sumB

def main():
    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findMissing(a, b, n))
        T -= 1
