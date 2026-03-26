from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def dfs(u, sol):
            if u == n - 1:
                res.append(sol.copy())
                return
            for v in graph[u]:
                sol.append(v)
                dfs(v, sol)
                sol.remove(v)
        dfs(0, [0])
        return res
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution().allPathsSourceTarget(graph))