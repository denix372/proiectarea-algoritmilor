from typing import List
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [0] * n
        q = deque()
        graph2 = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                graph2[v].append(u)
                outdeg[u] += 1
            if outdeg[u] == 0:
                q.append(u)
        
        # graph2 = inverse graph
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph2[u]:
                outdeg[v] -= 1
                if  outdeg[v] == 0:
                    q.append(v)
        order.sort()
        return order
    
    def eventualSafeNodes2(self, graph):
        n = len(graph)
        color = [0] * n

        def dfs(u):
            if color[u] == 1:
                return False
            if color[u] == 2:
                return True

            color[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            color[u] = 2 
            return True
    
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

graph = [[1,2],[2,3],[5],[0],[5],[],[]]     
print(Solution().eventualSafeNodes(graph))
print(Solution().eventualSafeNodes2(graph))