#Function to find max sum of a cycle
def maxCycleSum(arr):
    n = len(arr)
    cycleSum = -1
    #Checking whether a loop exists from every node, if yes then find sum
    for i in range(n):
        #Start from i index
        startIndex = i
        #Keep a record of all the visited nodes from the current node
        visited = {}
        #Temp sum for this node
        sum = 0
        #Find the loop sum, else break
        while True:
            if visited.get(startIndex):
                break
            #Set visited node to true
            visited[startIndex] = True
            sum += startIndex
            #Update the startIndex
            startIndex = arr[startIndex]
            #If the starting node comes again that means there is a loop
            if startIndex == i:
                cycleSum = max(cycleSum, sum)
    return cycleSum

if __name__ == "__main__":
    testCases = int(input("Enter the number of test cases: "))
    while testCases > 0:    
        arr = list(map(int, input("Enter the graph: ").strip().split()))
        print("Max cycle sum:", maxCycleSum(arr))
        testCases -= 1
