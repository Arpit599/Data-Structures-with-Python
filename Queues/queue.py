class Queue:
    def __init__(self, capacity):
        self.front = self. size = 0
        self.capacity = capacity
        self.rear = capacity - 1
        self.q = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enque(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.size += 1
        return True

    def deque(self):
        if self.isEmpty():
            return False
        print("Element dequed", self.q[self.front])
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
        
    def q_front(self):
        if self.isEmpty():
            print("Queue is empty!") 
        else:
            print("Front of the queue", self.q[self.front])
        return

    def q_rear(self):
        if self.isEmpty():
            print("Queue is full!") 
        else:
            print("Rear of the queue", self.q[self.rear])
        return


if __name__ == "__main__":
    capacity = int(input("Enter the size of the queue: "))
    queue = Queue(capacity)
    while(1):
        print("1.Enque")
        print("2.Deque")
        print("3.Get front")
        print("4.Get rear")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            ele = int(input("Enter the element: "))
            if queue.enque(ele):
                print("Element enqueued")
            else:
                 print("Queue already full!")
        elif choice == 2:
            if not queue.deque():
                print("Queue already empty!")
        elif choice == 3:
            queue.q_front()
        elif choice == 4:
            queue.q_rear()
        else:
            print("Wrong choice!")
        print(queue.q)

    