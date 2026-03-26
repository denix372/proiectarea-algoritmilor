import sys
input = sys.stdin.readline
from collections import deque

def solve(n, adj):
    q = deque([0])
    visited = [False] * n
    visited[0] = True
    p = [0] * n
    while q:
        u = q.popleft()

        if u == n - 1:
            break

        for v in adj[u]:
            if not visited[v]:
                q.append(v)
                p[v] = u
                visited[v] = True
    if not visited[n - 1]:
        print("IMPOSSIBLE")
        return

    path = []
    i = n - 1
    while i != 0:
        path.append(i + 1)
        i = p[i]
    path.append(1)
    path.reverse()
    print(len(path))
    print(*path)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
solve(n, adj)
