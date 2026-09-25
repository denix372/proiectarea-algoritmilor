from collections import defaultdict

class Solution:
    def check_subarray_sum(self, nums: list[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        prefix = 0
        
        for i, x in enumerate(nums):  
            prefix += x
            rest = prefix % k
            if rest in d:
                if i - d[rest] >= 2:
                    return True
            else:
                d[rest] = i
    
        return False

nums = [23,2,4,6,7]
k = 6
print(Solution().checkSubarraySum(nums, k))