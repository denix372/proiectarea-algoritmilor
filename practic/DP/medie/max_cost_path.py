def solve(n, m, a):
    inf = float('inf')
    dp = [[[-inf] * (n + 1) for _ in range(n + 1)] for _ in range(n + m - 1)]
    dp[0][0][0] = a[0][0]

    for k in range(n + m - 2):
        for i1 in range(n):
            for i2 in range(n):
                if dp[k][i1][i2] == -inf:
                    continue
                
                # Try all 4 combinations of moves: 
                # (Right, Right), (Right, Down), (Down, Right), (Down, Down)
                for di1, dj1 in [(0, 1), (1, 0)]:
                    for di2, dj2 in [(0, 1), (1, 0)]:
                        ni1, nj1 = i1 + di1, (k - i1) + dj1
                        ni2, nj2 = i2 + di2, (k - i2) + dj2
                        
                        if ni1 < n and nj1 < m and ni2 < n and nj2 < m:
                            val = a[ni1][nj1]
                            # If both paths land on the same cell, add it only once
                            if not (ni1 == ni2 and nj1 == nj2):
                                val += a[ni2][nj2]
                            
                            if dp[k + 1][ni1][ni2] < dp[k][i1][i2] + val:
                                dp[k + 1][ni1][ni2] = dp[k][i1][i2] + val

    print(dp[n + m - 2][n - 1][n - 1])

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
solve(n, m, a)