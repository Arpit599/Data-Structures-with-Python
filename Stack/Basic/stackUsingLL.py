class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    #Function to push an integer into the stack.
    def push(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode

    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head == None:
            return -1
        #If there are is only one node left
        if self.tail == self.head:
            poppedItem = self.head.data
            self.head = None
            self.tail = None
            return poppedItem
        #If there are more than 2 nodes are left
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
            
        poppedItem = self.tail.data
        temp.next = None
        self.tail = temp
        return poppedItem

#  Driver Code Starts
if __name__ == '__main__':
    s = Stack()
    q1 = list(map(int, input().split()))
    i = 0
    while(i < len(q1)):
        if(q1[i] == 1):
            s.push(q1[i + 1])
            i = i + 2
        elif(q1[i] == 2):
            print(s.pop(), end=" ")
            i = i + 1
        elif(s.isEmpty()):
           print(-1)