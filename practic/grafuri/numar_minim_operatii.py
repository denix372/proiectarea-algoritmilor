from collections import deque

n = int(input())
l = list(map(int, input().split()))
src, tgt = map(int, input().split())

d = abs(tgt - src)

lo = src - d
hi = src + d

q = deque()
q.append((src, 0))
vis = set([src])

while q:
    x, dist = q.popleft()

    if x == tgt:
        print(dist)
        break
    for v in l:
        nx1 = x + v
        nx2 = x - v
        
        if lo <= nx1 <= hi and nx1 not in vis:
            vis.add(nx1)
            q.append((nx1, dist + 1))
        if lo <= nx2 <= hi and nx2 not in vis:
            vis.add(nx2)
            q.append((nx2, dist + 1))
        