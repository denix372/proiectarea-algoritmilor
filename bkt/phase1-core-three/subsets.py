from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def bkt(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            bkt(i + 1)

            subset.pop()
            bkt(i + 1)

        bkt(0)
        return res
    
sol = Solution()
res = sol.subsets([1, 2, 3])
for sub in res:
    print(sub)