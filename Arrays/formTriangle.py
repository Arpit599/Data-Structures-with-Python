class Solution:
    def noOfTriangles( self, arr, n):
        arr.sort()
        count = 0
        for i in range(n-1, 1, -1):
            low = 0 
            high = i - 1
            while(low < high):
                if(arr[low] + arr[high] > arr[i]):
                    count += high - low 
                    high -= 1
                else:
                    low += 1  
        return count

#  Driver Code Starts
def main():

    T = int(input("Enter the number of test cases: "))

    while(T > 0):
        n = int(input("Enter n: "))
        a = [int(x) for x in input("Enter array: ").strip().split()]
        ob = Solution()
        print("The possible number of triangles are", ob.noOfTriangles(a, n))

        T -= 1

if __name__ == "__main__":
    main()

