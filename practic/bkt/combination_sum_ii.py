
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def back(sol, i, s):
            if s == target:
                res.append(sol.copy())
                return
            
            if s > target or i == n:
                return

            sol.append(candidates[i])
            back(sol, i + 1, s + candidates[i])
            sol.pop()


            while i < n - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            back(sol, i + 1, s)
        
        back([], 0, 0)
        return res




        