
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.head = (self.head - 1) % self.capacity 
        self.queue[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
    
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


myCircularDeque =MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  # return True
print(myCircularDeque.insertLast(2))  # return True
print(myCircularDeque.insertFront(3)) # return True
print(myCircularDeque.insertFront(4)) # return False, the queue is full.
print(myCircularDeque.getRear())      # return 2
print(myCircularDeque.isFull())       # return True
print(myCircularDeque.deleteLast())   # return True
print(myCircularDeque.insertFront(4)) # return True
print(myCircularDeque.getFront())     # return 4