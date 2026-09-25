
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def en_queue(self, value: int) -> bool:
        if self.isFull():
            return False

        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1

        return True

    def de_queue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def rear(self) -> int:
        if self.isEmpty():
            return -1

        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
