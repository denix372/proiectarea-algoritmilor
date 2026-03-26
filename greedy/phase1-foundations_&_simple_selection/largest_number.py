from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(cmp))
        res = "".join(nums)
        return "0" if res[0] == "0" else res

nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))