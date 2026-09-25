import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        self.values.append(val)
        self.hashmap[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        
        i = self.hashmap[val]
        last_val = self.values[-1]
        self.values[i] = last_val
        self.hashmap[last_val] = i
        self.values.pop()
        del self.hashmap[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.values)


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2)) # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.