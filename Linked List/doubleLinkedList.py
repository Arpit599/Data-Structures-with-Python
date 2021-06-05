class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    nodeCount = 0

    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.head

        #Checking if newNode is the first node in the list or not
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        self.nodeCount += 1

    def insertAtEnd(self, data):
        newNode = Node(data)

        #Checking if newNode is the first node in the list or not
        if self.head is not None:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
        else:
            self.head = newNode
        self.nodeCount += 1
    
    def insertAfter(self, prev, data):
        if prev is None:
            return
        
        newNode = Node(data)
        newNode.next = prev.next
        newNode.prev = prev

        #If element is not to be inserted in the end
        if prev.next is not None:
            prev.next.prev = newNode

        prev.next = newNode
        self.nodeCount += 1

    def insertBefore(self, prev, data):
        if prev is None:
            return
        
        newNode = Node(data)
        newNode.next = prev
        newNode.prev = prev.prev

        #If element is to be inserted in the beginning
        if prev is self.head:
            self.head = newNode
        else:
            prev.prev.next = newNode
        
        prev.prev = newNode
        self.nodeCount += 1

    def findNode(self, nodeNum):
        temp = self.head
        if nodeNum > self.nodeCount:
            print("Not enough nodes in the list!")
            return None

        for i in range(nodeNum - 1):
            temp = temp.next
        return temp

    def deleteHead(self):
        if self.head == None:
            print("Empty list!")
            return
        #If head node is the last node left
        elif self.head.next == None:
            print("Last node to delete")
            self.head = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        
        self.nodeCount -= 1
    
    def deleteEnd(self):
        if self.head == None:
            print("Empty list!")
            return 
        #If only head node is left
        elif self.head.next == None:
            print("Last node to delete")
            self.head = None
        else:
            temp = self.head
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
        
        self.nodeCount -= 1
    
    def deleteAfter(self, givenNode):
        #If this is the last node in the list then invalid operation
        if givenNode.next == None:
            print("This is the last node!")
            return
        #If only two nodes are remaining and second node is to be deleted
        elif self.nodeCount == 2:
            self.head.next = None
        else:
            #If this is not the last second node in the list
            if givenNode.next.next != None:
                givenNode.next.next.prev = givenNode
            givenNode.next = givenNode.next.next
        
        self.nodeCount -= 1

    def deleteBefore(self, givenNode):
        #If this is the head node in the list then invalid operation
        if givenNode.prev == None:
            print("This is the head node!")
            return
        #If only two nodes are remaining and first node is to be deleted
        elif self.nodeCount == 2:
            self.head = givenNode
            givenNode.prev = None
        else:
            #If this is the second node change head
            if givenNode.prev.prev == None:
                self.head = givenNode
            else:
                givenNode.prev.prev.next = givenNode
            givenNode.prev = givenNode.prev.prev
        
        self.nodeCount -= 1

    def printList(self):
        if self.head is None:
            print("Empty list! Nothing to print")
            return

        temp = self.head 
        while(temp):
            print(str(temp.data) + " <-> ", end="")
            temp = temp.next
        print("Null")

    def printListReverse(self):
        if self.head is None:
            print("Empty list! Nothing to print")
            return

        temp = self.head 
        while(temp.next is not None):
            temp = temp.next
        while(temp is not None):
            print(str(temp.data) + " <-> ", end="")
            temp = temp.prev
        print("Null")

if __name__ == "__main__":
    dll = doubleLinkedList()
    while(True):
        print("1. Insert node at the front")
        print("2. Insert node after a node")
        print("3. Insert node before a node")
        print("4. Insert node at the end")
        print("5. Delete node at the front")
        print("6. Delete node after a node")
        print("7. Delete node before a node")
        print("8. Delete node at the end")
        print("9. Print list")
        print("10. Print reversed list")
        print("11. Print number of nodes")

        choice = int(input("Enter your choice: "))
        if(choice == 1):
            data = int(input("Enter the node value: "))
            dll.insertAtFront(data)
        elif(choice == 2):
            nodeNumber = int(input("Enter the number of node after which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            node = dll.findNode(nodeNumber)
            dll.insertAfter(node, nodeValue)
        elif(choice == 3):
            nodeNumber = int(input("Enter the number of node before which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            node = dll.findNode(nodeNumber)
            dll.insertBefore(node, nodeValue)
        elif(choice == 4):
            data = int(input("Enter the node value: "))
            dll.insertAtEnd(data)
        elif(choice == 5):
            dll.deleteHead()
        elif(choice == 6):
            nodeNumber = int(input("Enter number of the node after which you want to delete: "))
            node = dll.findNode(nodeNumber)
            if node == None:
                print("Invalid operation")
                continue
            dll.deleteAfter(node)
        elif(choice == 7):
            nodeNumber = int(input("Enter number of the node before which you want to delete: "))
            node = dll.findNode(nodeNumber)
            if node == None:
                print("Invalid operation")
                continue
            dll.deleteBefore(node)
        elif(choice == 8):
            dll.deleteEnd()
        elif(choice == 9):
            dll.printList()
        elif(choice == 10):
            dll.printListReverse()
        elif(choice == 11):
            print("Number of nodes:",dll.nodeCount)
        else: 
            print("Wrong choice")
