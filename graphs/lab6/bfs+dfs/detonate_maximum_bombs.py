from typing import List
from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    adj[i].append(j)

        max_detonated = 0
        
        for i in range(n):
            visited = set([i])
            q = deque([i])
            
            while q:
                u = q.popleft()
                
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            
            
            max_detonated = max(max_detonated, len(visited))
            
            # Optimization: If we already found a bomb that detonates ALL bombs, 
            # we can't do better than n.
            if max_detonated == n:
                return n
                
        return max_detonated

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(Solution().maximumDetonation(bombs))