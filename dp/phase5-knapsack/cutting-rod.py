#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n = len(price)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            for j in range(i , n + 1):
                dp[j] = max(dp[j], dp[j - i] + price[i - 1])
        return dp[n]
