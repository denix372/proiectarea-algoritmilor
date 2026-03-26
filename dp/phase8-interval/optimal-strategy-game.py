def solve(v):
    n = len(v)
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
    return first

def solve2(v):
    n = len(v)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + v[i]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = v[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            total_money = prefix[j + 1] - prefix[i]
            dp[i][j] = total_money - min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

arr = [5, 3, 7, 10]
print(solve(arr))
print(solve2(arr))

