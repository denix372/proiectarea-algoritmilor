from typing import List
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def bkt(s):
            if s == target:
                return 1
            if s > target:
                return 0

            cnt = 0
            for x in nums:
                cnt += bkt(s + x)
            return cnt
        return bkt(0)

nums = [1,2,3]
target = 4
print(Solution().combinationSum4(nums, target))