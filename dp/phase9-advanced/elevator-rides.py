import sys
input = sys.stdin.readline

input_data = sys.stdin.read().split()
n = int(input_data[0])
x = int(input_data[1])
w = [int(i) for i in input_data[2:]]

dp = [(n + 1, 0)] * (1 << n)
dp[0] = (1, 0)

for mask in range(1 << n):
    rides, weight = dp[mask]

    for i in range(n):
        if not (mask & (1 << i)):
            
            new_mask = mask | (1 << i)
            
            if weight + w[i] <= x:
                cost = (rides, weight + w[i])
            else:
                cost = (rides + 1, w[i])

            dp[new_mask] = min(dp[new_mask], cost)
            
final_mask = (1 << n) - 1
print(dp[final_mask][0])
