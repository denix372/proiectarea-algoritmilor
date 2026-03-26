import sys
input = sys.stdin.readline
INF = 10**9
def solve(n, K , a):
    dp = [[[INF] * (n + 1) for _ in range(n + 1)] for _ in range(K + 1)]
    dp[1][0][0] = a[0][0]
    for k in range(2,K + 1):
        for i in range(n):
            for j in range(n):
                m = INF
                if i > 0:
                    m = min(m, dp[k-1][i - 1][j])
                if j > 0:
                    m = min(m, dp[k-1][i][j - 1])
                if i > 0 and j > 0:
                    m = min(m,  dp[k-1][i - 1][j - 1])
                if m != INF:
                    dp[k][i][j] = a[i][j] + m
    res = INF
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res = min(res, dp[K][i][j])
    print(res)

n, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
solve(n, K, a)