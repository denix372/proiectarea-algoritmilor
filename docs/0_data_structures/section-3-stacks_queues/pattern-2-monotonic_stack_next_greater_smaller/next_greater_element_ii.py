from typing import List

class Solution:
    def next_greater_elements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                j = stack.pop()
                res[j] = nums[i % n]
            if i < n:
                stack.append(i % n)

        return res

nums = [1,2,1]
print(Solution().nextGreaterElements(nums))