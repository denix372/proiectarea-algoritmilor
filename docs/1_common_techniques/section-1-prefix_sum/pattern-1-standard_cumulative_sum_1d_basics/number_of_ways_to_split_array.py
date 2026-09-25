
class Solution:
    def ways_to_split_array(self, nums: list[int]) -> int:
        cnt = 0
        total = sum(nums)
        prefix = 0
        for i in range(len(nums) - 1):
            prefix += nums[i]
            sufix = total - prefix
            if prefix >= sufix:
                cnt += 1
        return cnt

nums = [10,4,-8,7]
print(Solution().waysToSplitArray(nums))