def isLengthEvenOrOdd(head):
    # Code here
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
        
    if count % 2 == 0:
        return 1
    else:
        return 0

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
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


#  Driver Code Starts
if __name__=='__main__':
    t = int(input("Enter the number of test cases: "))
    for i in range(t):
        n = int(input("Enter the number of nodes: "))
        arr = list(map(int, input("Enter the linked list: ").strip().split()))
        head = createList(arr, n)
        if(isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')