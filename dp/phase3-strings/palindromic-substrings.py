class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        s1 = s
        s2 = s[::-1]

        # Create a table to store lengths of longest common suffixes.
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = 0

        # Build dp[n+1][n+1] in bottom-up fashion.
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                    # MATHEMATICAL TRICK: 
                    # Calculate the required length for it to be a physical palindrome
                    k = i + j - n
                    
                    # If the required length is within the matched suffix length, 
                    # we found exactly one valid palindrome!
                    if 1 <= k <= dp[i][j]:
                        res += 1
                else:
                    dp[i][j] = 0
                    
        return res


sol = Solution()
print(sol.countSubstrings("aaa"))