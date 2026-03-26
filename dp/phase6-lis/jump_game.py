def canJump(nums):
    n = len(nums)
    
    # dp[i] represents whether we can reach index i
    dp = [False] * n
    
    # Base case: We are already at the first index, so it's reachable
    dp[0] = True 
    
    for i in range(1, n):
        for j in range(i):
            # To reach 'i', we must be able to reach a previous index 'j'
            # AND the jump length from 'j' must be long enough to land on or pass 'i'
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                
                # As soon as we find ONE way to reach 'i', we can stop looking back
                break 
                
    return dp[n - 1]