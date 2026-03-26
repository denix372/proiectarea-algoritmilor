from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        i = j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1

        return res    

g = [1,2]
s = [1,2,3]
print(Solution().findContentChildren(g, s))