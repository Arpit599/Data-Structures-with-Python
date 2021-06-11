class AdjNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount
        self.graph = [None] * self.vertexCount
    
    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):
        for i in range (self.vertexCount):
            print("\nEdges from vertex {}:\nhead".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
        print("\n")
        
if __name__ == "__main__":
    vertexCount = int(input("Enter the number of vertices: "))
    graph = Graph(vertexCount)
    while(1):
        print("1. Add edge to the graph")
        print("2. Print the graph")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            src = int(input("Enter the source: "))
            dest = int(input("Enter the destination: "))
            graph.addEdge(src, dest)
        elif choice == 2:
            graph.printGraph()
        else:
            print("Wrong choice!")
