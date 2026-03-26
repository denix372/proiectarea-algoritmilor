class Solution:
    def wildCard(self, txt: str, pat: str) -> bool:
        # code here
        n = len(txt)
        m = len(pat)
    
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            if pat[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if txt[i - 1] == pat[j - 1] or pat[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[n][m]

txt = "abcde"
pat = "a?c*"
print(Solution().wildCard(txt, pat))