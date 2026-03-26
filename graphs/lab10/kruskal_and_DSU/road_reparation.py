def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[b] = a
    return True

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))

edges.sort()

parent = list(range(n))
total = 0
used = 0

for c, a, b in edges:
    if unite(a, b):
        total += c
        used += 1

if used != n - 1:
    print("IMPOSSIBLE")
else:
    print(total)
