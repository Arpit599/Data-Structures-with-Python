class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def printListReverse(self):
        temp = self.head 
        while(temp.next is not None):
            temp = temp.next
        while(temp is not None):
            print(temp.data, end=" ")
            temp = temp.prev

if __name__ == "__main__":
    dll = doubleLinkedList()
    while(True):
        print("1. Insert node at the front")
        print("2. Insert node after a node")
        print("3. Insert node before a node")
        print("4. Insert node at the end")
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            data = int(input("Enter the node value: "))
            dll.insertAtFront(data)
            dll.printList()
            print(end="\n")
            dll.printListReverse()
            print(end="\n")
        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        else: 
            print("Wrong choice")

