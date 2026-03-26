
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        cnt = 0

        for x in nums:
            if x % 2 == 1:
                prefix += 1
            
            if prefix - k in d:
                cnt += d[prefix - k]
            
            d[prefix] += 1

        return cnt

nums = [1,1,2,1,1]
k = 3
print(Solution().numberOfSubarrays(nums, k))