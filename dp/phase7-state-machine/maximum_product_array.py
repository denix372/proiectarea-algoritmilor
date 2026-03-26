from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpmax = [0] * n
        dpmin = [0] * n
        dpmax[0] = dpmin[0] = nums[0]

        for i in range(1, n):
            if nums[i] >= 0:
                dpmax[i] = max(nums[i], dpmax[i - 1] * nums[i])
                dpmin[i] = min(nums[i], dpmin[i - 1] * nums[i])
            elif nums[i] < 0:
                dpmax[i] = max(nums[i], dpmin[i - 1] * nums[i])
                dpmin[i] = min(nums[i], dpmax[i - 1] * nums[i])
        return max(dpmax)

nums = [2,3,-2,4]
print(Solution().maxProduct(nums))
