
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= sufix
            sufix *= nums[i]

        return res
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))