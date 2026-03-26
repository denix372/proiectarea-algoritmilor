from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0] * n
        for a, b in edges:
            indeg[b] += 1
        res = []
        for i in range(n):
            if indeg[i] == 0:
                res.append(i)
        return res
        # return [i for i in range(n) if indeg[i] == 0 ]
sol = Solution()
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(sol.findSmallestSetOfVertices(n, edges))