
# DP approach O(n^2)
def jumps(arr):
    n = len(arr)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n - 1]

# Greedy Approach O(n)


def jumps2(arr):
    n = len(arr)

    maxReach = 0
    currReach = 0
    jump = 0

    for i in range(n):
        maxReach = max(maxReach, i + arr[i])

        if maxReach >= n - 1:
            return jump + 1
        
        if i == currReach:
            if i == maxReach:
                return -1
            else:
                jump += 1
                currReach = maxReach
    
    return -1



arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(jumps(arr))