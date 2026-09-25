class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        k = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k = i + 1
  
            res = max(res, i - k + 1)

        return res

nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))