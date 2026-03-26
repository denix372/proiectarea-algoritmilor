from typing import List
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        for _ in range(len(nums) - k):
            heappop(nums)

        return heappop(nums)

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
