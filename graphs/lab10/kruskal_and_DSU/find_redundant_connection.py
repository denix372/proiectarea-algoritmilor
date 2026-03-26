from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, a, b):
            ra = find(parent, a)
            rb = find(parent, b)
            if ra == rb:
                return False
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[ra] = rb
                rank[ra] += 1
            return True
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        for u, v in edges:
            if not union(parent, rank, u, v):
                return (u, v)
        return -1

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution().findRedundantConnection(edges))