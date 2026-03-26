from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [-1] * (n + 1)
        
        for i in range(1, n + 1):
            if colors[i] == -1:
                q = deque([i])
                colors[i] = 0  
                
                while q:
                    node = q.popleft()
                    
                    for neighbor in graph[node]:
                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[node]
                            q.append(neighbor)
                        elif colors[neighbor] == colors[node]:
                            return False
                            
        return True

n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(Solution().possibleBipartition(n, dislikes))