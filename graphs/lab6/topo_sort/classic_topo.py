from collections import deque

def topo_sort(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)

    for node in graph:
        if node not in visited:
            dfs(node)

    return list(reversed(stack))

# Kahn's Algorithm
def topo_kahn(graph):
    n = len(graph)
    indeg = [0] * n
    for u in range(n):
        for v in graph[u]:
            indeg[v] += 1

    q = deque([u for u in range(n) if indeg[u] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] = -1
            if indeg[v] == 0:
                q.append(v)
    return order

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E', 'F'],
    'C' : ['G'],
    'D' : [],
    'E' : [],
    'F' : ['H'],
    'G' : ['I'],
    'H' : [],
    'I' : [],
}



print(topo_sort(graph))
print(topo_kahn(graph))