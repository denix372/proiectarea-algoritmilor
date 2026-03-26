def solve(n, k):
    res = []
    def bkt(sol, i):
        if len(sol) == k:
            res.append(sol.copy())
            return
        
        for j in range(i, n + 1):
            sol.append(j)
            bkt(sol, j + 1)
            sol.pop()
    bkt([], 1)
    return res

n, k = map(int, input().split())
for r in solve(n, k):
    print(*r)