from typing import List
from collections import deque

class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        res.append(nums[queue[0]])

        for i in range(k, len(nums)):
            if queue[0] <= i - k:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            queue.append(i)
        
            res.append(nums[queue[0]])

        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))