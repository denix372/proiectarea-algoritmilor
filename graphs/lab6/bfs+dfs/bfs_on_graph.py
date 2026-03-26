
def bfs (graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        u = queue.pop(0)
        print(u, end = " ")

        for v in graph[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

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
bfs(graph, 'A')