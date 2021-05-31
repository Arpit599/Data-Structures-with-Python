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

    def printList(self):
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
        print("5. Print list")
        print("6. Print number of nodes")

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
            cll.printList()
        elif(choice == 6):
            print("Number of nodes:", cll.nodeCount)
        else: 
            print("Wrong choice")

