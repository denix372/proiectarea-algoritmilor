def solve(ok, n, p):
    p = [(a, b, c, i) for i , (a, b, c) in enumerate(p)]
    p.sort(key = lambda x: (x[0], x[1], x[2]))

    dp = [1] * n
    pr = [-1] * n
    for i in range(n):
        a2, b2, c2, _ = p[i]
        for j in range(i):
            a1, b1, c1, _ = p[j]
            if a1 <= a2 and b1 <= b2 and c1 >= c2:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pr[i] = j
    sol = max(dp)
    print(sol)
    if ok == 1:
        i = dp.index(sol)
        res = []
        while i != -1:
            res.append(p[i][3])
            i = pr[i]
        res.reverse()
        print(*res)

ok = int(input())
n = int(input())
p = []
for _ in range(n):
    a, b, c = map(int, input().split())
    p.append((a, b, c))
solve(ok, n, p)