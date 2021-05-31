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
        print("5. Print list")
        print("6. Print reversed list")
        print("7. Print number of nodes")

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
            dll.printList()
        elif(choice == 6):
            dll.printListReverse()
        elif(choice == 7):
            print("Number of nodes:",dll.nodeCount)
        else: 
            print("Wrong choice")
