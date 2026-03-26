from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        directed = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            directed.add((a, b))

        visited =[False] * n
        res = 0
        def dfs(u):
            nonlocal res
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    if (u, v) in directed:
                        res += 1
                    dfs(v)
        dfs(0)
        return res
        
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(Solution().minReorder(n, connections))