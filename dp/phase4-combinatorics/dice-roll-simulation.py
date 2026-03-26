from typing import List

MOD = 10**9 + 7
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n + 1)]
        
        for f in range(6):
            dp[1][f][1] = 1
            
        for i in range(1, n):
            for f in range(6):
                for c in range(1, rollMax[f] + 1):
                    if dp[i][f][c] == 0:
                        continue
                    for next_f in range(6):
                        if next_f == f:
                            if c + 1 <= rollMax[f]:
                                dp[i+1][next_f][c+1] = (dp[i+1][next_f][c+1] +
                                                        dp[i][f][c]) % MOD
                        else:
                            dp[i+1][next_f][1] = (dp[i+1][next_f][1] + 
                                                  dp[i][f][c]) % MOD
                            
        return sum(sum(row) for row in dp[n]) % MOD


n = 2
rollMax = [1,1,2,2,2,3]
print(Solution().dieSimulator(n, rollMax))