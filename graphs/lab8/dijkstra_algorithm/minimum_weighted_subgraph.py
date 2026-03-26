from typing import List
from heapq import heappush, heappop

INF = 10**10
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            rev[b].append((a, w))
        
        def dijkstra(start_node, graph):
            dist = [INF] * n
            dist[start_node] = 0
            q = [(0, start_node)]
            
            while q:
                d, u = heappop(q)
                
                if d > dist[u]:
                    continue
                    
                for v, w in graph[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heappush(q, (dist[v], v))
                        
            return dist        

        dist1 = dijkstra(src1, adj)        # dist from src1 to X
        dist2 = dijkstra(src2, adj)        # dist from src2 to X
        dist3 = dijkstra(dest, rev)    # dist from X to dest

        min_weight = INF
        for i in range(n):
            total = dist1[i] + dist2[i] + dist3[i]
            if total < min_weight:
                min_weight = total
                
        return min_weight if min_weight != INF else -1

n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5
print(Solution().minimumWeight(n, edges, src1, src2, dest))
