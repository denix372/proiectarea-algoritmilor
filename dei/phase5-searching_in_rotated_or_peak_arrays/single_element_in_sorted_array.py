from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[left]
    
nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))