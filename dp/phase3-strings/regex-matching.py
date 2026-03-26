class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
    
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        # For RegEx, "c*" or "a*b*c*" can match an empty string by choosing zero occurrences.
        # We must look back TWO spaces, not one.
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Choice A: Zero occurrences of the preceding element
                    # We drop the '*' and the character before it
                    dp[i][j] = dp[i][j - 2]
                    
                    # Choice B: One or more occurrences
                    # We can only consume the text character if the preceding pattern character matches
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[n][m]

s = "aa"
p = "a*"
print(Solution().isMatch(s, p))