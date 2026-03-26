from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n 
        
        for i in range(n):
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

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(Solution().isBipartite(graph))