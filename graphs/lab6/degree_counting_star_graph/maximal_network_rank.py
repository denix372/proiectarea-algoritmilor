from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank = 0
        degre = [0] * n
        edges = set()
        for a, b in roads:
            degre[a] += 1
            degre[b] += 1
            edges.add((a, b))

        for i in range(n - 1):
            for j in range(i + 1, n):
                r = degre[i] + degre[j]
                if (i, j) in edges or (j, i) in edges:
                    r -= 1
                rank = max(rank, r)
        return rank
sol = Solution()
n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(sol.maximalNetworkRank(n, roads))