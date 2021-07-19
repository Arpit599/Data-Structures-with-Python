# Function should return sum of last n nodes 
def sumOfLastN_Nodes(head,n):
    print(head)
    sum = 0
    stack = []
    
    #Push all the nodes in the stack
    while head :
        stack.append(head.data)
        head = head.next
    
    #Pop the 'n' nodes from above and do the sum    
    while n:
        sum += stack.pop()
        n = n - 1
    print(head)
    return sum

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Creates a new node with given value and appends it at the end of the linked list
    def insert(self, new_value):
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
    t=int(input())
    for cases in range(t):
        n, nth_node = map(int, input("Enter the number of nodes and the nth node: ").strip().split())
        a = LinkedList() # Create a new linked list 'a'.
        nodes_a = list(map(int, input("Enter the list: ").strip().split()))
        for x in nodes_a:
            a.insert(x)  # Add to the end of the list
        print("The sum is", sumOfLastN_Nodes(a.head, nth_node))