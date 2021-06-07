import math

def fractionalNodes(head,k):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        index = int(math.ceil(count/k))
        
        for i in range(index - 1):
            head = head.next
        return head
        
class Node:
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

# Linked List class
class LinkedList: 
    # Function to initialize the Linked List object 
    def __init__(self):  
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
                
    def display(self,node):
        while(node is not None):
            print(node.data,end=" ")
            node=node.next

#  Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        for i in range(0, len(arr)):
            lis.insert(arr[i])
        ans = fractionalNodes(lis.head, k)
        print(ans.data)