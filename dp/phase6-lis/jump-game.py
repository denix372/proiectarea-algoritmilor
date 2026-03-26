from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
                
            max_reach = max(max_reach, i + nums[i])
            
            if max_reach >= len(nums) - 1:
                return True
                
        return True

# DP solution but Slow O(n^2)
def canJumpDP(nums):
    n = len(nums)
    dp = [False] * n
    
    dp[0] = True 

    for i in range(1, n):
        for j in range(i):
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break 

    return dp[n - 1]

nums = [2,3,1,1,4]
print(Solution().canJump(nums))
print(canJumpDP(nums))