#Class Node to define contents of node object
class Node:
     #Constructor function
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
#Class Tree for initializing root and tree operations
class Tree:
    #Constructor function
    def __init__(self):
        self.root = None

    #Function to insert new node, based on level-order traversal/BFS
    def insertion(self, data):
        newNode = Node(data)
        #If this is the first node in the tree
        if self.root == None:
            self.root = newNode
            return
        #Otherwise look for the first empty place in the tree
        queue = []
        queue.append(self.root)
        temp = queue[0]
        while len(queue):
            temp = queue.pop(0)
            #If the left child is empty, insert
            if not temp.left:
                temp.left = newNode
                break
            #Otherwise enque left child to explore it later
            else:
                queue.append(temp.left)
            #If the right child is empty, insert
            if not temp.right:
                temp.right = newNode
                break
            #Otherwise enque right child to explore it later
            else:
                queue.append(temp.right)

    #Function to find the node to be deleted, uses level-order traversal/BFS
    def deletion(self, nodeValue):
        #If root is None then tree is empty
        if self.root == None:
            print("\nTree is empty!\n")
            return
        #If there is single node
        if self.root.left == None and self.root.right == None:
            #If single node's value is equal to the required value
            if self.root.data == nodeValue:
                self.root = None
                return
            #Otherwise value is not present
            else:
                print("\nValue not present!\n")
                return
        #Use BFS to go to the last node, and also to find the required node
        queue = []
        queue.append(self.root)
        foundNode = None
        temp = None
        while len(queue):
            temp = queue.pop(0)
            #If root is to be deleted
            if temp.data == nodeValue:
                foundNode = temp
            #Move to left sub-tree
            if temp.left:
                if temp.left.data == nodeValue:
                    foundNode = temp.left
                queue.append(temp.left)
            #Move to right sub-tree
            if temp.right:
                if temp.right.data == nodeValue:
                    foundNode = temp.right
                queue.append(temp.right)
        #If value to be deleted doesn't exists
        if foundNode == None:
            print("\nValue not present\n")
            return
        #If value to be deleted exists
        foundNode.data = temp.data
        self.removeNode(temp)

    #Function to delete the node, uses level-order traversal/BFS
    def removeNode(self, node):
        queue = []
        queue.append(self.root)
        while len(queue):
            temp = queue.pop(0)
            #If left child is the required node, delete it, otherwise enque
            if temp.left:
                if temp.left == node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)
            #If right child is the required node, delete it, otherwise enque
            if temp.right:
                if temp.right == node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            
    #Left -> Root -> Right
    def inorderTraversal(self, node):
        if node == None:
            return
        self.inorderTraversal(node.left)
        print(node.data, end = " ")
        self.inorderTraversal(node.right)
    
    #Root -> Left -> Right
    def preorderTraversal(self, node):
        if node == None:
            return
        print(node.data, end = " ")
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)

    #Left -> Right -> Root
    def postorderTraversal(self, node):
        if node == None:
            return
        self.postorderTraversal(node.left)
        self.postorderTraversal(node.right)
        print(node.data, end = " ")

    #Traversal of nodes level by level
    def levelOrderTraversal(self):
        queue = []
        queue.append(self.root)
        while len(queue):
            temp = queue.pop(0)
            print(temp.data, end = " ")
            #Enque children of current node
            if temp.left:
                queue.append(temp.left)
            #Enque children of current node
            if temp.right: 
                queue.append(temp.right)

    def search(self, node, value):
        if node == None:
            return False
        if node.data == value:
            return True
        #Search in the left sub-tree
        if self.search(node.left, value):
            return True
        #Search in the right sub-tree
        elif self.search(node.right, value):
            return True
        #Return false if none of the above case
        return False

if __name__ == "__main__":
    tree = Tree()
    while (1):
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Search a value")
        print("4. Inorder Traversal")
        print("5. Pre-order Traversal")
        print("6. Post-order Traversal")
        print("7. Level-order Traversal")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            nodeValue = int(input("Enter the new node value: "))
            tree.insertion(nodeValue)
        elif choice == 2:
            nodeValue = int(input("Enter the node value to delete: "))
            tree.deletion(nodeValue)
        elif choice == 3:
            if tree.root == None:
                print("\nTree is empty!\n")
                continue
            searchValue = int(input("Enter the search value: "))
            if tree.search(tree.root, searchValue):
                print("\nValue is present!\n")
            else:
                print("\nValue is not present!\n")
        elif choice == 4:
            if tree.root == None:
                print("\nTree is empty!\n")
                continue
            print("\nInorder traversal of the tree:", end = " ")
            tree.inorderTraversal(tree.root)
            print("\n")
        elif choice == 5:
            if tree.root == None:
                print("\nTree is empty!\n")
                continue
            print("\nPre-order traversal of the tree:", end = " ")
            tree.preorderTraversal(tree.root)
            print("\n")
        elif choice == 6:
            if tree.root == None:
                print("\nTree is empty!\n")
                continue
            print("\nPost-order traversal of the tree:", end = " ")
            tree.postorderTraversal(tree.root)
            print("\n")
        elif choice == 7:
            if tree.root == None:
                print("\nTree is empty!\n")
                continue
            print("\nLevel-order traversal of the tree:", end = " ")
            tree.levelOrderTraversal()
            print("\n")
        else:
            print("Wrong choice!")