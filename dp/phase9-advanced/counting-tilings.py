MOD = 10**9 + 7

def solve(n, m):
    transitions = [[] for _ in range(1 << n)]
    
    for mask in range(1 << n):
        valid_next_masks = []
        
        def generate_next(i, j):
            if i == n:
                valid_next_masks.append(j)
                return
                
            if mask & (1 << i):
                generate_next(i + 1, j)
            else:
                generate_next(i + 1, j | (1 << i))

                if i + 1 < n and not (mask & (1 << (i + 1))):
                    generate_next(i + 2, j)

        generate_next(0, 0)
        transitions[mask] = valid_next_masks

    dp = [[0] * (1 << n) for _ in range(m + 1)]
    dp[0][0] = 1
    
    for i in range(m):
        for mask in range(1 << n):
            if dp[i][mask] == 0:
                continue

            for next_mask in transitions[mask]:
                dp[i + 1][next_mask] = (dp[i + 1][next_mask] + dp[i][mask]) % MOD

    print(dp[m][0])

n, m = map(int, input().split())
solve(n, m)