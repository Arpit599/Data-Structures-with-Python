class Solution: 
    def deleteAlt(self, head):
        if head == None:
            return
        node = head.next
        if node == None:
            return
        head.next = node.next
        self.deleteAlt(head.next)

class Node: 
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None  

#  Driver Code Starts
if __name__=='__main__':
    t = int(input("Enter number of test cases: "))
    for i in range(t):
        
        n = int(input("Enter number of nodes: "))
        arr = list(map(int, input("Enter the nodes: ").strip().split()))
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        
        ob = Solution()
        ob.deleteAlt(head)
        
        while head is not None:
            print(head.data, end = " ")
            head = head.next
        print()   
        