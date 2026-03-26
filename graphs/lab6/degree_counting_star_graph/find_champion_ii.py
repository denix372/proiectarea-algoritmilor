from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for a, b in edges:
            indeg[b] += 1
        
        res = [i for i in range(n) if indeg[i] == 0]
        if len(res) != 1:
            return -1
        return res[0]
        
sol = Solution()
n = 3
edges = [[0,1],[1,2]]
print(sol.findChampion(n, edges))