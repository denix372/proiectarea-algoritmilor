from typing import List
import heapq

INF = 10**15

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for a, b, w in edges:
            self.adj[a].append((b, w))

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.adj[a].append((b, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [INF] * self.n
        dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


ops = ["Graph","shortestPath","shortestPath","addEdge","shortestPath"]
args = [
    [4, [[0,2,5],[0,1,2],[1,2,1],[3,0,3]]],
    [3, 2],
    [0, 3],
    [[1,3,4]],
    [0, 3]
]
obj = None
out = []

for op, arg in zip(ops, args):
    if op == "Graph":
        n, edges = arg
        obj = Graph(n, edges)
        out.append(None)

    elif op == "addEdge":
        obj.addEdge(arg[0])
        out.append(None)

    elif op == "shortestPath":
        res = obj.shortestPath(arg[0], arg[1])
        out.append(res)

print(out)
