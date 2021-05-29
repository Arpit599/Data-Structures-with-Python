class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, prev, data):
        if prev is None:
            print("Please enter a valid previous node")
        newNode = Node(data)
        newNode.next = prev.next
        prev.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__" :

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    # llist.insertAtFront(4)
    # llist.insertAtEnd(5)
    # llist.insertAtFront(6)
    # llist.insertAtEnd(7)
    llist.insertAfter(llist.head.next.next, 4)
    llist.printList()
