from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        for i in range(len(nums)):
            if j == k:
                return sum(nums)
            if nums[i] < 0:
                nums[i] = -nums[i]
                j += 1
            else:
                break
        if (k - j) % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2 * min(nums)
                
nums = [4,2,3]
k = 1
print(Solution().largestSumAfterKNegations(nums, k))