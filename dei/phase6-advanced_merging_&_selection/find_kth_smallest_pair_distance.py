from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 0

            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1

            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
    

nums = [1,6,1]
k = 3
print(Solution().smallestDistancePair(nums, k))