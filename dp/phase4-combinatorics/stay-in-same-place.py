MOD = 10**9 + 7
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        maxPos = min(arrLen - 1, steps)
        dp = [0] * (maxPos + 1)
        dp[0] = 1

        for _ in range(steps):
            dpPrev = dp[:]
            
            dpLeft  = [0] * (maxPos + 1)
            dpStay  = [0] * (maxPos + 1)
            dpRight = [0] * (maxPos + 1)
            
            for p in range(maxPos + 1):
                dpStay[p] = dpPrev[p]
                
                if p + 1 <= maxPos:
                    dpLeft[p] = dpPrev[p + 1]
                
                if p - 1 >= 0:
                    dpRight[p] = dpPrev[p - 1]
            
            for p in range(maxPos + 1):
                dp[p] = (dpLeft[p] + dpStay[p] + dpRight[p]) % MOD
        
        return dp[0]

steps = 3
arrLen = 2
print(Solution().numWays(steps, arrLen))