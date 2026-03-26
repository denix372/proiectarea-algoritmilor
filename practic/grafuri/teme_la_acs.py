from collections import deque

n, x = map(int, input().split())
obl = list(map(lambda z : int(z) - 1, input().split()))
adj = [[] for _ in range(n)]
rev = [[] for _ in range(n)]
indeg = [0] * n

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] != 0:
        m = a[0]
        for j in range(1, m + 1):
            u = a[j] - 1
            adj[u].append(i)
            rev[i].append(u)

needed = [False] * n
q = deque()

for o in obl:
    if not needed[o]:
        needed[o] = True
        q.append(o)
    
while q:
    u = q.popleft()
    for v in rev[u]:
        if not needed[v]:
            needed[v] = True
            q.append(v)

indeg = [0] * n
for u in range(n):
    if needed[u]:
        for v in adj[u]:
            indeg[v] += 1

q = deque()
for u in range(n):
    if needed[u] and indeg[u] == 0:
        q.append(u)
cnt = 0
while q:
    u = q.popleft()
    cnt += 1
    for v in adj[u]:
        if needed[v]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

needs = 0
for u in range(n):
    if needed[u]:
        needs += 1

if cnt != needs:
    print(-1)
else:
    ans = []
    for u in range(n):
        if needed[u]:
            ans.append(u + 1)
    ans.sort()
    print(len(ans))
    print(*ans)