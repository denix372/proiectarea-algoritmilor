# Dynamic programming approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = 0
        end_pos = 0

        s1 = s
        s2 = s[::-1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                    if dp[i][j] > res:
                        # VERIFICATION TRICK:
                        # Check if the reversed substring maps to the same original physical indices
                        if i - dp[i][j] == n - j:
                            res = dp[i][j]
                            end_pos = i
                else:
                    dp[i][j] = 0

        return s1[end_pos - res : end_pos]

# Two Pointers / Expansion from center approach
def longestPalindrome2(s):
    if not s:
        return ""
    n = len(s)
    start = 0
    end = 0
    res = 0
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1
    
    for i in range(n):
        l, r = i, i 
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > res:
                start = l
                end = r
                res = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > res:
                start = l
                end = r
                res = r - l + 1
            l -= 1
            r += 1

    return s[start: end + 1]
    
print(Solution().longestPalindrome("babad"))
print(longestPalindrome2("babad"))