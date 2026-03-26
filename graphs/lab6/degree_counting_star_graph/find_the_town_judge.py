from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)
        max_in = -1
        town = 1

        for a, b in trust:
            indeg[b] += 1
            outdeg[a] += 1
            if max_in < indeg[b]:
                max_in = indeg[b]
                town = b
        if indeg[town] == n - 1 and outdeg[town] == 0:
            return town
        return -1

sol = Solution()
n = 3
trust = [[1,3],[2,3]]
print(sol.findJudge(n, trust))