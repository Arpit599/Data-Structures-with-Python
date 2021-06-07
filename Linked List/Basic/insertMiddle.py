#Function to insert a node in the middle of the linked list.
def insertInMid(head,node):
    nodeCount = 0
    temp = head
    while temp:
        nodeCount += 1
        temp = temp.next
    
    mid = 0
    if nodeCount % 2 == 0:
        mid = int(nodeCount/2)
    else:
        mid = int(nodeCount/2) + 1
    # print(mid)
    midNode = head
    for i in range(mid-1):
        midNode = midNode.next
    
    node.next = midNode.next
    midNode.next = node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the 
    #linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return
    
    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(' ')
#  Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        mid_elem = int(input())
        insertInMid(a.head, Node(mid_elem))
        a.printList()