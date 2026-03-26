from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if(len(connections) < n - 1):
            return -1
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
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
    
        for u, v, in connections:
            union(u, v)

        cnt = 0
        for x in range(n):
            if parent[x] == x:
                cnt += 1
        
        return cnt - 1


n = 4
connections = [[0,1],[0,2],[1,2]]
print(Solution().makeConnected(n, connections))