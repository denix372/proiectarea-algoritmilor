from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

even_count = 0
odd_count = 0

for u in range(1, n + 1):
    if dist[u] == -1:
        continue

    if dist[u] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    for v in adj[u]:
        if dist[v]!= -1:
            if dist[u] % 2 == dist[v] % 2:
                if dist[u] % 2 == 0:
                    even_valid = False
                else:
                    odd_valid = False

ans = min(even_count, odd_count)
print(ans)