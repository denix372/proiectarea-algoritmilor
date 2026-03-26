def dfs(u, visited, match, adj):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or dfs(match[v], visited, match, adj):
                match[v] = u
                return True
    return False

def max_bipartite_matching(n, m, adj):
    match = [-1] * m
    result = 0

    for u in range(n):
        visited = [False] * m
        if dfs(u, visited, match, adj):
            result += 1

    return result, match

n = 3
m = 3

adj = [
    [0, 1],
    [0],
    [0, 2]]

result, match = max_bipartite_matching(n, m, adj)
print("Maximum matching =", result)
print("matches =", match)
