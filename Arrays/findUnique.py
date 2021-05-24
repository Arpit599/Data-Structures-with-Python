class Solution:
    def findUnique(self, a, n, k): 
        a.sort()

        dict = {}
        for i in range(n):
            if(a[i] not in dict.keys()):
                dict[a[i]] = 1
            else:
                dict[a[i]] += 1

        for i in range(n):
            if(dict[a[i]] % k == 1):
                return a[i]
            
#  Driver Code Starts
if __name__=='__main__':
    T = int(input("Enter the number of test cases: "))

    for _ in range(T):
        n, k = [int(x) for x in input("Enter n and k: ").split()]
        a = [int(x) for x in input("Enter the array: ").split()]

        print("The unique element is", Solution().findUnique(a,n,k))
