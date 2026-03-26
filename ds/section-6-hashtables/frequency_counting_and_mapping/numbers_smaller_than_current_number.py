from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, x in enumerate(sorted(nums)):
            if x not in d:
                d[x] = i
                
        return [d[x] for x in nums]

nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))