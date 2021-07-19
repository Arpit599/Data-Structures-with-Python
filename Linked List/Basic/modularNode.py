def modularNode(head, k):
    #function should return the modular Node
    
    # Corner cases
    if (k <= 0 or head == None):
        return None
    
    #if no such node is present then return -1
    maxNum = -1
    index = 1
    while head:
        if index % k == 0:
            maxNum = head.data
        head = head.next
        index += 1
        
    return maxNum

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        k = int(input())
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(modularNode(a.head,k))

