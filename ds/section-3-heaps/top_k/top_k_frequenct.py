from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        q = []
        for x in nums:
            d[x] += 1
        for x, v in d.items():
            heappush(q, (-v, x))
        res = []
        for _ in range(k):
            _, x = heappop(q)
            res.append(x)
        return res

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))