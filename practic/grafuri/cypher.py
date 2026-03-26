from collections import deque

t = int(input())

for _ in range(t):
    i1, i2, i3, i4 = map(int, input().split())
    src = i1*1000 + i2*100 + i3*10 + i4
    f1, f2, f3, f4 = map(int, input().split())
    dst = f1*1000 + f2*100 + f3*10 + f4
    n = int(input())
    res = set()
    for _ in range(n):
        r1, r2, r3, r4 = map(int, input().split())
        r = r1*1000 + r2*100 + r3*10 + r4
        res.add(r)

    if src in res:
        print(-1)
        continue

    q = deque([src])
    dist = [-1] * 10000
    dist[src] = 0

    while q:
        u = q.popleft()
        if u == dst:
            print()
            print(dist[u])
            print()
            break

        a = u//1000
        b = (u//100) % 10
        c = (u//10) % 10
        d = u % 10
        digits = [a, b, c, d]
        for i in range(4):
            for dx in (-1, 1):
                nd = digits.copy()
                nd[i] = (nd[i] + dx) % 10
                v = nd[0] * 1000 + nd[1] * 100 + nd[2] * 10 + nd[3]
                
                if v not in res and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
    else:
        print(-1)