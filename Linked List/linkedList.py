class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    nodeCount = 0

    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.nodeCount += 1

    def insertAfter(self, nodeNum, data):
        if nodeNum > self.nodeCount:
            print("Not enough nodes!")
            return
        newNode = Node(data)
        temp = self.head
        for i in range(nodeNum - 1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode 

        self.nodeCount += 1
    
    def insertBefore(self, nodeNum, data):
        if nodeNum > self.nodeCount:
            print("Not enough nodes!")
            return
        
        newNode = Node(data)
        if nodeNum == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(nodeNum - 2):
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode 

        self.nodeCount += 1

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        self.nodeCount += 1

    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + " -> ", end="")
            temp = temp.next
        print("Null")

if __name__ == "__main__" :

    llist = LinkedList()

    while(True):
        print("1. Insert node at the front")
        print("2. Insert node after a node")
        print("3. Insert node before a node")
        print("4. Insert node at the end")
        print("5. Print list")
        print("6. Print number of nodes")

        choice = int(input("Enter your choice: "))
        if(choice == 1):
            data = int(input("Enter the node value: "))
            llist.insertAtFront(data)
        elif(choice == 2):
            nodeNumber = int(input("Enter the number of node after which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            llist.insertAfter(nodeNumber, nodeValue)
        elif(choice == 3):
            pass
            nodeNumber = int(input("Enter the number of node before which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            llist.insertBefore(nodeNumber, nodeValue)
        elif(choice == 4):
            data = int(input("Enter the node value: "))
            llist.insertAtEnd(data)
        elif(choice == 5):
            llist.printList()
        elif(choice == 6):
            print("Number of nodes:", llist.nodeCount)
        else: 
            print("Wrong choice")
