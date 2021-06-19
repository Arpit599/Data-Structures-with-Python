#Function to find max sum of a cycle
def maxWeightNode(arr):
    n = len(arr)
    weightArr = [0] * n
    #Node with maximum node
    maxWeightNode = -1
    #Max count for incoming edges so far
    maxCount = -1
    #Traverse through the array to store the node count
    for i in range(n):
        if arr[i] != -1:
            weightArr[arr[i]] += 1
            #If weight of this node is greater than maxCount, update
            if weightArr[arr[i]] > maxCount:
                maxCount = weightArr[arr[i]]
                maxWeightNode = arr[i]
    
    return maxWeightNode

if __name__ == "__main__":
    testCases = int(input("Enter the number of test cases: "))
    while testCases > 0:    
        arr = list(map(int, input("Enter the graph: ").strip().split()))
        print("Max weight node:", maxWeightNode(arr))
        testCases -= 1
