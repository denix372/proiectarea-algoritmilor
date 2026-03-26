from collections import deque

def bfs_multi_source(graph, sources, seen):
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


with open("berarii2.in", "r") as fin:
    N, M, P = map(int, fin.readline().split())

    # graful invers
    g = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, fin.readline().split())
        g[y].append(x)   # inversăm muchia

    breweries = list(map(int, fin.readline().split()))

seen = [False] * (N + 1)

bfs_multi_source(g, breweries, seen)

result = [i for i in range(1, N + 1) if not seen[i]]

with open("berarii2.out", "w") as fout:
    fout.write(str(len(result)) + "\n")
    if result:
        fout.write("\n".join(map(str, result)))
