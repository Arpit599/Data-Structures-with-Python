def findDifference(a1, a2, n):

    diffCount = 0
    
    for i in range(n):
        if(a1[i] != a2[i]):
            j = i + 1
            
            while(a1[i] != a2[j]):
                j += 1

            while(i != j):
                temp = a2[j]
                a2[j] = a2[j - 1]
                a2[j - 1] = temp
                j -= 1
                diffCount += 1
                
    return diffCount
    
#  Driver Code Starts
t = int(input("Enter the number of test cases: "))
for _ in range(0, t):
    n = int(input("Enter the value of n: "))

    a = list(map(int, input("Enter ranking order by first friend: ").split()))
    b = list(map(int, input("Enter ranking order by second fried").split()))
    ans = findDifference(a, b, n)
    print(ans)