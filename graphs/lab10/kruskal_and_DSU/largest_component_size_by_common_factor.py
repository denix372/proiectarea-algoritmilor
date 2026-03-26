from typing import List
from collections import Counter
from math import sqrt
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_val = max(nums)
        parent = list(range(max_val + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                parent[ra] = rb
    
        # 1) Connect each number to its factors
        for x in nums:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    union(x, i)
                    union(x, x // i)
        
        # 2) Count the sizes of components
        counts = Counter()
        for x in nums:
            root = find(x)
            counts[root] += 1
        return max(counts.values())

nums = [4,6,15,35]
print(Solution().largestComponentSize(nums))