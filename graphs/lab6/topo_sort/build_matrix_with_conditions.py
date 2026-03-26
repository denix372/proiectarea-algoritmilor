from typing import List
from collections import deque, defaultdict

class Solution:
    def topo(self, k, edges):
        graph = defaultdict(list)
        indeg = [0] * (k + 1)

        for a, b in edges:
            graph[a].append(b)
            indeg[b] += 1

        q = deque([i for i in range(1, k+1) if indeg[i] == 0])
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return order if len(order) == k else []

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowOrder = self.topo(k, rowConditions)
        colOrder = self.topo(k, colConditions)

        if not rowOrder or not colOrder:
            return []

        rowPos = {x: i for i, x in enumerate(rowOrder)}
        colPos = {x: i for i, x in enumerate(colOrder)}

        matrix = [[0] * k for _ in range(k)]
        for x in range(1, k+1):
            matrix[rowPos[x]][colPos[x]] = x

        return matrix

k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
print(Solution().buildMatrix(k, rowConditions, colConditions))