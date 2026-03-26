from math import comb

def olimpiada(n, k, p):
    #
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1.0

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * p[i - 1]
    return dp[n][k] / comb(n, k)

n, k = map(int, input().split())
probs = []
for i in range(n):
    p = float(input())
    probs.append(p)
print(f"{olimpiada(n, k, probs):.5f}")