from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        max_sum = sum(nums)
        s = 0
        arr = []
        for x in nums:
            if s > max_sum - s:
                return arr
            else:
                arr.append(x)
                s += x
        return arr
        
nums = [4,3,10,9,8]
print(Solution().minSubsequence(nums))
