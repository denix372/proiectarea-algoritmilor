from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left_dp = [0] * n
        left_dp[0] = height[0]
        for i in range(1, n):
            left_dp[i] = max(left_dp[i - 1], height[i])

        right_dp = [0] * n
        right_dp[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_dp[i] = max(right_dp[i + 1], height[i])

        total_water = 0
        for i in range(n):
            water_level = min(left_dp[i], right_dp[i])
            total_water += (water_level - height[i])
            
        return total_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))