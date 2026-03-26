def dfs(u, seen, match, adj):
    for v in adj[u]:
        if not seen[v]:
            seen[v] = True
            if match[v] == -1 or dfs(match[v], seen, match, adj):
                match[v] = u
                return True
    return False

def max_bipartite_matching(n, m, adj):
    match = [-1] * m
    result = 0

    for u in range(n):
        seen = [False] * m
        if dfs(u, seen, match, adj):
            result += 1

    return result, match

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(k):
    a, b =map(int, input().split())
    adj[a - 1].append(b - 1)

result, match = max_bipartite_matching(n, m, adj)

print(result)
for girl in range(m):
    if match[girl] != -1:
        boy = match[girl]
        print(boy + 1, girl + 1)