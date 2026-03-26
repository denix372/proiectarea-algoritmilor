from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def back(sol, i):
            if i == n:
                res.append(sol.copy())
                return

            sol.append(nums[i])
            back(sol, i + 1)
            sol.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            back(sol, i + 1)

        back([], 0)
        return res