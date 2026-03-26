from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        i, j = -1, -1
    
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            if nums[mid] == target:
                i = mid
                
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            if nums[mid] == target:
                j = mid
    
        return [i, j]
    
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))