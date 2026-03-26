import sys
input = sys.stdin.readline
from collections import deque

def solve(n, s, t, original):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if original[u][v] == 1:
                residual[u][v] = 1

    def bfs():
        parent = [-1] * n
        parent[s] = -2 #source
        q = deque([(s, float("inf"))])

        while q:
            u, flow = q.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    new_flow = min(flow, residual[u][v])
                    if v == t:
                        return new_flow, parent
                    q.append((v, new_flow))
        return 0, parent
    max_flow = 0
    while True:
        flow, parent = bfs()
        if flow == 0:
            break
        max_flow += flow
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u
    print(max_flow)

    paths = []
    while True:
        parent = [-1] * n
        parent[0] = -2
        q = deque([0])

        while q:
            u = q.popleft()
            if u == n - 1:
                break
            for v in range(n):
                if parent[v] == -1 and  original[u][v] == 1 and residual[u][v] == 0:
                    parent[v] = u
                    q.append(v)
        if parent[n - 1] == -1:
            break

        path = []
        v = n - 1
        while v != -2:
            path.append(v)
            u = parent[v]
            if u == -2:
                break
            residual[u][v] = 1
            v = u
        paths.append(path[::-1])
    for p in paths:
        print(len(p))
        for x in p:
            print(x + 1, end = " ")
        print()

n, m = map(int, input().split())
original = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    original[a - 1][b - 1] = 1

solve(n, 0, n - 1, original)