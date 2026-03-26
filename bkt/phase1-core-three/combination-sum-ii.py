from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        n = len(candidates)

        def back(sol, i, total):
            if total == target:
                res.append(sol.copy())
                return

            if total > target or i >= n:
                return

            sol.append(candidates[i])
            back(sol, i + 1, total + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            back(sol, i + 1, total)

        back([], 0,  0)
        return res
        
        
sol = Solution()
for i in sol.combinationSum2([10,1,2,7,6,1,5], 8):
    print(i)

