from collections import defaultdict

class Solution:
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        s = 0

        for i in range(k):
            s += nums[i]
            d[nums[i]] += 1
        
        if len(d) == k:
            res = s
        
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            d[nums[i - k]] -= 1
            d[nums[i]] += 1
            if d[nums[i - k]] == 0:
                del d[nums[i - k]]
            
            if len(d) == k:
                res = max(res, s)
        
        return res
            
nums = [1,5,4,2,9,9,9]
k = 3
print(Solution().maximumSubarraySum(nums, k))