def count_ap_subsequences(arr):
    n = len(arr)
    if n == 0:
        return 1

    dp = [{} for _ in range(n)]
    
    total_aps = 1 + n
    
    for i in range(1, n):
        for j in range(i):

            diff = arr[i] - arr[j]
            
            aps_ending_at_j = dp[j].get(diff, 0)
            
            dp[i][diff] = dp[i].get(diff, 0) + aps_ending_at_j + 1
    
            total_aps += aps_ending_at_j + 1
            
    return total_aps

arr = [1, 2, 3]
print(count_ap_subsequences(arr))