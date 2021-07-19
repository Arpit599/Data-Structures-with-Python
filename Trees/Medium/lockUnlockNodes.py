import math

class Node:
    def __init__(self, data):
        self.data = data
        self.numLockedDesc = 0
        self.isLocked = False
        self.uid = None
        self.parent = None
        self.child = []

def Lock(X, uid):
    #Get the address of the node to be locked from the dictionary
    temp = nodeAddress[X]
    # print(nodeAddress)
    # for i in range(len(nodeAddress)):
    #     print(nodeAddress[i].parent)
    # print(temp.data, temp)
    # print(X == "china")
    # print(nodeAddress["china"])
    # print(nodeAddress[X])
    # print(nodeAddress.keys())
    if temp.isLocked or temp.numLockedDesc != 0:
        return False
    
    # print(temp.data, temp.parent)

    if checkAncestors(temp.parent):
        temp.isLocked = True
        temp.uid = uid
        lockedNodesArr.append(temp)
        return True

    return False

def checkAncestors(node):
    if node == None:
        return True
    
    if node.isLocked:
        return False
    
    #Increase locked descendants count in parent nodes
    if checkAncestors(node.parent):
        node.numLockedDesc += 1
        return True
    return False

def Unlock(X, uid):
    #Get the address of the node to be locked from the dictionary
    temp = nodeAddress[X]

    #If the node is not locked or owner is someone else
    if not temp.isLocked or temp.uid != uid:
        return False

    #If everything is fine, update the node
    temp.uid = None
    temp = temp.parent
    temp.isLocked = False
    
    #Decrease locked descendants count in parent nodes
    while temp.parent:
        temp.numLockedDesc -= 1
        temp = temp.parent
    
    return True

def Upgrade(X, uid):
    #First append the locked nodes with same uid as passed above in locked desc arr
    for i in range(len(lockedNodesArr)):
        # print("Inside lockednodes print", lockedNodesArr[i].data)
        if lockedNodesArr[i].uid == uid:
            lockedDescArr.append(lockedNodesArr[i])

    node = nodeAddress[X]

    #If current node's locked desc count is greater than locked desc arr size return false
    if node.numLockedDesc > len(lockedDescArr):
        return False

    #First unlock all locked nodes
    for i in range(len(lockedDescArr)):
        # print("Inside lockeddesc print", lockedDescArr[i].data)
        Unlock(lockedDescArr[i].data, uid)

    #If desc arrays are not empty
    if len(lockedNodesArr) != 0 and len(lockedDescArr) != 0:
        if node.numLockedDesc == 0:
            node.isLocked = True
            node.uid = uid
            lockedDescArr.clear()
            return True
    
    #If all the above conditions are not met return false and lock again the unlocked nodes
    for i in range(len(lockedDescArr)):
        Lock(lockedDescArr[i].data, uid)

    #Clear the desc arr
    lockedDescArr.clear()
    
    return False

#To store the nodes value
nodesArr = []
#To store the locked nodes address
lockedNodesArr = []
#To store the locked descendant nodes address
lockedDescArr = []
#Dictionary to store the node address of each input node
nodeAddress = {}

if __name__ == "__main__":
    nodeCount = int(input("Enter the number of nodes: "))
    childCount = int(input("Enter the number of children: "))
    queryCount = int(input("Enter the number of queries: "))
    print("Enter the nodes now!")
    nodesArr = [None] * nodeCount
    for i in range(nodeCount):
        nodesArr[i] = input()
        newNode = Node(nodesArr[i])
        nodeAddress[nodesArr[i]] = newNode
        if i != 0:
            # print("Parent value", nodesArr[math.floor((i - 1) / childCount)])
            # print("Parent index", math.floor((i - 1) / childCount))
            # print("Parent address", nodeAddress[nodesArr[math.floor((i - 1) / childCount)]])
            newNode.parent = nodeAddress[nodesArr[math.floor((i - 1) / childCount)]]
            # print("New node data and parent address", newNode.data, newNode.parent)
        # else:
            # print("Parent value", nodesArr[0])
            # print("Parent address", nodeAddress[nodesArr[0]])
            # print("New node data and parent address", newNode.data, newNode.parent)

    for i in range(queryCount):
        operation, nodeVal, uid = input().split()
        operation = int(operation)
        uid = int(uid)

        if operation == 1:
            print(Lock(nodeVal, uid))
        elif operation == 2:
            print(Unlock(nodeVal, uid))
        elif operation == 3:
            print(Upgrade(nodeVal, uid))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.numLockedDesc = 0
