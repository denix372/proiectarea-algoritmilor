import sys
input = sys.stdin.readline
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)

    if ra == rb:
        return False
    if size[ra] < size[rb]:
        parent[ra] = rb
        size[rb] += size[ra]
    else:
        parent[rb] = ra
        size[ra] += size[rb]
    return True


def kruskal(n, edges):
    for u, v in edges:
        union(parent, size, u, v)
    cnt = 0
    r = 0
    for i in range(1, n + 1):
        if parent[i] == i:
            cnt += 1
        r = max(r, size[i])
    return cnt, r

n, m = map(int, input().split())
edges = []
comp = n
parent = list(range(n + 1))
size = [1] * (n + 1)
largest = 1
for _ in range(m):
    a, b =  map(int, input().split())
    edges.append((a, b))
    if union(parent, size, a, b):
        comp -= 1
        largest = max(largest, size[find(parent, a)])
    print(comp, largest)