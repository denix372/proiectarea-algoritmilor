from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_pal(sub):
            return sub == sub[::-1]

        def backtrack(start, sol):
            if start == n:
                res.append(sol.copy())
                return

            for end in range(start, n):
                sub = s[start : end + 1]
                if is_pal(sub):
                    sol.append(sub)
                    backtrack(end + 1, sol)
                    sol.pop()
    
        backtrack(0, [])
        return res
        
        

s = "aab"
sol = Solution()
print(sol.partition(s))