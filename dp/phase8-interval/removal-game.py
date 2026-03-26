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

def solve2(n, v):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + v[i]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = v[i]
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # The total points available in the current interval [i, j]
            total_money = prefix[j + 1] - prefix[i]
            
            # We take the total money and SUBTRACT what the opponent will optimally take.
            # To maximize our share, we leave the opponent with the minimum of their two options.
            dp[i][j] = total_money - min(dp[i + 1][j], dp[i][j - 1])
            
    print(dp[0][n - 1])

n = int(input())
v = list(map(int, input().split()))
solve2(n, v)