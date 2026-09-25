class Solution:
    def find_middle_index(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        sufix = [0] * n
        sufix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            sufix[i] = sufix[i + 1] + nums[i]
        
        for i in range(n):
            if prefix[i] == sufix[i]:
                return i
        return -1

class Solution2:
    def find_middle_index(self, nums: list[int]) -> int:
        prefix = 0
        total = sum(nums)
        for i in range(len(nums)):
            sufix = total - prefix - nums[i]
            if prefix == sufix:
                return i
            prefix += nums[i]
        return -1

nums = [2,3,-1,8,4]
print(Solution().findMiddleIndex(nums))
print(Solution2().findMiddleIndex(nums))