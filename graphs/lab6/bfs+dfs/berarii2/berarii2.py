from collections import deque

# method one, using dfs
def dfs_multisource(N, edges, sources):
    graph = [[] for _ in range(N + 1)]
    for x, y in edges:
        graph[y].append(x)   # inversam muchia
    seen = [False] * N

    def dfs(node):
        seen[node] = True
        for nxt in graph[node]:
            if not seen[nxt]:
                dfs(nxt)

    for s in sources:
        if not seen[s]:
            dfs(s)
    
    result = []
    for i in range(1, N ):
        if not seen[i]:
            result.append(i)
    return result

# method two, using bfs
def bfs_multisource(N, edges, sources):
    graph = [[] for _ in range(N + 1)]
    for x, y in edges:
        graph[y].append(x)   # inversam muchia
    seen = [False] * (N + 1)

    q = deque()

    for s in sources:
        if not seen[s]:
            seen[s] = True
            q.append(s)

    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not seen[nxt]:
                seen[nxt] = True
                q.append(nxt)

    result = [i for i in range(1, N + 1) if not seen[i]]
    return result

with open("berarii2.in", "r") as fin:
    N, M, P = map(int, fin.readline().split())

    #g = [[] for _ in range(N + 1)]
    edges = []
    for _ in range(M):
        x, y = map(int, fin.readline().split())
        edges.append((x, y))

    breweries = list(map(int, fin.readline().split()))

result = bfs_multisource(N, edges, breweries)

with open("berarii2.out", "w") as fout:
    fout.write(str(len(result)) + "\n")
    if result:
        fout.write("\n".join(map(str, result)))
