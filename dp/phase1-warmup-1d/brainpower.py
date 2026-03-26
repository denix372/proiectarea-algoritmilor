from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        dp[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            p, b = questions[i]
            if i + b  + 1 <= n - 1:
                dp[i] = max(p + dp[i + b + 1], dp[i + 1])
            else:
                dp[i] = max(p, dp[i + 1])

        return dp[0]
    
sol = Solution()
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(sol.mostPoints(questions))
        