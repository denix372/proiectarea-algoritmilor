from typing import List
from heapq import heappop, heappush

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        q = []
        for y in arr:
            heappush(q, (abs(y - x), y))

        for _ in range(k):
            _, y = heappop(q)
            res.append(y)
        return sorted(res)

arr = [1,2,3,4,5]
k = 4
x = 3
print(Solution().findClosestElements(arr, k, x))