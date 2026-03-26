def count_partitions(arr, difference):
    total_sum = sum(arr)
    
    if (total_sum + difference) % 2 != 0 or total_sum < difference:
        return 0
        
    target = (total_sum + difference) // 2
    
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] + dp[j - num] # replace OR with +
            
    return dp[target]


arr = [1, 1, 2, 3]
difference = 1

print(f"Number of ways: {count_partitions(arr, difference)}")