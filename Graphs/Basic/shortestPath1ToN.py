import math
class Solution:
    #Start from the end to get min steps, if we start from front we wont get min 
    def minStep (self, n):
        count = 0
        while n != 1:
            #If multiple of 3 then reduce n to n/3
            if n % 3 == 0:
                n = int(n/3)
            #If not multiple of 3 then reduce n by 1
            else:
                n -= 1
            count += 1
            
        return count

#  Driver Code Starts
if __name__ == '__main__': 
    testCase_num = int(input("Enter the number of test cases: "))
    for tc in range (testCase_num):
        n = int(input("Enter the number of vertices: "))
        ob = Solution()
        print("Minimum number of steps required:", ob.minStep(n))
