from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
        
        res = [[] for _ in range(n)]

        def dfs(u, start):
            for v in adj[u]:
                if not res[v] or res[v][-1] != start:
                    res[v].append(start)
                    dfs(v, start)

        for i in range(n):
            dfs(i, i)

        return res

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(Solution().getAncestors(n, edgeList))