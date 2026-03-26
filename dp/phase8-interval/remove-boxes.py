from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for k in range(i + 1):
                    # Option 1: Remove boxes[i] and its 'k' left attachments right now.
                    # We get (k + 1)^2 points, plus whatever the rest of the interval yields.
                    res = (k + 1) * (k + 1)
                    if i + 1 <= j:
                        res += dp[i + 1][j][0]
                    
                    # Option 2: Try to merge with a future box 'm' of the same color.
                    for m in range(i + 1, j + 1):
                        if boxes[i] == boxes[m]:
                            
                            # Cost of removing the middle part: [i+1 to m-1]
                            middle = dp[i + 1][m - 1][0] if (i + 1 <= m - 1) else 0
                            
                            # Cost of solving the right part with k+1 attachments: [m to j]
                            right = dp[m][j][k + 1]
                            
                            res = max(res, middle + right)
                    dp[i][j][k] = res

        # Return the answer for the full array [0 to n-1] with 0 left attachments
        return dp[0][n - 1][0]

boxes = [1,3,2,2,2,3,4,3,1]
print(Solution().removeBoxes(boxes))