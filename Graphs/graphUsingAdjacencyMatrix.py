graph = []
vertices = []
vertices_num = 0

def addVertex(vertex):
    global graph, vertices, vertices_num

    #Check if vertex is already present
    if vertex in vertices:
        print("Vertex already present!")
        return
    #If not present, add new vertex
    vertices_num += 1
    vertices.append(vertex)
    tempRow = []
    #For adding new zero column in the existing graph
    if vertices_num > 1:
        for row in graph:
            row.append(0)
    #For adding new zero row in the existing graph
    for i in range(vertices_num):
        tempRow.append(0)
    graph.append(tempRow)

def addEdge(src, dest):
    global graph, vertices
    #If either the source or destination does not exists then return
    if src not in vertices or dest not in vertices:
        if src not in vertices:
            print("Vertex {} does not exists!".format(src))
        if dest not in vertices:
            print("Vertex {} does not exists!".format(dest))
        return 
    #Can't have a self loop on any node
    if src == dest:
        print("Source and destination can not be same!")
        return
    #If there is already an edge between source and destination
    if graph[vertices.index(src)][vertices.index(dest)] == 1 \
        or graph[vertices.index(dest)][vertices.index(src)] == 1:
        print("Edge already present!")
        return

    #Add new edge if none of the above case is present
    graph[vertices.index(src)][vertices.index(dest)] = 1
    graph[vertices.index(dest)][vertices.index(src)] = 1

def removeVertex(vertex):
    global graph, vertices_num, vertices

    #If there are no vertices then return
    if len(vertices) == 0:
        print("No vertex in the graph!")
        return
    #If the vertex is not present already, return
    if vertex not in vertices:
        print("Vertex not present!")
        return
    
    #Find index of the vertex to be removed in the vertices list
    index = vertices.index(vertex)
    while index < vertices_num - 1:
        #Shift the columns to the left
        for i in range(vertices_num):
            graph[i][index] = graph[i][index + 1]
        #Shift the rows upwards
        for i in range(vertices_num):
            graph[index][i] = graph[index + 1][i]
        index += 1
        
    vertices.remove(vertex)
    vertices_num -= 1

def removeEdge(src, dest):
    global graph, vertices

    #If either the source or destination does not exists then return
    if src not in vertices or dest not in vertices:
        if src not in vertices:
            print("Vertex {} does not exists!".format(src))
        if dest not in vertices:
            print("Vertex {} does not exists!".format(dest))
        return 
    #Self loops are not allowed, return
    if src == dest:
        print("Source and destination can not be same!")
        return

    #If there is no edge between source and destination
    if graph[vertices.index(src)][vertices.index(dest)] == 0 \
        or graph[vertices.index(dest)][vertices.index(src)] == 0:
        print("Edge already absent!")
        return

    #Remove edge if none of the above case is present
    graph[vertices.index(src)][vertices.index(dest)] = 0
    graph[vertices.index(dest)][vertices.index(src)] = 0

def printGraph():
    printVertices()
    for i in range(vertices_num):
        print("Vertex {} connections: ".format(vertices[i]), end = "")
        for j in range(vertices_num):
            print(graph[i][j], end = " ")
        print()

def printVertices():
    print("Vertices are: ", end = "")
    for vertex in vertices:
        print(vertex, end = " ")
    print()

if __name__ == "__main__":
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
            addVertex(v)
        elif choice == 2:
            src, dest = map(int, input("Enter the source and the destination: ").strip().split())
            addEdge(src, dest)
        elif choice == 3:
            v = int(input("Enter vertex: "))
            removeVertex(v)
        elif choice == 4:
            src, dest = map(int, input("Enter the source and the destination: ").strip().split())
            removeEdge(src, dest)
        elif choice == 5:
            printGraph()
        elif choice == 6:
            printVertices()
        else:
            print("Wrong choice!")