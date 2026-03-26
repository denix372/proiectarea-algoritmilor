from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        cnt = 0
        for start in range(n):
            for end in range(start + 1, n + 1):
                if prefix[end] - prefix[start] == k:
                    cnt += 1
        return cnt

class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1 
        prefix = cnt = 0
    
        for x in nums:
            prefix += x
            if prefix - k in d:
                cnt += d[prefix - k]

            d[prefix] += 1

        return cnt

nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, k))