from typing import List

MOD = 10**9 + 7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        K = len(group)
        
        # dp[k][i][p] 
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(K + 1)]
        
        # Base case: Considering 0 crimes, using 0 members, making 0 profit = 1 way
        dp[0][0][0] = 1
        
        for k in range(1, K + 1):
            members = group[k - 1]
            earn = profit[k - 1]
            
            for i in range(n + 1):
                for p in range(minProfit + 1):
                    
                    # CHOICE 1: Skip the current crime
                    # We keep the exact same members and profit as we had with k-1 crimes
                    skip = dp[k - 1][i][p]
                    
                    # CHOICE 2: Take the current crime
                    take = 0
                    if i >= members:
                        # We look at the state BEFORE we committed this crime
                        prev_profit = max(0, p - earn)
                        take = dp[k - 1][i - members][prev_profit]
                        
                    # Total ways to reach this state is the sum of both choices
                    dp[k][i][p] = (skip + take) % MOD
                    
        # The answer is the sum of all schemes that hit minProfit
        # after considering all K crimes, using anywhere from 0 to n members.
        total_schemes = sum(dp[K][i][minProfit] for i in range(n + 1))
        
        return total_schemes % MOD

n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]
print(Solution().profitableSchemes(n,minProfit, group, profit))