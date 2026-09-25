from typing import List

class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))