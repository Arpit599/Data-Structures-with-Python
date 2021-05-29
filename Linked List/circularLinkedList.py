class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularList:
    def __init__(self):
        self.head = None
    
    def insertHead(self, data):
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

    def insertAfter(self, prev, data):
        newNode = Node(data)
        if prev.next == self.head:
            self.push(data)
            return
        else:
            newNode.next = prev.next
            prev.next = newNode

    def push(self, data):
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
            

    def printList(self):
        temp = self.head
        while(1):
            print(temp.data, end=" ")
            temp = temp.next
            if(temp == self.head):
                break

if __name__ == "__main__":
    cll = circularList()

    # cll.insertHead(6)
    cll.push(1)
    cll.insertAfter(cll.head, 2)
    cll.insertAfter(cll.head, 3)
    cll.insertAfter(cll.head.next, 4)
    cll.insertAfter(cll.head.next.next.next, 69)
    # cll.push(3)
    # cll.push(4)
    # cll.insertHead(5)

    cll.printList()
