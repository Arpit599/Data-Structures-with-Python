class MyStack:
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
        
    def isEmpty():
        if len(self.arr) == 0:
            return -1

#  Driver Code Starts
if __name__=='__main__':
    s = MyStack()
    q1 = list(map(int,input("Enter the array: ").split()))
    i = 0
    while(i < len(q1)):
        if(q1[i] == 1):
            s.push(q1[i + 1])
            i = i + 2
        elif(q1[i] == 2):
            print(s.pop(), end = " ")
            i = i + 1
        elif(s.isEmpty()):
            print(-1)
            i = i + 1
