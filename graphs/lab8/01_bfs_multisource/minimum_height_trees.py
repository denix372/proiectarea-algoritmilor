from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def bfs(start):
            q = deque([start])
            visited = [False] * n
            visited[start] = True
            parent = [-1] * n
            
            farthest_node = start
            
            while q:
                u = q.popleft()
                farthest_node = u
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        q.append(v)
                        
            return farthest_node, parent

        node_A, _ = bfs(0)
        node_B, parent = bfs(node_A)

        path = []
        curr = node_B
        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        m = len(path)
        if m % 2 == 1:
            return [path[m // 2]]
        else:
            return [path[m // 2 - 1], path[m // 2]]

class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        # 2. Find the first layer of leaves (degree == 1)
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        
        remaining_nodes = n
        
        while remaining_nodes > 2:
            # The number of leaves in the current layer
            leaves_count = len(q)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                u = q.popleft()
                
                for v in adj[u]:
                    degree[v] -= 1
                    # If the neighbor becomes a leaf, queue it up for the next layer!
                    if degree[v] == 1:
                        q.append(v)
    
        # 4. The remaining nodes (1 or 2) are the centroids!
        return list(q)

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(Solution().findMinHeightTrees(n, edges))
print(Solution2().findMinHeightTrees(n, edges))