#         self.isLocked = False
#         self.uid = None
#         self.parent = None
#         self.child = []

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insertion(self, root, newNode):
        
#         if root == None:
#             self.root = newNode
#             # print("Check")
#             return True

#         # if len(root.child) == 0:
#         #     root.child.append(newNode)
#         #     print("inside first node insertion of child")
#         #     return True

#         # for i in range(len(root.child)):
#         #     if len(root.child) != childCount:
#         #         root.child.append(newNode)
#         #         root.child[len(root.child) - 1].parent = root
#         #         print("Inside if")
#         #         return True
#         #     else:
#         #         print("Inside else")
#         #         if self.insertion(root.child[i], newNode):
#         #             break
#         queue = []
#         queue.append(root)
#         temp = queue[0]
#         while len(queue):
#             temp = queue.pop()
#             if len(temp.child) != childCount:
#                 temp.child.append(newNode)
#                 newNode.parent = temp
#                 # print("Inside if condition")
#                 break
#             else:
#                 for i in range(len(temp.child)):
#                     queue.append(temp.child[i])
#                     # print("Inside else condition")

# def Lock(X, uid, root):
#     temp = nodeAddress[X]
#     print(nodeAddress)
#     # print(temp)
#     # print(X == "china")
#     # print(nodeAddress["china"])
#     # print(nodeAddress[X])
#     # print(nodeAddress.keys())
#     if temp.isLocked or temp.numLockedDesc != 0:
#         return False

#     if checkAncestors(temp.parent, root):
#         temp.isLocked = True
#         temp.uid = uid
#         lockedNodesArr.append(temp)
#         return True

#     return False

# def checkAncestors(node, root):
#     if node == root and not node.isLocked:
#         node.numLockedDesc += 1
#         return True
    
#     if node.isLocked:
#         return False
    
#     if checkAncestors(node.parent, root):
#         node.numLockedDesc += 1
#         return True
    
#     return False

# def Unlock(X, uid):
#     temp = nodeAddress[X]
#     if not temp.isLocked or temp.uid != uid:
#         return False

#     temp.uid = None
#     temp = temp.parent
#     temp.isLocked = False
    
#     while temp.parent:
#         temp.numLockedDesc -= 1
#         temp = temp.parent
    
#     return True

# def Upgrade(X, uid):
#     for i in range(len(lockedNodesArr)):
#         print("Inside lockednodes print", lockedNodesArr[i].data)
#         if lockedNodesArr[i].uid == uid:
#             lockedDescArr.append(lockedNodesArr[i])


#     for i in range(len(lockedDescArr)):
#         print("Inside lockeddesc print", lockedDescArr[i].data)
#         Unlock(lockedDescArr[i].data, uid)

#     node = nodeAddress[X]

#     if node.numLockedDesc == 0:
#         node.isLocked = True
#         node.uid = uid
#         return True
    
#     for i in range(len(lockedDescArr)):
#         Lock(lockedDescArr[i].data, uid)
    
#     return False

# nodesArr = []
# lockedNodesArr = []
# lockedDescArr = []
# nodeAddress = {}

