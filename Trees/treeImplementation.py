class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insertion(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
            return
        queue = []
        queue.append(self.root)
        temp = queue[0]
        while len(queue):
            temp = queue.pop(0)

            if not temp.left:
                temp.left = newNode
                break
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = newNode
                break
            else:
                queue.append(temp.right)

    def deletion(self, nodeValue):
        if self.root == None:
            print("\nTree is empty!\n")
            return
        
        if self.root.left == None and self.root.right == None:
            if self.root.data == nodeValue:
                self.root = None
                return
            else:
                print("\nValue not present!\n")
                return

        queue = []
        queue.append(self.root)
        foundNode = None
        temp = None
        while len(queue):
            temp = queue.pop(0)

            if temp.left:
                if temp.left.data == nodeValue:
                    foundNode = temp.left
                queue.append(temp.left)

            if temp.right:
                if temp.right.data == nodeValue:
                    foundNode = temp.right
                queue.append(temp.right)
        
        if foundNode == None:
            print("\nValue not present\n")
            return
            
        foundNode.data = temp.data
        self.deleteNode(temp)
        
    def deleteNode(self, node):
        queue = []
        queue.append(self.root)
        while len(queue):
            temp = queue.pop(0)

            if node == self.root:
                self.root = None
                return

            if temp.left:
                if temp.left == node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)

            if temp.right:
                if temp.right == node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            
    def inorderTraversal(self, node):
        if node == None:
            return
        self.inorderTraversal(node.left)
        print(node.data, end = " ")
        self.inorderTraversal(node.right)

if __name__ == "__main__":
    tree = Tree()
    while (1):
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Inorder Traversal")
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
            print("\nInorder traversal of the tree:", end = " ")
            tree.inorderTraversal(tree.root)
            print("\n")
        else:
            print("Wrong choice!")
    # tree = Tree()
    # tree.root = Node(10)
    # tree.root.left = Node(11)
    # tree.root.left.left = Node(7)
    # tree.root.right = Node(9)
    # tree.root.right.left = Node(15)
    # tree.root.right.right = Node(8)
    # tree.inorderTraversal(tree.root)