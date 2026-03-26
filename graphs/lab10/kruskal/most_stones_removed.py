from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for r, c in stones:
            if r not in parent:
                parent[r] = r
                rank[r] = 0
            if ~c not in parent:
                parent[~c] = ~c
                rank[~c] = 0
            union(r, ~c) 
        
        roots = set(find(x) for x in parent)
        return len(stones) - len(roots)


stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(Solution().removeStones(stones))