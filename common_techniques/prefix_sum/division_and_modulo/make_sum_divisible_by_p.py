from collections import defaultdict

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0
        
        d = defaultdict(int)
        d[0] = -1
        prefix = 0
        min_len = len(nums)
        for i, x in enumerate(nums):
            prefix += x
            rest = prefix % p
            needed = (rest - target) % p
            if needed in d:
                min_len = min(min_len, i - d[needed])

            d[rest] = i

        if min_len < len(nums):
            return min_len
        else:
            return -1

nums = [3,1,4,2]
p = 6
print(Solution().minSubarray(nums, p))