#decomment just if you use the first function
#import sys
#sys.setrecursionlimit(300000)
from collections import deque

def findOrder(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)

    res = []
    color = [0] * (n + 1)
    def dfs(u):
        if color[u] == 1:
            return False
        if color[u] == 2:
            return True

        color[u] = 1
        for v in graph[u]:
            if dfs(v) == False:
                return False
        color[u] = 2
        res.append(u)

    for u in range(1, n + 1):
        if dfs(u) == False:
            return []

    res.reverse()
    return res

def bfs_khan(n, prerequisites):
    adj = {c : [] for c in range(1, n + 1)}
    indeg = {c : 0 for c in range(1, n + 1)}

    for a, b in prerequisites:
        adj[a].append(b)
        indeg[b] += 1

    q = deque([c for c in range(1, n + 1) if indeg[c] == 0])

    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    # if not all nodes are in order -> cycle
    if len(order) != n:
        return []

    return order

n, m = map(int, input().split())
req = []

for _ in range(m):
    (a, b) = map(int, input().split())
    req.append([a, b])

res = findOrder(n, req)
if res == []:
    print("IMPOSSIBLE")
else:
    for i in res:
        print(i, end = " ")