class Solution:
    def isSubsetSum(self, arr, target):
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] | dp[j - num]
        return dp[target]


arr = [3, 34, 4, 12, 5, 2]
sum = 9
sol = Solution()
print(sol.isSubsetSum(arr, sum))