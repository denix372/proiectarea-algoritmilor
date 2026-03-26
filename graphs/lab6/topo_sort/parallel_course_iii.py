from typing import List
from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        
        for a, b in relations:
            adj[a].append(b)
            indeg[b] += 1
    
        dist = [0] * (n + 1)
        q = deque()

        for i in range(1, n + 1):
            if indeg[i] == 0:
                dist[i] = time[i - 1]
                q.append(i)
        while q:
            u = q.popleft()
            
            for v in adj[u]:
                dist[v] = max(dist[v], dist[u] + time[v - 1])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return max(dist)

n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
print(Solution().minimumTime(n, relations, time))