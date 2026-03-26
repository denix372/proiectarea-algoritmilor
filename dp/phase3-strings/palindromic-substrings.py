class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # lungime 1
        for i in range(n):
            dp[i][i] = True
            count += 1

        # lungime >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    # dacă e "aa" sau "aba"
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1

        return count


sol = Solution()
print(sol.countSubstrings("aaa"))