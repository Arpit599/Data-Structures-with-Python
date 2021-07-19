#Node to store vertex value and the next reference
class AdjNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self):
        self.graph = [] #List that stores the reference of the vertex node
        self.vertices = [] #list that stores only the vertex value
        self.vertexCount = 0 #Number of vertices in the graph

    #Function to add vertex
    def addVertex(self, vertex):
        #Return if vertex is already present
        if self.checkVertexExistence(vertex):
            print("\nVertex {} already present!\n".format(vertex))
            return
        
        newVertex = AdjNode(vertex)
        self.graph.append(newVertex) #Store the reference of the new vertex node
        self.vertices.append(vertex) #Store the vertex value
        self.vertexCount += 1

    #Function to add edge
    def addEdge(self, src, dest):
        #Check whether source and destination vertices exist 
        if not self.srcDestExists(src, dest):
            return
        #Return if source and destination are same
        if src == dest:
            print("\nSource and destination can't be same!\n")
            return
        #Check if there is already an edge
        if self.checkEdgeExistence(src, dest):
            print("\nEdge already present!\n")
            return
        #Accessing vertex head 
        srcHead = self.graph[self.vertices.index(src)]
        #Adding new edge/link at the end
        node = AdjNode(dest)
        while srcHead.next:
            srcHead = srcHead.next
        srcHead.next = node

    #Function to remove vertex 
    def removeVertex(self, vertex):
        #Check whether source and destination vertices exist 
        if not self.checkVertexExistence(vertex):
            print("\nVertex {} not present!\n".format(vertex))
            return
        #Get the required vertex's index in the vertices list
        reqVertexIndex = self.vertices.index(vertex)
        
        self.graph.pop(reqVertexIndex) #Remove the reference of the vertex to be removed
        self.vertexCount -= 1 #Decrease vertex count
        self.vertices.remove(vertex) #Remove the vertex value from the vertices list

        #Remove the edge from all the vertices by traversing list of each vertex
        for i in range(self.vertexCount):
            temp = self.graph[i]
            self.disconnect(temp, vertex)

    #Function to remove edge
    def removeEdge(self, src, dest):
        #Check whether source and destination vertices exist 
        if not self.srcDestExists(src, dest):
            return
        #Return if source and destination are same
        if src == dest:
            print("\nSource and destination can't be same!\n")
            return
        #Check if there is already no edge\
        if not self.checkEdgeExistence(src, dest):
            print("\nEdge already absent!\n")
            return

        #Remove the source to destination edge by traversing list of source vertex
        temp = self.graph[self.vertices.index(src)]
        self.disconnect(temp, dest)

    #Function to remove edges where node is the source node and value is the destination node's vertex value
    def disconnect(self, node, value):
        while node:
            if node.next and node.next.vertex == value:
                node.next = node.next.next
                break
            node = node.next
    
    #Function to check whether source and destination exists
    def srcDestExists(self, src, dest):
        if src not in self.vertices or dest not in self.vertices:
            if src not in self.vertices:
                print("\nVertex {} does not exists!".format(src))
            if dest not in self.vertices:
                print("Vertex {} does not exists!\n".format(dest))
            return False
        return True
    
    #Function to check whether an edge exists between source and destination passed as parameters
    def checkEdgeExistence(self, src, dest):
        srcIndex = self.vertices.index(src)
        srcHead = self.graph[srcIndex]
        srcTemp = srcHead.next
        while srcTemp:
            if srcTemp.vertex == dest:
                return True
            srcTemp = srcTemp.next
        return False
    
    #Function to check whether a vertex exists or not
    def checkVertexExistence(self, vertex):
        if vertex not in self.vertices:
            return False
        return True
    
    #Function to check whether the graph is empty or not
    def isEmpty(self):
        if self.vertexCount == 0:
            print("\nEmpty Graph!\n")
            return True
        return False

    #Function to print the graph
    def printGraph(self):
        #Check whether the graph is empty
        if self.isEmpty():
            return
        for i in range (self.vertexCount):
            print("\nEdges from vertex {}:\n".format(self.vertices[i]), end="")
            temp = self.graph[i].next
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
        print("\n")
    
    #Funtion to print the vertices
    def printVertices(self):
        #Check whether the graph is empty
        if self.isEmpty():
            return
        print("\nVertices are: ", end = "")
        for v in self.vertices:
            print(v, end = " ")
        print("\n")

#Driver code
if __name__ == "__main__":
    graph = Graph()
    while(1):
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Remove vertex")
        print("4. Remove edge")
        print("5. Print graph")
        print("6. Print vertices")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            v = int(input("Enter vertex: "))
            graph.addVertex(v)
        elif choice == 2:
            src, dest = map(int, input("Enter the source and the destination: ").strip().split())
            graph.addEdge(src, dest)
        elif choice == 3:
            if graph.vertexCount == 0:
                print("\nEmpty Graph!\n")
                continue
            v = int(input("Enter vertex: "))
            graph.removeVertex(v)
        elif choice == 4:
            src, dest = map(int, input("Enter the source and the destination: ").strip().split())
            graph.removeEdge(src, dest)
        elif choice == 5:
            graph.printGraph()
        elif choice == 6:
            graph.printVertices()
        else:
            print("\nWrong choice!\n")