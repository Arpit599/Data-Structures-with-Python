n1Exists = False
n2Exists = False

def LCA(root, n1, n2):
    global n1Exists
    global n2Exists
    if root == None:
        return None
    print("Node rn", root.data)
    if root.data == n1 or root.data == n2:
        if root.data == n1:
            n1Exists = True
        else:
            n2Exists = True
        
        # if not n1Exists or not n2Exists:
        #     leftLCA = LCA(root.left, n1, n2)
        #     rightLCA = LCA(root.right, n1, n2)
        # else:
        #     return root
        return root
    leftLCA = LCA(root.left, n1, n2)
    rightLCA = LCA(root.right, n1, n2)

    if leftLCA == None and rightLCA == None:
        return None
    
    if leftLCA != None and rightLCA != None:
        return root

    return leftLCA if leftLCA != None else rightLCA
    

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
    lca = LCA(root, 10, 12).data
    if not n1Exists or not n2Exists:
        print("Nodes are not present!", n1Exists, n2Exists)
    else:
        print("The LCA is", lca)
    # print("The LCA is", lca)
