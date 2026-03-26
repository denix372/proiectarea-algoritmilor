from heapq import heappop, heappush

start, end, m = map(int, input().split())
q = []
edges = []
for _ in range(m):
    a, b  = map(int, input().split())
    edges.append((a, b))
edges.sort()

i = 0
current = start
level = 0

while current < end:
    while i < m and edges[i][0] <= current:
        heappush(q, (-edges[i][1], edges[i][1]))
        i += 1
    y = heappop(q)[1]
    current = y
    level += 1
print(level)
