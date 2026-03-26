from math import ceil
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1 
        right = max(nums)
        
        while left <= right:
            mid = (left + right) // 2

            res = 0
            s = 0
            for x in nums:
                s += ceil(x / mid)
            
            if s <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left

        
nums = [1,2,5,9]
threshold = 6
print(Solution().smallestDivisor(nums, threshold))