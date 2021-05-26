class Solution:
    def winner(self, x, m, n, arr):
        ramWin, rohanWin = 0, 0
        for i in range(x):
            if(arr[i] % m == 0):
                ramWin += 1
            elif(arr[i] % n == 0):
                rohanWin += 1
        if(ramWin > rohanWin):
            return "Ram"
        elif(ramWin < rohanWin):
            return "Rohan"
        else:
            return "Both"

if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        x = int(input("Enter the number of opponents: "))
        m, n = [int(a) for a in input("Enter respective strengths of Ram and Rohan: ").split()]
        arr = list(map(int, input("Enter the strength of the opponents: ").split()))        
        ob = Solution()
        print(ob.winner(x, m, n, arr))
