class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularList:
    nodeCount = 0

    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = newNode
        else:
            newNode.next = self.head
            temp = self.head
            while(temp.next is not self.head):
                temp = temp.next
            temp.next = newNode
        
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
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
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
        
        if self.head is not None:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
        else:
            newNode.next = newNode
            self.head = newNode
        self.nodeCount += 1

    def deleteHead(self):
        if self.head == None:
            print("Empty list!")
            return
        elif self.head.next == self.head:
            self.head = None
            print("Last node to delete")
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head

        self.nodeCount -= 1

    def deleteEnd(self):
        if self.head == None:
            print("Empty list!")
            return
        elif self.head.next == self.head:
            self.head = None
            print("Last node to delete")
        else:
            temp = self.head
            while(temp.next.next != self.head):
                temp = temp.next
            temp.next = self.head

        self.nodeCount -= 1

    def deleteAfter(self, nodeNum):
        if nodeNum > self.nodeCount:
            print("Not enough nodes!")
            return
            
        #Deleting node is nodeCount = 1 and nodeNum = 0 or 1, then delete no node
        elif self.nodeCount == 1 and (nodeNum == 1 or nodeNum == 0):
            print("Only one node in the list")

        #Deleting head node and making new head if nodeNum = 2 and nodeCount = 2 
        elif nodeNum == 2 and self.nodeCount == 2:
            self.head = self.head.next
            self.head.next = self.head

        #If node to be deleted is the head but nodeCount > 2
        elif nodeNum == self.nodeCount:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

        #Deleting node elsewhere
        else:
            temp = self.head
            for i in range(nodeNum - 1):
                temp = temp.next
            temp.next = temp.next.next

        self.nodeCount -= 1

    def deleteBefore(self, nodeNum):
        if nodeNum > self.nodeCount:
            print("Not enough nodes!")
            return

        #Deleting node before head node
        elif nodeNum == 1:
            #If there is only one node left, the operation is invalid
            if self.nodeCount == 1:
                print("Invalid Operation, Only one node present")
                return
            #Else delete the node
            temp = self.head 
            while(temp.next.next != self.head):
                temp = temp.next
            temp.next = self.head

        #Deleting node before nodeNum = 2 
        elif nodeNum == 2:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

        #Deleting node elsewhere
        else:
            temp = self.head
            for i in range(nodeNum - 3):
                temp = temp.next
            temp.next = temp.next.next

        self.nodeCount -= 1
    
    def printList(self):
        if self.head == None:
            print("Empty list!")
            return
        temp = self.head
        while(1):
            print(str(temp.data) + " -> ", end="")
            temp = temp.next
            if(temp == self.head):
                print("HEAD")
                break

if __name__ == "__main__":
    cll = circularList()
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
            cll.insertAtFront(data)
        elif(choice == 2):
            nodeNumber = int(input("Enter the number of node after which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            cll.insertAfter(nodeNumber, nodeValue)
        elif(choice == 3):
            nodeNumber = int(input("Enter the number of node before which you want to enter the new node: "))
            nodeValue = int(input("Enter the value of the new node: "))
            cll.insertBefore(nodeNumber, nodeValue)
        elif(choice == 4):
            data = int(input("Enter the node value: "))
            cll.insertAtEnd(data)
        elif(choice == 5):
            cll.deleteHead()
        elif(choice == 6):
            nodeNumber = int(input("Enter the number of node after which you want to delete: "))
            cll.deleteAfter(nodeNumber)
        elif(choice == 7):
            nodeNumber = int(input("Enter the number of node before which you want to delete: "))
            cll.deleteBefore(nodeNumber)
        elif(choice == 8):
            cll.deleteEnd()
        elif(choice == 9):
            cll.printList()
        elif(choice == 10):
            print("Number of nodes:", cll.nodeCount)
        else: 
            print("Wrong choice")

