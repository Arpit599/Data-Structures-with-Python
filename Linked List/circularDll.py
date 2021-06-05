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
            newNode.prev = self.head.prev
            self.head.prev.next = newNode
            self.head.prev = newNode
        else:
            newNode.next = newNode
            newNode.prev = newNode

        self.head = newNode
        self.nodeCount += 1

    def insertAtEnd(self, data):
        newNode = Node(data)

        #Checking if newNode is the first node in the list or not
        if self.head is not None:
            newNode.next = self.head
            newNode.prev = self.head.prev
            self.head.prev.next = newNode
            self.head.prev = newNode
        else:
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode
        self.nodeCount += 1
    
    def insertAfter(self, prev, data):
        if prev is None:
            return
        
        newNode = Node(data)
        newNode.next = prev.next
        newNode.prev = prev

        #If element is not to be inserted in the end
        prev.next.prev = newNode

        prev.next = newNode
        self.nodeCount += 1

    def insertBefore(self, prev, data):
        if prev is None:
            return
        
        newNode = Node(data)
        newNode.next = prev
        newNode.prev = prev.prev 
        prev.prev.next = newNode
        prev.prev = newNode
        
        #If element is to be inserted in the beginning
        if prev is self.head:
            self.head = newNode
        self.nodeCount += 1

    def deleteHead(self):
        #If list is empty, return 
        if self.nodeCount == 0:
            print("List is empty!")
            return
        #If there is single node in the list
        elif self.nodeCount == 1:
            self.head.next = None
            self.head.prev = None
            self.head = None
        #If there are more than one nodes in the list
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

        self.nodeCount -= 1
        
    def deleteEnd(self):
        #If list is empty, return 
        if self.nodeCount == 0:
            print("List is empty!")
            return
        #If there is single node in the list
        elif self.nodeCount == 1:
            self.head.next = None
            self.head.prev = None
            self.head = None
        #If there are more than one nodes in the list
        else:
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
        
        self.nodeCount -= 1

    def deleteAfter(self, givenNode):
        if self.nodeCount == 1:
            print("Last node! Invalid operation")
            return
        #If givenNode is last node, the next node is head node, so delete head node
        elif givenNode.next == self.head:
            givenNode.next = self.head.next
            self.head.next.prev = givenNode
            self.head = self.head.next
        #For number of nodes greater than 3
        else:
            givenNode.next.next.prev = givenNode
            givenNode.next = givenNode.next.next

        self.nodeCount -= 1       

    def deleteBefore(self, givenNode):
        if self.nodeCount == 1:
            print("Last node! Invalid operation")
            return
        #If givenNode is first node, the previous node is to be delete
        elif givenNode == self.head:
            givenNode.prev.prev.next = self.head
            self.head.prev = givenNode.prev.prev
        #For number of nodes greater than 3 or if the second node is the given node then change the head
        else:
            #If givenNode is second node, then delete the head node
            if givenNode.prev == self.head:
                self.head = self.head.next
            givenNode.prev.prev.next = givenNode
            givenNode.prev = givenNode.prev.prev

        self.nodeCount -= 1

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
        #Printing the head first and incrementing the pointer otherwise loop will not run
        print(str(temp.data) + " <-> ", end="")
        temp = temp.next

        while(temp != self.head):
            print(str(temp.data) + " <-> ", end="")
            temp = temp.next
        print("Head")

    def printListReverse(self):
        if self.head is None:
            print("Empty list! Nothing to print")
            return

        temp = self.head.prev 
        while(temp != self.head):
            print(str(temp.data) + " <-> ", end="")
            temp = temp.prev

        #To print the head element as it gets skipped in the loop above
        print(str(temp.data) + " <-> ", end="")
        print("Head")

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
            print("Number of nodes:", dll.nodeCount)
        else: 
            print("Wrong choice")
