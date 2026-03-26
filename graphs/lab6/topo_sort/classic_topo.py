from collections import deque

# basic topological sort (cycles are not detected => infinite loop if cycle exists)
def topo_sort(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)

    for node in range(len(graph)):
        if node not in visited:
            dfs(node)

    return list(reversed(stack))

# topological sort with cycle detection
def topo_sort_with_cycle(graph):
    n = len(graph)
    color = [0] * n
    order = []

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
        order.append(u)
        return True
        
    for u in range(n):
        if color[u] == 0:
            if dfs(u) == False:
                return []
    return order[::-1]

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
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order

graph = [
    [1,2],   # A → B,C
    [3,4,5], # B → D,E,F
    [6],     # C → G
    [],      # D
    [],      # E
    [7],     # F → H
    [8],     # G → I
    [],      # H
    []       # I
]

print(topo_sort(graph))
print(topo_sort_with_cycle(graph))
print(topo_kahn(graph))