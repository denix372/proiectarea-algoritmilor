from typing import List
from collections import defaultdict

class Solution:
    def find_pairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        cnt = 0
    
        for x in nums:
            d[x] += 1

        if k == 0:
            for key, v in d.items():
                if v > 1:
                    cnt += 1
        else:
            for key, v in d.items():
                if key + k in d:
                    cnt += 1
        return cnt
nums = [3,1,4,1,5] 
k = 2
print(Solution().findPairs(nums, k))