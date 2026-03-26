from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = []

        for a, b in edges:
            if a in visited:
                return a

            if b in visited:
                return b

            visited.append(a)
            visited.append(b)
        return 0
    
sol = Solution()
edges = [[1,2],[2,3],[4,2]]
print(sol.findCenter(edges))