# if __name__ == "__main__":
#     nodeCount = int(input("Enter the number of nodes: "))
#     childCount = int(input("Enter the number of children: "))
#     queryCount = int(input("Enter the number of queries: "))
#     print("Enter the nodes now!")
#     treeObj = Tree()
#     nodesArr = [None] * nodeCount
#     for i in range(nodeCount):
#         nodesArr[i] = input()
#         newNode = Node(nodesArr[i])
#         nodeAddress[nodesArr[i]] = newNode
#         treeObj.insertion(treeObj.root, newNode)
    
#     for i in range(queryCount):
#         operation, nodeVal, uid = input().split()
#         operation = int(operation)
#         uid = int(uid)

#         if operation == 1:
#             print(Lock(nodeVal, uid, treeObj.root))
#         elif operation == 2:
#             print(Unlock(nodeVal, uid))
#         elif operation == 3:
#             print(Upgrade(nodeVal, uid))

# # Write your code here
# import math

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.numLockedDesc = 0
#         self.isLocked = False
#         self.uid = None
#         self.parent = None
#         self.child = []

# def Lock(X, uid):
#     temp = nodeAddress[X]

#     if temp.isLocked or temp.numLockedDesc != 0:
#         return False

#     if not canLock(temp):
#         return False
    
#     parentNode = temp.parent

#     while parentNode:
#         parentNode.numLockedDesc += 1
#         parentNode = parentNode.parent

#     temp.isLocked = True
#     temp.uid = uid
#     lockedNodesArr.append(temp)
#     return True

# def canLock(node):   
#     parentNode = node.parent
#     while parentNode:
#         if parentNode.isLocked:
#             return False
#         parentNode = parentNode.parent
#     return True

# def Unlock(X, uid):
#     temp = nodeAddress[X]

#     if not temp.isLocked:
#         return False
    
#     if temp.uid != uid:
#         return False
    
#     temp.uid = None
#     temp.isLocked = False
#     parentNode = temp.parent

#     while parentNode:
#         parentNode.numLockedDesc -= 1
#         parentNode = parentNode.parent

#     return True

# def Upgrade(X, uid):

#     node = nodeAddress[X]

#     if node.isLocked or node.numLockedDesc == 0:
#         return False

#     for i in range(len(lockedNodesArr)):
#         if lockedNodesArr[i].uid == uid:
#             if node.numLockedDesc == 0:
#                 break
#             prevCount = node.numLockedDesc
#             Unlock(lockedNodesArr[i].data, uid)
#             if node.numLockedDesc < prevCount:
#                 lockedDescArr.append(lockedNodesArr[i])
#             else:
#                 Lock(lockedNodesArr[i].data, uid)

#     if node.numLockedDesc == 0:
#         node.isLocked = True
#         node.uid = uid
#         lockedDescArr.clear()
#         return True

#     lockedDescArr.clear()

#     return False

# nodesArr = []
# lockedNodesArr = []
# lockedDescArr = []
# nodeAddress = {}

# if __name__ == "__main__":
#     nodeCount = int(input())
#     childCount = int(input())
#     queryCount = int(input())
#     nodesArr = [None] * nodeCount

#     for i in range(nodeCount):
#         nodesArr[i] = input()
#         newNode = Node(nodesArr[i])
#         nodeAddress[nodesArr[i]] = newNode
    
#         if i != 0:
#             newNode.parent = nodeAddress[nodesArr[math.floor((i - 1)/childCount)]]
    
#     for i in range(queryCount):
#         operation, nodeVal, uid = input().split()
#         operation = int(operation)
#         uid = int(uid)

#         if operation == 1:
#             if Lock(nodeVal, uid):
#                 print("true")
#             else:
#                 print("false")
#         elif operation == 2:
#             if Unlock(nodeVal, uid):
#                 print("true")
#             else:
#                 print("false")
#         elif operation == 3:
#             if Upgrade(nodeVal, uid):
#                 print("true")
#             else:
#                 print("false")
    




