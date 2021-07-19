import sys
 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def countSubtrees(root, count=0):
    if root is None:
        return -sys.maxsize, count
 
    if root.left is None and root.right is None:
        count = count + 1
        return root.data, count
 
    left, count = countSubtrees(root.left, count)
    right, count = countSubtrees(root.right, count)
 
    if ((left == -sys.maxsize and right == root.data) or
            (right == -sys.maxsize and left == root.data) or
            (left == right and left == root.data)):
        count = count + 1
        return root.data, count
 
    return -sys.maxsize, count
 
 
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(4)
    root.right.left.left = Node(5)
    root.right.left.right = Node(5)
    root.right.right.right = Node(7)
    
    if(countSubtrees(root)[1] == 0):
        print(-1)
    else:
        print(countSubtrees(root)[1])
 