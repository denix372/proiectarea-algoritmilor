from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        n = len(nums)
        def bkt(i, sol):
            if i == n:
                res.append(sol.copy())
                return

            # all subset that include nums[i]
            sol.append(nums[i])
            bkt(i + 1, sol)
            sol.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            bkt(i + 1, sol)

        bkt(0, [])
        return res
        
sol = Solution()

for i in sol.subsetsWithDup([1, 2, 2, 3]):
    print(i)