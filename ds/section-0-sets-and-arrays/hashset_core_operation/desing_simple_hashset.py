class MyHashSet:

    def __init__(self):
        self.hashset = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key] 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


myHashSet = MyHashSet()
myHashSet.add(1)      # set = [1]
myHashSet.add(2)      # set = [1, 2]
print(myHashSet.contains(1)) # return True
print(myHashSet.contains(3)) # return False, (not found)
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(2) # return True
myHashSet.remove(2)   # set = [1]
myHashSet.contains(2) # return False, (already removed)