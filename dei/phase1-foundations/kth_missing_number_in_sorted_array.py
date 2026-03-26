from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def count_missing_before_index(index: int) -> int:
            return nums[index] - nums[0] - index

        n = len(nums)
        total_missing_in_range = count_missing_before_index(n - 1)
        if k > total_missing_in_range:
            return nums[n - 1] + k - total_missing_in_range

        left, right = 0, n - 1
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if count_missing_before_index(mid) >= k:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[first_true_index - 1] + k - count_missing_before_index(first_true_index - 1)

nums = [4, 7, 9, 10]
k = 3
print(Solution().missingElement(nums, k))