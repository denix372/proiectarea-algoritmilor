from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        up_dp = [0] * n
        down_dp = [0] * n 
        
        teams = 0

        for i in range(1, n):
            for j in range(i):
                if rating[j] < rating[i]:
                    up_dp[i] += 1
                    teams += up_dp[j]
                    
                elif rating[j] > rating[i]:
                    down_dp[i] += 1
                    teams += down_dp[j]
                    
        return teams


sol = Solution()
rating = [2,5,3,4,1]
print(sol.numTeams(rating))