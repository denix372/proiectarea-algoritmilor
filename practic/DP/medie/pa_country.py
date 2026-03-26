INF = 10**9
MOD = 666013
def solve(n, m, p, a, x1, y1, x2, y2):
    dp = [[[0] * m for _ in range(n)] for _ in range(p + 1)]
    dp[0][x1 - 1][y1 - 1] = 1
    for t in range(1, p + 1):
        for i in range(n):
            for j in range(m):
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if a[nx][ny] != 1:
                            dp[t][i][j] += dp[t - 1][nx][ny] % MOD
    return sum(dp[t][x2 - 1][y2 - 1] for t in range(1, p + 1)) % MOD


n, m, p = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, p, a, x1, y1, x2, y2))