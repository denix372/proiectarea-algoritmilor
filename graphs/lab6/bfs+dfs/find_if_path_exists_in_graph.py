from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited[source] = True

        def dfs(u):
            visited[u] = True
            if u == destination:
                return True
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
            return False
        return dfs(source)

sol = Solution()
n = 6
source = 0
destination = 5
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
print(sol.validPath(n, edges,source, destination))