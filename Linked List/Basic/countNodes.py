#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # append at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next

class Solution:
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        count = 0
        temp = head_node
        while temp:
            temp = temp.next
            count += 1
        return count

#Driver Code Starts
if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for cases in range(t):
        n = int(input("Enter number of nodes: "))
        ll = LinkedList()
        nodes = list(map(int, input().strip().split())) #list containing nodes
        for x in nodes:
            node = Node(x) # create a new node
            ll.append(node)
        print("Number of nodes present:", Solution().getCount(ll.head))
