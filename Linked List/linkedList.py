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
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        self.nodeCount += 1

    def deleteHead(self):
        if self.head == None:
            print("Can't delete node from empty list")
            return

        self.head = self.head.next
        self.nodeCount -= 1
    
    def deleteAfter(self, nodeNum):
        if nodeNum >= self.nodeCount:
            print("Not enough nodes!")
            return
        
        temp = self.head
        for i in range(nodeNum - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.nodeCount -= 1

    def deleteBefore(self, nodeNum):
        if nodeNum == 1:
            print("Invalid operation!...No nodes before head to delete")
            return
        elif nodeNum > self.nodeCount:
            print("Not enough nodes!")
            return
        elif nodeNum == 2:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(nodeNum - 3):
                temp = temp.next
            temp.next = temp.next.next
        self.nodeCount -= 1
    
    def deleteEnd(self):
        if self.head == None:
            print("Can't delete node from empty list")
            return 

        if self.head.next == None:
            self.head = None
        else:
            temp = self.head 
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None

        self.nodeCount -= 1

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
        print("5. Delete node at the front")
        print("6. Delete node after a node")
        print("7. Delete node before a node")
        print("8. Delete node at the end")
        print("9. Print list")
        print("10. Print number of nodes")

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
            llist.deleteHead()
        elif(choice == 6):
            nodeNumber = int(input("Enter the number of node after which you want to delete: "))
            llist.deleteAfter(nodeNumber)
        elif(choice == 7):
            nodeNumber = int(input("Enter the number of node after which you want to delete: "))
            llist.deleteBefore(nodeNumber)
        elif(choice == 8):
            llist.deleteEnd()
        elif(choice == 9):
            llist.printList()
        elif(choice == 10):
            print("Number of nodes:", llist.nodeCount)
        else: 
            print("Wrong choice")
