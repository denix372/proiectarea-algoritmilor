
def tsp(cost):
    n = len(cost)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            # if city u is visited
            if mask & (1 << u): 
                for v in range(n):
                    # if v is not visited
                    if not (mask & (1 << v)):

                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    # We need the cost of visiting all cities (final_mask) + the cost to return to start (0).
    final_mask = (1 << n) - 1
    min_cost = float('inf')

    for i in range(1, n):
        min_cost = min(min_cost, dp[final_mask][i] + cost[i][0])

    return min_cost

cost = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

res = tsp(cost)
print(res)
