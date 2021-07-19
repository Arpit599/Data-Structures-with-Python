#Function to return the nearest cell accessible from both the nodes
def findMeetingCell(arr, src, dest):
    #Common reachable node
    meetingCell = None
    #Start from node next to src
    startSrc = arr[src]
    #Start from node next to dest
    startDest = arr[dest]
    n = len(arr)
    #list to store the distance of every accessible node from src
    distanceSrc = [-1] * n

    #To maintain the node distance from src
    count = 1
    #Initialize the distance from source for source node to be zero
    distanceSrc[src] = 0
    #Run loop until dead-end or loop is encountered
    while True:
        #To check loop present or not
        if startSrc == -1 or distanceSrc[startSrc] != -1:
            break
        #If dead-end then break
        if arr[startSrc] == -1:
            break
        #Store distance of the current node from the src node
        distanceSrc[startSrc] = count
        #Update startSrc to be the next accesible node
        startSrc = arr[startSrc]
        count += 1

    #Again initialize count to 1, as this time we will use it for dest node
    count = 1
    #Variable to store the minimum sum of distances from src and dest
    minSumDist = 100000
    #Dictionary to store the visited nodes
    visited = {}
    #Mark the destination node to be visited
    visited[dest] = True

    #Run loop until a node is already visited or a dead-end occurs
    while True:
        #Check if the node has been already visited
        if visited.get(startDest):
            break
        else:
            visited[startDest] = True
        #Update minSumDist if it is the minimum so far
        if distanceSrc[startDest] > 0 and distanceSrc[startDest] + count < minSumDist:
            meetingCell = startDest
            minSumDist = distanceSrc[startDest] + count
        #Check if this is the dead-end
        if startDest != -1 and arr[startDest] == -1:
            break
        #Update startSrc to be the next accesible node
        startDest = arr[startDest]
        count += 1

    return meetingCell

if __name__ == "__main__":
    testCases = int(input("Enter the number of test cases: "))
    while testCases > 0:    
        arr = list(map(int, input("Enter the graph: ").strip().split()))
        src = int(input("Enter the source: "))
        dest = int(input("Enter the destination: "))
        print("Nearest common accessible node:", findMeetingCell(arr, src, dest))
        testCases -= 1
