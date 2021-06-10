from collections import deque

#Function to reverse the queue.
def rev(q):
    #Using deque to append popped element from the queue at front of the deque 
    temp_queue = deque()
    while not q.empty():
        temp_queue.appendleft(q.get())
    #Then pop element from front of deque and append to the original queue
    while temp_queue:
        q.put(temp_queue.popleft())
    return q

#  Driver Code Starts
from queue import Queue
if __name__ == '__main__':
    n = int(input("Enter the queue size: "))
    a = list(map(int, input("Enter the queue: ").split()))
    q = Queue(maxsize = n+1)
    for j in a:
        #q.put() to push element to the queue
        q.put(j)
    q = rev(q)
    for i in range(0, n):
        #q.get() to pop element from the queue
        print(q.get(), end=" ")
