from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def back(sol, i, total):
            if total == target:
                res.append(sol.copy())
                return

            if total > target or i >= n:
                return

            sol.append(candidates[i])
            back(sol, i, total + candidates[i])
            sol.pop()
            back(sol, i + 1, total)

        back([], 0,  0)
        return res
        
sol = Solution()
for i in sol.combinationSum([2, 3, 7], 7):
    print(i)

