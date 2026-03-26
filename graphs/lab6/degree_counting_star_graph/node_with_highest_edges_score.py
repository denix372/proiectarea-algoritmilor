from typing import List
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        sol = 0
        max_score = 0
        for i in range(n):
            scores[edges[i]] += i
            if max_score < scores[edges[i]] or max_score == scores[edges[i]] and sol > edges[i]:
                max_score = scores[edges[i]]
                sol = edges[i]
        return sol
        
sol = Solution()
edges = [1,0,0,0,0,7,7,5]
print(sol.edgeScore(edges))