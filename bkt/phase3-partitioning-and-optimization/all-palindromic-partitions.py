from typing import List

class Solution:
    def partition(self, s: str):
        n = len(s)
        res = []
        part = []

        # 1. Precompute palindromes
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or pal[i+1][j-1]:
                        pal[i][j] = True

        # 2. Backtracking using pal[][] O(1)
        def back(i):
            if i == n:
                res.append(part.copy())
                return

            for j in range(i, n):
                if pal[i][j]:
                    part.append(s[i:j+1])
                    back(j + 1)
                    part.pop()

        back(0)
        return res

        

s = "aab"
sol = Solution()
print(sol.partition(s))