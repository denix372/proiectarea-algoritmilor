def solve(n, v):
    dp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = v[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(v[i] - dp[i + 1][j],
                            v[j] - dp[i][j - 1])
    total = sum(v)
    first =(total + dp[0][n - 1]) // 2
    print(first)


n = int(input())
v = list(map(int, input().split()))
solve(n, v)