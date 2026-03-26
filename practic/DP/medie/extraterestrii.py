MOD = 666013

def solve(n, m, k , a):
    dp = [[0] * m for _ in range(n + 1)]
    # dp[len][j] = nr de cuvinte de lungime len care se termina in j
    for j in range(m):
        dp[1][j] = 1 # lungime 1
    for length in range(2, n + 1):
        for j in range(m):
            s = 0
            for i in range(m):
                if a[i][j]:
                    s += dp[length - 1][i]
            dp[length][j] = s % MOD
    print(sum(dp[n]) % MOD)

n, m, k = map(int, input().split())
a  = [[1] * m for _ in range(m)]
for _ in range(k):
    i, j = map(int, input().split())
    a[i - 1][j - 1] = 0

solve(n, m, k, a)
