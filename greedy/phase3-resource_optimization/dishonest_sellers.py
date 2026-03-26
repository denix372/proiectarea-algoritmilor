
from heapq  import heappush, heappop
def solve(n, k, a, b):
    q = []
    for i in range(n):
        heappush(q, (a[i] - b[i], a[i], b[i]))

    res = 0
    for i in range(k):
        _, r, _ = heappop(q)
        res += r

    while q:
        _, r1, r2 = heappop(q)
        res += min(r1, r2)
    return res

k= 3
a = [3, 4, 7, 10, 3]
b = [4, 5, 5, 12, 5]
print(solve(len(a), k, a, b))