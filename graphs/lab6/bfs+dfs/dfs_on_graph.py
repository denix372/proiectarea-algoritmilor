def dfs (graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end = " ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

def dfs2(graph, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end= " ")

    for n in graph[node]:
        if n not in visited:
            dfs2(graph, n, visited)

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
dfs(graph, 'A')