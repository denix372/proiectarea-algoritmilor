from typing import List
from collections import defaultdict

class Solution:
    def max_operations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        cnt = 0
        for x in nums:
            target = k - x
            if d[target] > 0:
                cnt += 1
                d[target] -= 1
            else:
                d[x] += 1
        return cnt

nums = [1,2,3,4]
k = 5
print(Solution().maxOperations(nums, k))
