from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        if n >= 9:
            limit = 9
        else:
            limit = n 
        nums = list(range(1, limit + 1))

        def back(sol, i, total):
            if total == n and len(sol) == k:
                res.append(sol.copy())
                return

            if total > n or i == len(nums):
                return

            sol.append(nums[i])
            back(sol, i + 1, total + nums[i])
            sol.pop()
            back(sol, i + 1, total)

        back([], 0,  0)
        return res
        

sol = Solution()
for i in sol.combinationSum3(3, 9):
    print(i)