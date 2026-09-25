
class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]


lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4