from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n 
        cnt = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        s = 0
        longest = max(dp)
        for i in range(n):
            if dp[i] == longest:
                s += cnt[i]
        return s
        

sol = Solution()
nums = [1,3,5,4,7]
print(sol.findNumberOfLIS(nums))