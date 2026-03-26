from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        left_index = bisect_left(nums, target)
        right_index = bisect_right(nums, target)

        target_count = right_index - left_index

        return target_count > len(nums) // 2
    
nums = [1, 2, 3, 3, 3, 3, 4]
target = 3
print(Solution().isMajorityElement(nums, target))