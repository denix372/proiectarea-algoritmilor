
n, m, p = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

for _ in range(p):
    x = list(map(int, input().split()))

    pos = [0]* (n + 1)
    for i, u in enumerate(x):
        pos[u] = i
    
    ok = True
    for a, b in edges:
        if pos[a] - pos[b] >= 0:
            ok = False
            break
    if not ok:
        print("NU")
    else:
        print("DA")