from typing import List
from heapq import heappop, heappush

INF = 10**15

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for a, b, w in edges:
            self.adj[a].append((b, w))

    def add_edge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.adj[a].append((b, w))

    def shortest_path(self, node1: int, node2: int) -> int:
        dist = [INF] * self.n
        dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))

        return -1

g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(g.shortestPath(3, 2)) # return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
print(g.shortestPath(0, 3)) # return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]) # We add an edge from node 1 to node 3, and we get the second diagram above.
print(g.shortestPath(0, 3)) # return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.