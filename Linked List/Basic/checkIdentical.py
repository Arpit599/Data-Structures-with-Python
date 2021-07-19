#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    while(head1 and head2):
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    
    return (head1 == None and head2 == None)

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

#  Driver Code Starts
if __name__=='__main__':
    t = int(input("Enter the number of test cases: "))
    for i in range(t):
        n = int(input("Enter the number of nodes in list1: "))
        arr = list(map(int, input("Enter the list1: ").strip().split()))
        head1 = createList(arr, n)
        n = int(input("Enter the number of nodes in list2: "))
        arr = list(map(int, input("Enter the list2: ").strip().split()))
        head2 = createList(arr, n)
        if(areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')