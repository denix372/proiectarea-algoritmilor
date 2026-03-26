from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def back(sol,start):
            if start == n:
                res.append(sol.copy())
                return

            for end in range(start, n):
                p = s[start:end + 1]
                if p == p[::-1]:
                    sol.append(p)
                    back(sol, end + 1)
                    sol.pop()

        back([], 0)
        return res
        