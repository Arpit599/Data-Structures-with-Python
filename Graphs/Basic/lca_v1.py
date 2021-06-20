global path1 
path1 = []
global path2 
path2 = []

def getPath(node, searchVal, path):
    if node == None:
        return False
    path.append(node.data)
    if node.data == searchVal:
        return True
    if getPath(node.left, searchVal, path) or getPath(node.right, searchVal, path):
        return True
    path.pop()
    return False

def LCA(root, n1, n2):
    global path1
    global path2

    if not getPath(root, n1, path1) or not getPath(root, n2, path2):
        return -1
    
    pointChange = -1

    for i in range(len(path1) if len(path1) < len(path2) else len(path2)):
        if path1[i] != path2[i]:
            break
    print("Path1", path1)
    print("Path2", path2)
    pointChange = i - 1
    return path1[pointChange]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print("The LCA is", LCA(root, 8, 10))
