from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
    
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return
            
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[ra] = rb
                rank[ra] += 1
            return
        
        parent = list(range(n))
        rank = [0] * (n)
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        cnt = 0
        for i in range(n):
            if parent[i] == i:
                cnt += 1
        return cnt


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))